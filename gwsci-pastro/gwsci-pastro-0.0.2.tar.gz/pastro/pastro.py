#!/usr/bin/env python3
import sys
from gstlal import rio
import numpy
from ligo.lw import ligolw
from ligo.lw import utils as ligolw_utils
from ligo.lw.utils import process as ligolw_process
from lal import rate
from optparse import OptionParser
from gstlal import far
import h5py
import sqlite3
from scipy.interpolate import PPoly
from scipy.integrate import quad
import json
import glob
import numpy as np

class pastro_model(object):
  """
  pastro model we build to calculate p(c|x)

  """
  def __init__(self, mcstart = 0.8, mcstop = 500., mcnum = 100, lrstart = -20., lrstop = 90., lrnum = 111, categories = set(["Terrestrial", "BNS", "NSBH", "BBH"])):
    self.mcstart = mcstart
    self.mcstop = mcstop
    self.mcnum = mcnum
    self.lrstart = lrstart
    self.lrstop = lrstop
    self.lrnum = lrnum
    self.categories = categories
    self.lr_thresh = None
    self.expected_counts_above_thresh = None

    self.mcbins = rate.LogarithmicBins(self.mcstart, self.mcstop, int(self.mcnum))
    self.lrbins = rate.LinearBins(self.lrstart, self.lrstop, int(self.lrnum))
    self.bins = rate.NDBins((self.mcbins, self.lrbins))
  
    self.LnPDF = {}
    for category in self.categories:
      self.LnPDF[category] = rate.BinnedLnPDF(self.bins)

    self.p_x_given_ci = {cat:None for cat in self.categories}
    self.p_of_ci = {cat:None for cat in self.categories}
 
  def increment(self, category, mc, lr, cnt = 1):
    # invalidate any stored distributions
    self.p_x_given_ci = {cat:None for cat in self.categories}
    self.p_of_ci = {cat:None for cat in self.categories}

    mc = max(min(mc, self.mcstop), self.mcstart)
    lr = max(min(lr, self.lrstop), self.lrstart)
    self.LnPDF[category].count[(mc, lr)] += cnt

  def add_expected_counts_above_thresh(self, counts, lr_thresh):
    """
    determine N_above_thresh

    """
    # invalidate any stored distributions
    self.p_x_given_ci = {cat:None for cat in self.categories}
    self.p_of_ci = {cat:None for cat in self.categories}

    assert (lr_thresh < self.lrstop and lr_thresh >= self.lrstart)
    self.lr_thresh = lr_thresh
    assert self.categories == set(counts)
    self.expected_counts_above_thresh = counts

  def __iadd__(self, other):
    for attr in ("mcstart", "mcstop", "mcnum", "lrstart", "lrstop", "lrnum"):
      assert getattr(self, attr) == getattr(other, attr)
    assert self.expected_counts_above_thresh is None
    assert self.lr_thresh is None
    categories = self.categories | other.categories
    for category in categories:
      if category in other.categories:
        self.LnPDF[category].count.array += other.LnPDF[category].count.array
      else:
        self.LnPDF[category] = rate.BinnedLnPDF(self.bins)
        self.LnPDF[category].count.array[:] = other.LnPDF[category].count.array[:]
    return self

  def prior(self, d = {"BNS": (1.2, 0.4, -1), "NSBH":(3., 0.5, -1), "BBH":(100., 33., -1), "Terrestrial":(50., 10000., -4)}):
    prior_LnPDF = {}
    for cat in self.categories:
      prior_LnPDF[cat] = rate.BinnedLnPDF(self.bins)
      for mc in self.mcbins.centres():
        for lr in self.lrbins.centres():
          prior_LnPDF[cat].count[(mc, lr)] += numpy.exp(-(mc - d[cat][0])**2 / (2 * d[cat][1]**2)) * (lr - self.lrstart + 1.)**d[cat][2]
      prior_LnPDF[cat].array /= prior_LnPDF[cat].array.sum()
    return prior_LnPDF

  def finalize(self, prior = None):#, mc_KDE_bins, lr_KDE_bins, sigma_KDE, KDE=True):

    """
    this method will set self.lnp_x_given_ci and self.p_ci
    """

    #
    # First produce p_x_given_ci
    #

    # FIXME make these dynamic with silvermans rule
    KDE_bins = 5.0
    KDE_sigma = 10.0
    self.lnp_x_given_ci = {}

    final_lnPDF = {cat: rate.BinnedLnPDF(self.bins) for cat in self.categories}
    for cat in self.categories:
      final_lnPDF[cat].array[:] = self.LnPDF[cat].array[:]
      if prior is not None:
        final_lnPDF[cat].array[:] += prior[cat].array[:]
      lnPDF = final_lnPDF[cat]
      rate.filter_array(lnPDF.array, rate.gaussian_window(KDE_bins, KDE_bins, sigma = KDE_sigma))
      lnPDF.normalize()
      self.lnp_x_given_ci[cat] = lnPDF.mkinterp()


    #
    # Then produce p_ci
    #

    # find the closest index of the LR threshold
    Lix = numpy.searchsorted(self.lrbins.centres(), self.lr_thresh)
    

    # get the L array and dL array
    Ls = self.lrbins.centres()[Lix:]
    dLs = self.lrbins.upper()[Lix:] - self.lrbins.lower()[Lix:]

    # Then get the mc and dmc arrays
    mcs = self.mcbins.centres()
    dmcs = self.mcbins.upper() - self.mcbins.lower()

   
    int_p_x_given_ci_above_L = {}

    for cat in self.categories:
      int_p_x_given_ci_above_L[cat] = 0
      for mc, dmc in zip(mcs, dmcs):
        for L, dL in zip(Ls, dLs):
          lnpdf = self.lnp_x_given_ci[cat](mc, L)
          assert not numpy.isnan(lnpdf)
          int_p_x_given_ci_above_L[cat] += (numpy.exp(lnpdf) * dmc * dL) if numpy.isfinite(lnpdf) else 0.

    #
    # Then compute p_ci
    #

    self.p_ci = {}
    Nsum = sum(self.expected_counts_above_thresh.values())
    for cat in self.categories:
      self.p_ci[cat] = self.expected_counts_above_thresh[cat] / Nsum / int_p_x_given_ci_above_L[cat]


  def __call__(self, data):
    mc = data["mchirp"]
    lr = data["likelihood"]
    out = {}
    for cat in self.categories:
      out[cat] = numpy.exp(self.lnp_x_given_ci[cat](mc, lr)) * self.p_ci[cat]
    norm = sum(out.values())

    p_a = {cat: float(out[cat]/norm) for cat in out}
    return json.dumps(p_a)

  def to_h5(self, fname):
    """
    read to h5 file

    """
    f = h5py.File(fname, "w")
    # FIXME not elegant
    f.attrs['model'] = 0
    dist = f.create_group("distributions")
    dist.create_dataset("mcbins", data=numpy.array([self.mcstart, self.mcstop, self.mcnum]))
    dist.create_dataset("lrbins", data=numpy.array([self.lrstart, self.lrstop, self.lrnum]))
    counts = dist.create_group("counts")
    for category in self.LnPDF:
      counts.create_dataset(category, data = self.LnPDF[category].array)
    if self.lr_thresh is not None:
      dist.create_dataset("lr_thresh", data=self.lr_thresh)
    if self.expected_counts_above_thresh is not None:
      expected = dist.create_group("expected_counts_above_thresh")
      for category in self.expected_counts_above_thresh:
        expected.create_dataset(category, data=self.expected_counts_above_thresh[category])

    f.close()

  @classmethod
  def from_h5(cls, fname):
    """
    read from h5 file
    
    """
    f = h5py.File(fname)
    dist = f["distributions"]
    mcstart, mcstop, mcnum = dist["mcbins"]
    lrstart, lrstop, lrnum = dist["lrbins"]
    categories = set(dist["counts"].keys())

    model = pastro_model(mcstart, mcstop, mcnum, lrstart, lrstop, lrnum, categories)

    for category in categories:
      model.LnPDF[category].count.array[:] = numpy.array(dist["counts"][category])[:]
    if "expected_counts_above_thresh" in dist:
      model.expected_counts_above_thresh = {}
      for category in dist["expected_counts_above_thresh"]:
        model.expected_counts_above_thresh[category] = numpy.array(dist["expected_counts_above_thresh"][category]).item()
    if "lr_thresh" in dist:
        model.lr_thresh = numpy.array(dist["lr_thresh"]).item()
    f.close()
    return model

class p_astro_fgmc(object):
    
    def __init__(self, A_init=0.0, coefficients=0.0, SNR=0.0, indextoid=None, rates={'BBH':0.,'BNS':0.,'NSBH':0.},far_th=2.78e-4,V={'BBH':0.,'BNS':0.,'NSBH':0.}):
        
        categories=list(rates.keys())
        self.categories=categories
        
        self.template_weight_coefficients=coefficients
        self.template_weight_SNR=SNR
        
        self.indextoid=indextoid
        
        self.A=A_init
        self.V=V
        self.rates=rates
        self.far_th=far_th
        self.counts={c:rates[c]*V[c] for c in self.categories}
        self.counts['Terr']=far_th
    
    def read_dir(self, template_weight_dir, rankstat_file, template_bank_database):
      """
      read template_weight, rankstat, and template_bank from the directory path. 
      """
      # set self.template_bank_database
      connection=sqlite3.connect(template_bank_database)
      cur=connection.cursor()
      dtype=[('k',int),('template_id',int)]
      cur.execute('''
            SELECT template.k,template.template_id
            FROM template
            ''')
      indextoid=np.array(cur.fetchall(), dtype=dtype)
      self.indextoid=np.zeros(len(indextoid['k']))
      self.indextoid[indextoid['k']]=indextoid['template_id']
      self.indextoid=self.indextoid.tolist()
      # set self.A
      A,B, fapfar,rankstatpdf,xmin=self.normalize_f_over_b(rankstat_file)
      far_th_file=fapfar.far_from_rank(xmin)
      if self.far_th is None:
          self.far_th=far_th_file
      self.A=A

      # set self.template_weight_dir
      coefficients,SNR=self.load_template_weights(template_weight_dir)
      self.template_weight_coefficients=coefficients
      self.template_weight_SNR=SNR

      # return self  # not needed

    def load_template_weights(self,template_weight_dir):
        filenames=glob.glob(template_weight_dir+'/ceff*.h5')
        coefficients={}
        categories=list(self.categories)
        for fn in filenames:
            f=h5py.File(fn,'r')
            coeff=np.array(f['coefficients'])
            SNR=np.array(f['SNR'])
            for c in categories:
                if c in fn:
                    coefficients[c]=coeff
            f.close()
        
        
        return coefficients,SNR
        
        
    
    def normalize_f_over_b(self,rankstat_file):
        
        rankingstatpdf = far.marginalize_pdf_urls([rankstat_file], "RankingStatPDF", verbose=True)
    
        zero_lag_lr_lnpdf = rankingstatpdf.zero_lag_lr_lnpdf
        zl = rankingstatpdf.zero_lag_lr_lnpdf.copy()
        zl.array[:40] = 0.
    
        if not zl.array.any():
            raise ValueError("zero-lag counts are all zero")
        ln_likelihood_ratio_threshold, = zl.argmax()
    
    
        rankingstatpdf = rankingstatpdf.new_with_extinction()
        fapfar = far.FAPFAR(rankingstatpdf)
        
        
        
        xmin=ln_likelihood_ratio_threshold
    
        rankingstatpdf.noise_lr_lnpdf.array[: rankingstatpdf.noise_lr_lnpdf.bins[0][xmin]]=0.
        rankingstatpdf.noise_lr_lnpdf.normalize()
        rankingstatpdf.signal_lr_lnpdf.array[: rankingstatpdf.signal_lr_lnpdf.bins[0][xmin]]=0.
        rankingstatpdf.signal_lr_lnpdf.normalize()
        rankingstatpdf.zero_lag_lr_lnpdf.array[:rankingstatpdf.zero_lag_lr_lnpdf.bins[0][xmin]]=0.
        rankingstatpdf.zero_lag_lr_lnpdf.normalize()
    
    
        noise_lr_lnpdf=rankingstatpdf.noise_lr_lnpdf.mkinterp()
        lnb=np.vectorize(lambda x: noise_lr_lnpdf(x))
    
        B,dB=quad(lambda x: np.exp(lnb(x)),xmin,np.inf,limit=1000)
    
        A,dA=quad( lambda x : np.exp(x+lnb(x)-np.log(B)),xmin,np.inf,limit=1000)
        
        lnb=None
        
        return A,B, fapfar,rankingstatpdf,xmin
    
    
    
    def calculate_template_weights(self,template_id,snr):
        index=self.indextoid.index(int(template_id))
        
        weights={}
        for c in self.categories:
            weights[c]=np.exp(np.nan_to_num(PPoly(self.template_weight_coefficients[c][:,:,index],self.template_weight_SNR)(snr)))
        return {c:weights[c]/np.sum(list(weights.values())) for c in self.categories}

    
    
    def __call__(self,data,background_weight=1./3.):

        template_id=data['template_id']
        L=data['likelihood']
        snr=data['snr']
        
        f_over_b=np.exp(L)/self.A
        
        template_weights=self.calculate_template_weights(template_id,snr)
        
        if background_weight==1.:
            background_weight=1./len(self.categories)
        
        
        denominator=(1.+(f_over_b)*np.sum(np.array([template_weights[c]*(self.counts[c]/self.counts['Terr']) for c in self.categories]))/background_weight)
    
        numerator={c:f_over_b*(self.counts[c]/self.counts['Terr'])*template_weights[c]/background_weight for c in self.categories}
    
        p_a={c:float(numerator[c]/denominator) for c in self.categories}
    
        p_terr=1.-np.sum([p_a[c] for c in self.categories])
        
        p_a['Terrestrial']=float(p_terr)
        
        return json.dumps(p_a)
    
    # This does nothing
    def prior(self, p=None):
        pass

    # This does nothing
    def finalize(self, prior=None):
        pass
        
    def to_h5(self,filename):
        
        hf=h5py.File(filename,'w')
        # FIXME not elegant
        hf.attrs['model'] = 1
        coefficients=hf.create_group('coefficients')
        for c in self.categories:
            coefficients.create_dataset(c,data=self.template_weight_coefficients[c])
        hf.create_dataset('SNR',data=self.template_weight_SNR)
        
        hf.create_dataset('A',data=np.array([self.A]))
        
        
        rates=hf.create_group('rates')
        for c in list(self.rates.keys()):
            rates.create_dataset(c,data=np.array([self.rates[c]]))
        
        V=hf.create_group('V')
        for c in list(self.V.keys()):
            V.create_dataset(c,data=np.array([self.V[c]]))
        
        hf.create_dataset('far_th',data=np.array([self.far_th]))
        
        hf.create_dataset('indextoid',data=np.array(self.indextoid))
        hf.close()
        
    @classmethod
    def from_h5(cls,filename):
        
        self=cls.__new__(cls)
        hf=h5py.File(filename,'r')
        
        coefficients=hf['coefficients']
        coeff={}
        for c in list(coefficients.keys()):
            coeff[c]=coefficients[c][()]
        self.template_weight_coefficients=coeff
        self.categories=list(coeff.keys())
        self.template_weight_SNR=hf['SNR'][()]
        
        self.A=hf['A'][()][0]
        
        
        self.rates={}
        rates=hf['rates']
        for c in list(rates.keys()):
            self.rates[c]=rates[c][()][0]
        
        self.V={}
        V=hf['V']
        for c in list(V.keys()):
            self.V[c]=V[c][()][0]
        
        self.far_th=hf['far_th'][()][0]
        
        self.counts={c:self.rates[c]*self.V[c] for c in self.categories}
        self.counts['Terr']=self.far_th
        
        self.indextoid=hf['indextoid'][()].tolist()
        hf.close()
        
        return self

MODELS = {
          0: pastro_model(),
          1: p_astro_fgmc()
         }

def load(fname):
  f = h5py.File(fname)
  return MODELS[f.attrs["model"]].from_h5(fname)
