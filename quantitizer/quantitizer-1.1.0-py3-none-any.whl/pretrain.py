from mega import Mega

from quantitizer.exceptions import NotFoundModel

__mega = Mega()
__url_map = dict({
    "fasttext-compressed-en-100":
        "https://mega.nz/file/KyA2UDZK#dMbytXDGGiUdIbJyx64OpS3sZKlA2dUkExe5bGbAAkA",
    "w2v-compressed-en-100":
        "https://mega.nz/file/3jQRVRha#gibpsoGJPyPyB93In1ZMk451WWy6vGuZMRO9y4_SbxE"
})


def load(name, outdir="."):
    # m = __mega.login()
    if name not in __url_map:
        raise NotFoundModel("Model not found")

    __mega.download_url(__url_map[name], dest_path=outdir)
    # m.download_url(__url_map[name], dest_path=outdir)
