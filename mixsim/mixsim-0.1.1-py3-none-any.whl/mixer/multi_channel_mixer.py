import numpy as np

from mixsim.mixer.base_mixer import Mixer
from mixsim.rir_simulator.source import Source
from mixsim.util.audio import is_clipped


class MultiChannelMixer(Mixer):
    """Mixer class for generating multi-channel mixture."""

    def __init__(
        self,
    ) -> None:
        pass

    def sample_snr(self, snr_list, num):
        select_snr_list = np.random.choice(snr_list, size=num)

    def mix_sources(self, sources: list[Source]):
        pass

    @staticmethod
    def check_audio_availability(y_s, ref_mic=-1):
        if not isinstance(y_s, list):
            y_s = [y_s]

        for y in y_s:
            assert y.ndim in (1, 2), "Only support signals with the shape of [C, T] or [T]."

            if y.ndim == 2:
                assert ref_mic >= 0, "The input is multi-channel. Assign an explicit reference mic for computation."

    def compute_rms(self, y, ref_mic=-1):
        self.check_audio_availability(y, ref_mic=ref_mic)
        return np.sqrt(np.mean(y**2))

    def loudness_max_norm(self, y, scalar=None, ref_mic=-1, eps=1e-6):
        """Maximum normalization to signals."""
        self.check_audio_availability(y, ref_mic=ref_mic)

        if not scalar:
            if y.ndim == 1:
                scalar = np.max(np.abs(y)) + eps
            else:
                scalar = np.max(np.abs(y[ref_mic, :])) + eps

        y /= scalar

        return y, scalar

    def loudness_rms_norm(self, y, target_rms=-25, scalar=None, ref_mic=-1, eps=1e-6):
        """Loudness normalization based on the Root Mean Square (RMS).

        Normalize the RMS of signals to a given RMS based on Decibels Relative to Full Scale
        (dBFS).

        Note: A small amount of signal samples would be clipped after normalization, but it
        does not matter.
        """
        self.check_audio_availability(y, ref_mic=ref_mic)

        if not scalar:
            if y.ndim == 1:
                current_rms = self.compute_rms(y)
            else:
                current_rms = self.compute_rms(y[ref_mic, :])

            scalar = 10 ** (target_rms / 20) / (current_rms + eps)

        y *= scalar

        return y, scalar

    def scalar_to_desired_sxr(self, meaningful, meaningless, desired_ratio, ref_mic=-1, eps=1e-6):
        """Generally calculate the scalar of the noise or interference to fulfill a desired
        SXR (SNR or SIR) ratio.

        Args:
            meaningful: meaningful input, like target clean
            meaningless: meaningless or unwanted input, like background noise
            desired_ratio: SNR or SIR ratio

        Returns:
            Scalar, which can be used to adjust the RMS of the meaningless signals to
            satisfy the given ratio.
        """
        self.check_audio_availability([meaningful, meaningless], ref_mic=ref_mic)

        meaningful_rms = self.compute_rms(meaningful if meaningful.ndim == 1 else meaningful[ref_mic, :])
        meaningless_rms = self.compute_rms(meaningless if meaningless.ndim == 1 else meaningless[ref_mic, :])

        scalar = meaningful_rms / (10 ** (desired_ratio / 20)) / (meaningless_rms + eps)

        return scalar

    def sir_snr_mix(self, tgt, ref, noise, sir, snr, target_rms, target_rms_floating, ref_mic=-1, eps=1e-6):
        """
        Shapes:
            meaningful: [C, T] or [T,]
            meaningless: [T,]
            mix: [C, T] or [T,]
        """
        self.check_audio_availability([tgt, ref], ref_mic=ref_mic)

        tgt, _ = self.loudness_max_norm(tgt, ref_mic=ref_mic)
        tgt, _ = self.loudness_rms_norm(tgt, target_rms, ref_mic=ref_mic)

        ref, _ = self.loudness_max_norm(ref, ref_mic=ref_mic)
        ref, _ = self.loudness_rms_norm(ref, target_rms, ref_mic=ref_mic)

        noise, _ = self.loudness_max_norm(noise, ref_mic=ref_mic)
        noise, _ = self.loudness_rms_norm(noise, target_rms, ref_mic=ref_mic)

        sir_scalar = self.scalar_to_desired_sxr(tgt, ref, sir, ref_mic=ref_mic)
        snr_scalar = self.scalar_to_desired_sxr(tgt, noise, snr, ref_mic=ref_mic)

        ref *= sir_scalar
        noise *= snr_scalar

        mix = tgt + ref + noise

        mix_target_rms = np.random.randint(target_rms - target_rms_floating, target_rms + target_rms_floating)
        mix, mix_scalar = self.loudness_rms_norm(mix, mix_target_rms, ref_mic=ref_mic)

        # After rescale the noisy signal, there still need to rescale the clean and noise signals such that
        # the saved audio signals has a correct SNR ratio.
        # When training neural networks, you could apply loudness norm again.
        tgt *= mix_scalar
        ref *= mix_scalar
        noise *= mix_scalar

        # May exceed [-1, 1].
        if is_clipped(mix):
            mix_scalar = np.max(np.abs(mix)) / (0.99 - eps)  # 相当于除以 1
            mix = mix / mix_scalar
            tgt = tgt / mix_scalar
            ref = ref / mix_scalar
            noise = noise / mix_scalar

        return mix, tgt, ref, noise

    def mix(self, sources: list[Source], overlap_ratios: list[float], noise: Source):
        """Mix sources and noise."""
        assert len(sources) == len(overlap_ratios), "Number of sources and overlap ratios must be equal."

        # Mix sources and noise.
        mixed_sources = []
        for source, overlap_ratio in zip(sources, overlap_ratios):
            pass
