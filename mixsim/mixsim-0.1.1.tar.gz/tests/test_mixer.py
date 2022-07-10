import numpy as np
from mixsim.util.normalization import loudness_norm_max, loudness_norm_rms
from mixsim.util.audio import sxr_mix, compute_sxr, is_audio


class TestMixer:
    def test_loudness_max_norm(self):
        y = np.random.random((2, 16000))
        y, _ = loudness_norm_max(y, ref_mic=0)
        assert y.ndim == 2

    def test_single_channel_loudness_max_norm(self):
        y = np.random.random(16000)
        y, _ = loudness_norm_max(y)
        assert y.ndim == 1

    def test_loudness_rms_norm(self):
        y = np.random.random((2, 16000))
        y, _ = loudness_norm_rms(y, ref_mic=0)
        assert y.ndim == 2

    def test_sxr_mix(self):
        meaningful = np.random.random((2, 16000))
        meaningless = np.random.random((2, 16000))
        sxr = 0
        target_rms = -25
        target_rms_floating = 5
        ref_mic = 0

        mix, meaningful, meaningless = sxr_mix(
            meaningful,
            meaningless,
            sxr,
            target_rms,
            target_rms_floating,
            ref_mic=ref_mic,
        )

        new_sxr = compute_sxr(meaningful, meaningless, ref_mic=ref_mic)

        sxr_gap = abs(new_sxr - sxr)
        assert sxr_gap <= 1, f"SNR gap: {sxr_gap}"

    def test_check_is_audio(self):
        meaningful = np.random.random((2, 16000))
        meaningless = np.random.random((2, 16000))
        is_audio([meaningful, meaningless], 0)

        meaningful = np.random.random(16000)
        meaningless = np.random.random(16000)
        is_audio([meaningful, meaningless], 0)
