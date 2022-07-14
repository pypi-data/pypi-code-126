import warnings

from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.stats import sigma_clip, mad_std
from astropy.utils.exceptions import AstropyUserWarning
from astroquery.exceptions import TableParseError
from astroquery.jplhorizons import Horizons
from astroquery.simbad import Simbad
from lightkurve import LightCurve, LightkurveWarning
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.offsetbox import AnchoredText
import numpy as np
import pandas as pd
from retrying import retry
from wotan import flatten

from .utils import CANDIDATES_COLUMNS, extend, fill_gaps, find_consecutive, get_flare_probability

CUSTOM_SIMBAD = Simbad()
CUSTOM_SIMBAD.add_votable_fields("otype")

CVs = ["CataclyV*", "CataclyV*_Candidate", "Nova", "Nova_Candidate"]
EBs = ["EclBin", "EclBin_Candidate"]


def load_from_lightkurve(lc):
    with warnings.catch_warnings():
        warnings.simplefilter("error", category=LightkurveWarning)

        try:
            lc = lc.normalize()
            lc.meta["ZERO_CENTERED"] = False
        except LightkurveWarning:
            lc.meta["ZERO_CENTERED"] = True
            try:
                lc = lc.select_flux("sap_flux").normalize()
            except LightkurveWarning:
                lc.flux += lc.flux.std() - lc.flux.min()
                lc = lc.normalize()

    flc = FlareLightCurve(lc)

    return flc


class FlareLightCurve(LightCurve):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meta["candidates"] = None

    def _remove_model(self):
        if 0 < self.period <= 2.5 or (0 < self.period <= 5 and self.otype in EBs):
            period_array = np.array([1, 2, 4]) * self.period
            std_array = np.zeros_like(period_array)
            folded_lc_list = []
            trend_folded_flux_list = []

            for i, period in enumerate(period_array):
                folded_lc = self.fold(period)

                detrended_folded_flux, trend_folded_flux = flatten(
                    folded_lc.time.value,
                    folded_lc.flux,
                    method="median",
                    window_length=period / 200,
                    return_trend=True,
                )

                std_array[i] = np.nanstd(detrended_folded_flux)

                folded_lc_list.append(folded_lc)
                trend_folded_flux_list.append(trend_folded_flux)

            std_array *= 0.75 ** np.array([2, 1, 0])
            index = std_array.argmin()

            self.period = period_array[index]

            if 0 < self.period <= 2.5 or (0 < self.period <= 5 and self.otype in EBs):
                trend_folded_flux = trend_folded_flux_list[index]
                folded_lc = folded_lc_list[index]

                model_flux = trend_folded_flux[folded_lc.time_original.argsort()] - 1
                model_flux = sigma_clip(model_flux, sigma_upper=10000, masked=True).filled(np.nan)

                return model_flux

        return 0

    def _standardize(self, window=2):
        # define upper limit by rolling window (window length = 2 d)
        flux_series = pd.Series(self.detrended_flux, index=pd.DatetimeIndex(self.time.datetime))
        rolling_window = flux_series.rolling(pd.Timedelta(window, unit="d"), min_periods=1, center=True)

        rolling_std = rolling_window.apply(mad_std, kwargs={"ignore_nan": True})
        rolling_std[np.isnan(self.detrended_flux)] = np.nan
        standardized_flux = (self.detrended_flux - 1) / rolling_std

        self.add_columns(
            [rolling_std * self.flux.unit, standardized_flux * self.flux.unit],
            names=["rolling_std", "standardized_flux"],
        )

    def _extend_multiple_events(self, i_start_array, i_stop_array, i_extend_limit=45):
        i_start_ext_array = np.zeros_like(i_start_array)
        i_stop_ext_array = np.zeros_like(i_stop_array)

        for i in range(i_start_array.size):
            i_start = i_start_array[i]
            i_stop = i_stop_array[i]

            t_extend_limit = (i_extend_limit + 0.2) * self.meta["TIMEDEL"]
            t_start = self.time.value[i_start] - t_extend_limit
            t_stop = self.time.value[i_stop] + t_extend_limit

            indexes = np.nonzero((self.time.value >= t_start) & (self.time.value <= t_stop))[0]
            i_start_ext, i_stop_ext = extend(self.standardized_flux, i_start, i_stop)

            i_start_ext_array[i] = max(i_start_ext, indexes[0])
            i_stop_ext_array[i] = min(i_stop_ext, indexes[-1])

        i_overlap = np.nonzero(i_start_ext_array[1:] <= i_stop_ext_array[:-1])[0] + 1
        i_overlap_start, i_overlap_stop = find_consecutive(i_overlap, 1)

        if i_overlap_start is not None:
            i_stop_ext_array[i_overlap_start - 1] = i_stop_ext_array[i_overlap_stop]
            i_start_ext_array = np.delete(i_start_ext_array, i_overlap)
            i_stop_ext_array = np.delete(i_stop_ext_array, i_overlap)

        return i_start_ext_array, i_stop_ext_array

    def _is_at_edge(self, i_start: int, i_stop: int, window: float = 30 / 1440):
        """Check if a candidate is at the edge of the lightcurve."""

        time = self.time[~np.isnan(self.standardized_flux)].value
        t_start = self.time.value[i_start]
        t_stop = self.time.value[i_stop]

        before = np.nonzero((time > t_start - window) & (time < t_start))[0]
        after = np.nonzero((time > t_stop) & (time < t_stop + window))[0]

        return False if (before.size and after.size) else True

    @retry(stop_max_attempt_number=10)
    def _is_sso(self, i_peak: int, radius: float = 8):
        """Check if a candidate is caused by a Solar System Object (SSO) encounter."""

        mask = np.zeros_like(self.time, dtype=bool)
        mask[i_peak] = True

        res = self.query_solar_system_objects(cadence_mask=mask, radius=radius * 21 / 3600, show_progress=False)

        if res is not None:
            ap_mag = np.zeros(len(res))
            for row in res.itertuples():
                obj = Horizons(id=row.Name.strip(), location="500@-95", epochs=row.epoch, id_type="smallbody")
                eph = obj.ephemerides(quantities=9)
                try:
                    ap_mag[row.Index] = eph["V"].value
                except KeyError:
                    ap_mag[row.Index] = eph["Tmag"].value
            if (ap_mag < 19).any():
                return True

        return False

    @retry(stop_max_attempt_number=10)
    def _query_object_info_from_simbad(self):
        """Query object info from Simbad."""

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=UserWarning)
            try:
                query_result = CUSTOM_SIMBAD.query_object(self.label)
            except TableParseError:
                try:
                    obj_coord = SkyCoord(self.ra, self.dec, unit=(u.deg, u.deg), frame="icrs")
                    query_result = CUSTOM_SIMBAD.query_region(obj_coord, radius=3 * u.arcsec)
                    if len(query_result) > 1:
                        simbad_coords = SkyCoord(
                            query_result["RA"].data.data, query_result["DEC"].data.data, unit=(u.hourangle, u.deg)
                        )
                        distance = obj_coord.separation(simbad_coords)
                        query_result = query_result[distance.value.argmin()]
                except TableParseError:
                    query_result = None

        self.meta["otype"] = "/" if query_result is None else query_result["OTYPE"][0]

    def _calculate_period(self):
        """Calculate the period of the lightcurve."""

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            pg = self.to_periodogram()
            period = pg.period_at_max_power.value
            snr = pg.max_power / np.nanmedian(pg.power)

            if period < 10 and snr > 4.4:
                pg = self.to_periodogram(
                    minimum_period=max(period - 0.2, 0.01),
                    maximum_period=period + 0.2,
                    oversample_factor=1000,
                )
                self.meta["PERIOD"] = pg.period_at_max_power.value
            else:
                self.meta["PERIOD"] = -999

    def detrend(self, window_length=0.4):
        """Detrend the lightcurve."""
        self._query_object_info_from_simbad()
        self._calculate_period()

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=AstropyUserWarning)

            model_flux = self._remove_model()
            detrended_flux, trend_flux = flatten(
                self.time.value,
                self.flux - model_flux,
                method="biweight",
                window_length=window_length,
                return_trend=True,
            )
            trend_flux += model_flux

            self.add_columns(
                [detrended_flux * self.flux.unit, trend_flux * self.flux.unit], names=["detrended_flux", "trend_flux"]
            )
            self._standardize()

    def find_candidates(self, n_sigma: float = 3, n_consecutive: int = 2):
        """Find the candidates of flares."""

        if self.otype not in CVs:
            i_outliers = np.nonzero(self.standardized_flux > n_sigma)[0]

            i_start_array, i_stop_array = find_consecutive(
                i_outliers, n_consecutive, gap=1.2 * self.meta["TIMEDEL"], data=self.time.value
            )

            if i_start_array is not None:
                i_start_ext_array, i_stop_ext_array = self._extend_multiple_events(i_start_array, i_stop_array)

                at_edge = np.zeros_like(i_start_ext_array, dtype=bool)
                for i in range(at_edge.size):
                    at_edge[i] = self._is_at_edge(i_start_ext_array[i], i_stop_ext_array[i])

                if not at_edge.all():
                    i_start_ext_array = i_start_ext_array[~at_edge]
                    i_stop_ext_array = i_stop_ext_array[~at_edge]

                    i_peak_array = np.copy(i_start_ext_array)
                    for i in range(i_start_ext_array.size):
                        i_peak = self.standardized_flux[i_start_ext_array[i] : i_stop_ext_array[i] + 1].argmax()
                        i_peak_array[i] += i_peak

                    self.candidates = pd.DataFrame(columns=CANDIDATES_COLUMNS)
                    self.candidates.i_start = i_start_ext_array
                    self.candidates.i_peak = i_peak_array
                    self.candidates.i_stop = i_stop_ext_array
                    self.candidates.t_start = self.time.value[i_start_ext_array]
                    self.candidates.t_peak = self.time.value[i_peak_array]
                    self.candidates.t_stop = self.time.value[i_stop_ext_array]

    def mark_sso(self):
        """Mark if the candidates are caused by SSO encounters."""

        if self.candidates is not None:
            sso = np.zeros(len(self.candidates), dtype=bool)

            for row in self.candidates.itertuples():
                sso[row.Index] = self._is_sso(row.i_peak)

            self.candidates.sso = sso

    def calculate_parameters(self):
        """Calculate the parameters of the candidates."""

        if self.candidates is not None:
            best_proba_array = np.zeros(len(self.candidates))
            best_extend = np.zeros(len(self.candidates), dtype=int)

            n_row = 0
            for row in self.candidates.itertuples():
                t_extend_lim = self.time[row.i_stop] + 1.2 * self.meta["TIMEDEL"] * u.day
                n_extend = np.nonzero(self.time < t_extend_lim)[0][-1] - row.i_stop + 1
                proba = np.zeros(n_extend)

                for i in range(n_extend):
                    if self.standardized_flux[row.i_stop + i] <= self.standardized_flux[row.i_stop]:
                        lc_candidate = self[row.i_start : row.i_stop + i + 1].remove_nans("standardized_flux")
                        time = lc_candidate.time.value
                        flux = lc_candidate.standardized_flux

                        if not (np.diff(lc_candidate.cadenceno) == 1).all():
                            time, flux = fill_gaps(time, flux, lc_candidate.cadenceno)

                        if flux.size >= 4:
                            proba[i] = round(get_flare_probability(time, flux), 3)

                best_proba_array[n_row] = np.max(proba)
                best_extend[n_row] = np.argmax(proba)
                n_row += 1

            self.candidates.flare_prob = best_proba_array
            self.candidates.i_stop += best_extend
            self.candidates.t_stop = self.time[self.candidates.i_stop].value

            if not self.meta["ZERO_CENTERED"]:
                amp = np.zeros(len(self.candidates))
                duration = np.zeros(len(self.candidates))
                ed = np.zeros(len(self.candidates))

                n_row = 0
                for row in self.candidates.itertuples():
                    time = self.time.value[row.i_start : row.i_stop + 1]
                    flux = self.detrended_flux[row.i_start : row.i_stop + 1]
                    amp[n_row] = flux.max() - 1
                    duration[n_row] = (time[-1] - time[0]) * 1440
                    ed[n_row] = np.trapz(flux - 1, x=time * 86400)
                    n_row += 1

                self.candidates.amp = np.round(amp, 3)
                self.candidates.duration = np.round(duration, 0).astype(int)
                self.candidates.ed = np.round(ed, 2)

    def output_data(self, folder):
        if self.candidates is not None:
            output = self.candidates.copy()

            output.insert(0, "label", self.label)
            output.insert(1, "sector", self.sector)
            output.t_start = np.round(self.candidates.t_start, 7)
            output.t_stop = np.round(self.candidates.t_stop, 7)

            output.to_csv(folder / "{}-S{}.csv".format(self.label.replace(" ", ""), self.sector), index=False)

    def plot_candidates(self, figure_folder, threshold=0.5):
        """Plot the candidates."""

        if self.candidates is not None:
            self.candidates.loc[self.candidates.sso, "flare_prob"] = -999
            cond_list = [self.candidates.flare_prob >= threshold, self.candidates.flare_prob == -999]
            candidate_type_array = np.select(cond_list, ["flare", "sso"], "non-flare")
            color_array = np.select(cond_list, ["tab:red", "tab:orange"], "tab:gray")

            for row in self.candidates.itertuples():
                candidate_type = candidate_type_array[row.Index]
                color = color_array[row.Index]
                figure_subfolder = figure_folder / candidate_type
                figure_subfolder.mkdir(exist_ok=True)

                fig = plt.figure(figsize=(14, 4))

                ax_label = fig.add_subplot(111)
                ax_label.spines[["top", "bottom", "left", "right"]].set_visible(False)
                ax_label.tick_params(labelcolor="w", top=False, bottom=False, left=False, right=False)
                ax_label.set_xlabel(r"Time - 2457000 [BTJD days]", fontsize=12)
                ax_label.set_ylabel(r"Normalized Flux", fontsize=12)

                ax_original_lc = fig.add_subplot(221)
                ax_original_lc.scatter(self.time.value, self.flux, s=1, lw=0, c="k")
                ax_original_lc.plot(self.time.value, self.trend_flux, lw=1, c="tab:red")
                ax_original_lc.set_xticks([])

                ax_detrended_lc = fig.add_subplot(223)
                ax_detrended_lc.scatter(self.time.value, self.detrended_flux, s=1, lw=0, c="k")
                ax_detrended_lc.plot(self.time.value, 1 + 3 * self.rolling_std, lw=1, c="tab:gray")

                for element in self.candidates.itertuples():
                    alpha = 0.8 if row.Index == element.Index else 0.3

                    event_flux = self.detrended_flux[slice(element.i_start, element.i_stop + 1)]
                    extra_fill_region = (np.nanmax(event_flux) - np.nanmin(event_flux)) / 20
                    fill_lower_lim = np.nanmin(event_flux) - extra_fill_region
                    fill_upper_lim = np.nanmax(event_flux) + extra_fill_region

                    ax_detrended_lc.fill_between(
                        [element.t_start - 0.06, element.t_stop + 0.06],
                        fill_lower_lim,
                        fill_upper_lim,
                        facecolor=color_array[element.Index],
                        alpha=alpha,
                    )

                    ax_detrended_lc.annotate(
                        element.Index + 1,
                        (element.t_start - 0.5, fill_upper_lim),
                        c=color_array[element.Index],
                        alpha=alpha,
                    )

                ax_detrended_lc.set_xlim(*ax_original_lc.get_xlim())

                ax_event = fig.add_subplot(122)
                ax_event.axhline(3, c="tab:gray")
                ax_event.axhline(1, c="tab:gray", ls="--")

                box_str = "Candidate {}, {}".format(row.Index + 1, candidate_type)
                if candidate_type != "sso":
                    box_str += "\nflare probability: {}".format(row.flare_prob)

                at = AnchoredText(box_str, loc="upper right", frameon=True, prop={"multialignment": "right"})
                at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
                ax_event.add_artist(at)

                t_extend = 30.2 * self.meta["TIMEDEL"]

                i_plot = np.nonzero(
                    (self.time.value >= row.t_start - t_extend) & (self.time.value <= row.t_stop + t_extend)
                )
                ax_event.plot(self.time.value[i_plot], self.standardized_flux[i_plot], lw=1, ms=5, marker=".", c="k")

                i_event = slice(row.i_start, row.i_stop + 1)
                ax_event.plot(self.time.value[i_event], self.standardized_flux[i_event], ms=7, marker=".", c=color)

                ax_event.xaxis.set_major_locator(MaxNLocator(5))
                ax_event.yaxis.set_major_locator(MaxNLocator(integer=True))
                ax_event.set_xlim(
                    row.t_start - t_extend + self.meta["TIMEDEL"], row.t_stop + t_extend - self.meta["TIMEDEL"]
                )
                if self.standardized_flux[i_plot].min() < -6:
                    ax_event.set_ylim(bottom=-6)
                ax_event.set_ylabel(r"Standardized Flux", fontsize=12)
                ax_event.ticklabel_format(useOffset=False)
                ax_event.yaxis.set_label_position("right")
                ax_event.yaxis.tick_right()

                for ax in [ax_original_lc, ax_detrended_lc]:
                    ax.yaxis.set_major_locator(MaxNLocator(4))

                for ax in [ax_original_lc, ax_detrended_lc, ax_event]:
                    ax.minorticks_on()
                    ax.tick_params(which="both", direction="in")
                    ax.tick_params(axis="both", labelsize=12)

                ax_label.set_yticks(ax_detrended_lc.get_yticks())

                title = f"{self.label}, Sector {self.sector}, {self.otype}"
                title += ", P={:.2f}d".format(self.period) if self.period > 0 else ", P=/"

                plt.suptitle(title, y=0.94, fontsize=13)
                plt.subplots_adjust(hspace=0.05, wspace=0.012)

                figure_path = figure_subfolder / "{}-S{}-{}.png".format(
                    self.label.replace(" ", ""), self.sector, row.Index + 1
                )
                plt.savefig(figure_path, bbox_inches="tight")
                plt.close()
