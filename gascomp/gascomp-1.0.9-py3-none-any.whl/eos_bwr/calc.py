# This file is part of GasComp.

"""
.. module:: calc
   :synopsis: This module contains the thermodynamic BWR EOS calculation.

.. moduleauthor:: Michael Fischer
"""


# Python modules
import numpy
from scipy.optimize import newton, root

from . import data

# Physical constants
R_UNI = 0.08206     # Universal gas constant [atm*m^3/kmol*K]
TNORM = 273.15      # Norm temperature [K]
PNORM = 101325.0    # Norm pressure [Pa]


class Gas():
    """Gas class

       This class contains several methods for the calculation of gas
       properties as well as state changes according to the BWR equation
       of state.
       It takes a gas mixture given as dictionary as input.
    """

    def __init__(self, gasmixture):

        # Input
        self.__gasmixture = gasmixture

        # Mix general properties, BWR coefficients, cpi coefficients
        self.mix_generalPropsAndCoeffs()

        # Norm properties
        self.calc_normProperties()

    def mix_generalPropsAndCoeffs(self):
        """Mix general properties and coefficients."""

        # Init
        Nmix = len(self.__gasmixture)
        psi = numpy.zeros(Nmix)
        genProp = numpy.zeros((Nmix, data.nGenProp))
        bwrCoeffs = numpy.zeros((Nmix, data.nBwr))
        cpiCoeffs = numpy.zeros((Nmix, data.nCpi))

        # Fill
        counter = -1
        for name in self.__gasmixture.keys():
            counter = counter + 1
            psi[counter] = self.__gasmixture[name]
            genProp[counter, :] = (numpy.array(data.dataGenProp[name]) *
                                   numpy.array(data.facsGenProp))
            bwrCoeffs[counter, :] = (numpy.array(data.dataBwr[name]) *
                                     numpy.array(data.facsBwr))
            cpiCoeffs[counter, :] = (numpy.array(data.dataCpi[name]) *
                                     numpy.array(data.facsCpi))

        psi = psi*1.0/numpy.sum(psi)

        # General properties
        self.__genProp_mix = numpy.sum(psi*numpy.transpose(genProp), axis=1)

        # BWR coefficients
        Ag = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_A0]) *
              numpy.sqrt(numpy.abs(bwrCoeffs[:, data.IND_bwr_A0]))))**2
        Bg = (0.25*numpy.sum(psi*bwrCoeffs[:, data.IND_bwr_B0]) +
              0.75*numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_B0]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_B0]))**(1.0/3.0)) *
              numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_B0]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_B0]))**(2.0/3.0)))
        Cg = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_C0]) *
              numpy.sqrt(numpy.abs(bwrCoeffs[:, data.IND_bwr_C0]))))**2
        ak = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_a]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_a]))**(1.0/3.0)))**3
        bk = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_b]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_b]))**(1.0/3.0)))**3
        ck = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_c]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_c]))**(1.0/3.0)))**3
        al = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_alpha]) *
              (numpy.abs(bwrCoeffs[:, data.IND_bwr_alpha]))**(1.0/3.0)))**3
        gam = (numpy.sum(psi*numpy.sign(bwrCoeffs[:, data.IND_bwr_gamma]) *
               (numpy.abs(bwrCoeffs[:, data.IND_bwr_gamma]))**(1.0/2.0)))**2

        self.__bwrCoeffs_mix = numpy.array([Ag, Bg, Cg, ak, bk, ck, al, gam])

        # cpi coefficients
        self.__cpiCoeffs_mix = numpy.sum(psi*numpy.transpose(cpiCoeffs),
                                         axis=1)

    def calc_normProperties(self):
        """Calculate norm properties"""

        self.__ZN = self.calc_realGasFactor_Z(PNORM, TNORM)
        self.__KN = self.calc_compressibility_K(PNORM, TNORM)
        self.__KTN = self.calc_compressibility_KT(PNORM, TNORM)
        self.__KpN = self.calc_compressibility_Kp(PNORM, TNORM)
        self.__R = self.calc_gasConst_R()
        self.__rhoN = self.calc_eos_rho(self.__ZN, PNORM, TNORM)
        self.__cvN = self.calc_cv(PNORM, TNORM)
        self.__cpN = self.calc_cp(PNORM, TNORM)
        self.__kappaN = self.calc_expIsentropic_n(PNORM, TNORM)

    def calc_realGasFactor_Z(self, p, T):
        """Calculate Real gas factor Z.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Real gas factor Z.
        """

        p_atm = p/PNORM

        # Root search
        x0 = p_atm/(R_UNI*T)
        x = newton(self.util_Z_from_rhom, x0, args=(p_atm, T),
                   tol=1.0e-7)

        return p_atm/(x*R_UNI*T)

    def util_Z_from_rhom(self, rhom, p_atm, T):
        """Utility function to calculate real gas factor Z."""

        [Ag, Bg, Cg, ak, bk, ck, al, gam] = self.__bwrCoeffs_mix

        k1 = Bg*R_UNI*T - Ag - Cg/(T**2)
        k2 = bk*R_UNI*T - ak

        grhom2 = gam*rhom**2

        p_bwr = (R_UNI*T*rhom + k1*rhom**2 + k2*rhom**3 + ak*al*rhom**6 +
                 (ck/T**2)*rhom**3*(1 + grhom2)*numpy.exp(-grhom2))

        return p_atm - p_bwr

    def calc_compressibility_K(self, p, T):
        """Caculate compressibility K.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Compressibility K.
        """

        Z = self.calc_realGasFactor_Z(p, T)

        return Z/self.__ZN

    def calc_compressibility_KT(self, p, T):
        """Caculate compressibility KT.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Compressibility KT.
        """

        dT = 0.01

        Zu = self.calc_realGasFactor_Z(p, T-0.5*dT)
        Zm = self.calc_realGasFactor_Z(p, T)
        Zo = self.calc_realGasFactor_Z(p, T+0.5*dT)

        return (T/Zm)*(Zo-Zu)/dT

    def calc_compressibility_Kp(self, p, T):
        """Caculate compressibility Kp.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Compressibility Kp.
        """

        dp = 100.0

        Zu = self.calc_realGasFactor_Z(p-0.5*dp, T)
        Zm = self.calc_realGasFactor_Z(p, T)
        Zo = self.calc_realGasFactor_Z(p+0.5*dp, T)

        return (p/Zm)*(Zo-Zu)/dp

    def calc_gasConst_R(self):
        """Calculate specific gas constant.

        Returns
        -------
        out : float
            Specific gas constant [J/kg*K].
        """

        return 101325.0*R_UNI/self.__genProp_mix[data.IND_molmass]

    def calc_rho(self, p, T):
        """Calculate density.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Density [kg/m3].
        """

        Z = self.calc_realGasFactor_Z(p, T)

        return p/(Z*self.__R*T)

    def calc_eos_rho(self, Z, p, T):
        """Calculate density (general EOS).

        Parameters
        ----------
        Z : float
            Real gas factor.
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Density [kg/m3].
        """

        return p/(Z*self.__R*T)

    def calc_cpi(self, T):
        """Calculate ideal gas specific heat capacity cpi.

        Parameters
        ----------
        p : float
            Pressure [Pa].

        Returns
        -------
        out : float
            Ideal gas specific heat capacity cpi [J/kg*K].
        """

        [A, B, C, D, E] = self.__cpiCoeffs_mix

        cpi = A + B*T + C*T**2 + D*T**3 + E*T**4

        return 1000.0*cpi/self.__genProp_mix[data.IND_molmass]

    def calc_cv(self, p, T):
        """Calculate specific heat capacity cv.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Specific heat capacity cv [J/kg*K].
        """

        cpi = self.calc_cpi(T)

        return cpi - self.__R

    def calc_cp(self, p, T):
        """Calculate specific heat capacity cp.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Specific heat capacity cp [J/kg*K].
        """

        Z = self.calc_realGasFactor_Z(p, T)
        KT = self.calc_compressibility_KT(p, T)
        Kp = self.calc_compressibility_Kp(p, T)

        cv = self.calc_cv(p, T)

        cp = cv + Z*self.__R*(1+KT)**2/(1.0-Kp)

        return cp

    def calc_expPolytropic_n(self, p, T, etap):
        """Calculate polytropic exponent.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].
        etap : float
            Polytropic efficiency.

        Returns
        -------
        out : float
            Polytropic exponent.
        """

        Z = self.calc_realGasFactor_Z(p, T)
        KT = self.calc_compressibility_KT(p, T)
        Kp = self.calc_compressibility_Kp(p, T)

        cv = self.calc_cv(p, T)
        cp = cv + Z*self.__R*(1+KT)**2/(1.0-Kp)

        npoly = (cp/(cp*(1.0-Kp) - Z*self.__R*(1+KT)**2 +
                 Z*self.__R*(1+KT)*(1.0-1.0/etap)))

        return npoly

    def calc_expIsentropic_n(self, p, T):
        """Calculate isentropic exponent.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Isentropic exponent.
        """
        return self.calc_expPolytropic_n(p, T, 1.0)

    def changeOfState_isentropic(self, T1, p1, x1, direction):
        """Isentropic change of state [T1,p1]: x1 -> y1,y2.
        """

        if (direction == "yp_to_T2p2"):
            # (x1) = (yp)
            # (y1,y2) = (T2,p2)
            y1y2_init = [T1, p1]

        elif(direction == "p2_to_T2yp"):
            # (x1) = (p2)
            # (y1,y2) = (etap,yp)
            y1y2_init = [T1, 0.0]

        sol = root(self.util_changeOfState_isentropic_x1_to_y1y2, y1y2_init,
                   args=(T1, p1, x1, direction))
        (y1, y2) = sol.x

        return (y1, y2)

    def changeOfState_polytropic(self, T1, p1, x1, x2, direction):
        """Polytropic change of state [T1,p1]: x1,x2 -> y1,y2.
        """

        if (direction == "etapyp_to_T2p2"):
            # (x1,x2) = (etap,yp)
            # (y1,y2) = (T2,p2)
            y1y2_init = [T1, p1]

        elif(direction == "T2p2_to_etapyp"):
            # (x1,x2) = (T2,p2)
            # (y1,y2) = (etap,yp)
            y1y2_init = [1.0, 0.0]

        elif(direction == "p2yp_to_T2etap"):
            # (x1,x2) = (p2,yp)
            # (y1,y2) = (T2,etap)
            y1y2_init = [T1, 1.0]

        elif(direction == "p2etap_to_T2yp"):
            # (x1,x2) = (p2,etap)
            # (y1,y2) = (T2,yp)
            y1y2_init = [T1, 0.0]

        sol = root(self.util_changeOfState_polytropic_x1x2_to_y1y2,
                   y1y2_init, args=(T1, p1, x1, x2, direction))
        (y1, y2) = sol.x

        return (y1, y2)

    def util_changeOfState_polytropic_x1x2_to_y1y2(self, x, T1, p1, x1, x2,
                                                   direction):
        """Utility function for polytropic change of state [T1,p1]:
           x1,x2 -> y1,y2.
        """

        if (direction == "etapyp_to_T2p2"):
            etap = x1
            yp = x2
            T2 = x[0]
            p2 = x[1]
        elif(direction == "T2p2_to_etapyp"):
            T2 = x1
            p2 = x2
            etap = x[0]
            yp = x[1]
        elif(direction == "p2yp_to_T2etap"):
            p2 = x1
            yp = x2
            T2 = x[0]
            etap = x[1]
        elif(direction == "p2etap_to_T2yp"):
            p2 = x1
            etap = x2
            T2 = x[0]
            yp = x[1]

        return self.util_changeOfState_polytropic_gen(T1, p1, T2, p2, yp, etap)

    def util_changeOfState_isentropic_x1_to_y1y2(self, x, T1, p1, x1,
                                                 direction):
        """Utility function for isentropic change of state [T1,p1]:
           x1 -> y1,y2.
        """

        if (direction == "yp_to_T2p2"):
            yp = x1
            T2 = x[0]
            p2 = x[1]
        elif(direction == "p2_to_T2yp"):
            p2 = x1
            T2 = x[0]
            yp = x[1]

        return self.util_changeOfState_polytropic_gen(T1, p1, T2, p2, yp, 1.0)

    def util_changeOfState_polytropic_gen(self, T1, p1, T2, p2, yp, etap):
        """Utility function for polytropic change of state [T1,p1]: general
        """

        Z1 = self.calc_realGasFactor_Z(p1, T1)
        n1 = self.calc_expPolytropic_n(p1, T1, etap)

        Z1RT1 = self.__R*Z1*T1
        Z2 = self.calc_realGasFactor_Z(p2, T2)
        n2 = self.calc_expPolytropic_n(p2, T2, etap)

        n = 0.5*(n1+n2)
        fac = (n-1.0)/n

        f1 = yp - (Z1RT1/fac)*((p2/p1)**fac - 1.0)
        f2 = -1.0*(T2/T1) + (Z1/Z2)*((p2/p1)**fac)

        return [f1, f2]

    @property
    def gasmixture(self):
        """Gas composition.
        """
        return self.__gasmixture

    @property
    def generalProps(self):
        """General properties.
        """
        return self.__genProp_mix

    @property
    def genProp_molmass(self):
        """Molar mass [kg/kmol].
        """
        return self.__genProp_mix[data.IND_molmass]

    @property
    def normProp_ZN(self):
        """Real gas factor Z in norm state.
        """
        return self.__ZN

    @property
    def normProp_KN(self):
        """Compressibility K in norm state.
        """
        return self.__KN

    @property
    def normProp_KTN(self):
        """Compressibility KT in norm state.
        """
        return self.__KTN

    @property
    def normProp_KpN(self):
        """Compressibility Kp in norm state.
        """
        return self.__KpN

    @property
    def normProp_R(self):
        """Specific gas constant [J/kg*K].
        """
        return self.__R

    @property
    def normProp_rhoN(self):
        """Density [kg/m3] in norm state.
        """
        return self.__rhoN

    @property
    def normProp_cvN(self):
        """Specific heat capacity cv [J/kg*K] in norm state.
        """
        return self.__cvN

    @property
    def normProp_cpN(self):
        """Specific heat capacity cp [J/kg*K] in norm state.
        """
        return self.__cpN

    @property
    def normProp_kappaN(self):
        """Isentropic exponent.
        """
        return self.__kappaN
