import numpy as np

from mixsim.rir_simulator.source import Source
from mixsim.util.audio import scalar_to_desired_sxr
from mixsim.util.normalization import loudness_norm_rms


class Mixer:
    def __init__(
        self,
        snr_list: list[float],
        sir_list: list[float],
        target_rms_level: float = -25,
        target_rms_level_floating: float = -5,
        mixing_mode: str = "min",
    ) -> None:
        """Initialize the mixer.

        Args:
            snr_list: signal-to-noise ratio (SNR) list.
            sir_list: signal-to-interference ratio (SIR) list.
            target_rms_level: defaults to -25.
            target_rms_level_floating: floating value of level. Defaults to -5.
            mixing_mode: defaults to "min".
        """
        super().__init__()
        self.snr_list = snr_list
        self.sir_list = sir_list
        self.mixing_mode = mixing_mode
        self.target_rms_level = target_rms_level
        self.target_rms_level_floating = target_rms_level_floating

    def _random_select_from(self, dist: list, num=1) -> list:
        """Sample a value from a list."""
        return np.random.choice(dist, num).tolist()

    def mix(self, sources: list[Source], noise: Source) -> Source:
        """Mix the sources and noise.

        Args:
            sources: A list of sources.
            noise: A noise.

        Returns:
            mixed source.
        """
        # 1. Firstly normalize the sources and noise.
        for source in sources:
            source.y, _ = loudness_norm_rms(source.y, target_level=self.target_rms_level)
        noise.y, _ = loudness_norm_rms(noise.y, target_level=self.target_rms_level)

        # 2. Secondly, randomly select snr and sirs.
        sir_list = self._random_select_from(self.sir_list, len(sources) - 1)
        sir_list = [1.0] + sir_list
        snr = self._random_select_from(self.snr_list, 1)
        assert len(snr) == 1, "Only one snr is allowed."
        snr = snr[0]

        # 3. Thirdly, mix the sources and noise.
        for _, (source, sir) in enumerate(zip(sources, sir_list)):
            gain = scalar_to_desired_sxr(sources[0].y, source.y, sir)
            source.y *= gain
            source.loudness_gain = gain

        noise_gain = scalar_to_desired_sxr(sources[0].y, noise.y, snr)
        noise.y *= noise_gain
        noise.loudness_gain = noise_gain

        mix_y = [source.y for source in sources] + [noise.y]
        mix_y = np.array(mix_y).sum(axis=0)
        mix = Source(mix_y)

        return mix
