from gensim.models import KeyedVectors

from quantitizer import quantitize


def quantitize_wv(wv, sub_size, mode="cpu", n_iter=5):
    if mode == "cpu":
        wv_q = make_new_wv_model(
            wv, quantitize(wv.vectors, sub_size=sub_size, n_iter=n_iter))
    elif mode == "cuda":
        from quantitizer.cuda import quantitize_cuda

        wv_q = make_new_wv_model(
            wv, quantitize_cuda(wv.vectors, sub_size=sub_size, n_iter=n_iter))
    else:
        raise ValueError("mode must be 'cpu' or 'cuda'")

    return wv_q


def load_wv(path):
    wv = KeyedVectors.load(path)
    return wv


def make_new_wv_model(
        wv,
        new_vectors,
        new_vocab=None,
        cls=None,
):
    cls = cls or KeyedVectors
    # let the model be the ultimate type before saving+loading it
    # cls = cls or gensim.models.fasttext.FastTextKeyedVectors
    new_wv = cls(
        vector_size=wv.vector_size
    )
    new_wv.vectors_vocab = None  # if we don't fine tune the model we don't need these vectors
    new_wv.vectors = new_vectors  # quantized vectors top_vectors
    if new_vocab is None:
        new_wv.key_to_index = wv.key_to_index
    else:
        new_wv.key_to_index = new_vocab

    if hasattr(new_wv, 'update_index2word'):
        new_wv.update_index2word()

    return new_wv
