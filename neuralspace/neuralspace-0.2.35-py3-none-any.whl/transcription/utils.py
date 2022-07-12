from neuralspace.transcription.constants import DOMAIN, SAMPLE_RATE, SUBURL
from neuralspace.transcription.language_map import LANGUAGE_MAP


def get_sample_rate_and_suburl_from_language(language: str, domain: str):
    sub_url = None
    sample_rate = None
    model_map = LANGUAGE_MAP
    language_models = model_map.get(language, None)
    for model in language_models:
        if model[DOMAIN] == domain:
            sub_url = model.get(SUBURL, None)
            sample_rate = model.get(SAMPLE_RATE, None)

    return sub_url, sample_rate
