from lxml import html
import requests
import json
import os


def generate_core():
    prefix = '''import requests
    

class qbittorrent_rpc:
    def __init__(self, secured: bool = False, host: str = "127.0.0.1", port: int = 8080):
        self.s = requests.Session()
        self.rpc_url = "http{}://{}:{}".format("s" if secured else "", host, port)
<init>

    def post(self, api, params):
        return self.s.post(self.rpc_url+api, data=params)'''
    out = ""
    ref = "https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)"
    r = requests.get(ref)
    r = html.fromstring(r.content.decode())
    h1s = r.xpath("//div[@id='wiki-content']//h1")[3:-1]
    names = []
    for h1 in h1s:
        api = h1.xpath("./following-sibling::*[1]/code/text()")[0].replace("methodName", "{}")
        name = "".join(h1.xpath("./text()")).strip()
        print(name)
        hash = ref+"#"+name.lower().replace(" ", "-")
        print(hash)
        out += "\n\n# {}\n".format(hash)
        out += "class {}:\n".format(name.replace("(", "").replace(")", "").replace(" ", "_"))
        names.append(name.replace("(", "").replace(")", "").replace(" ", "_"))
        h2s = []
        while True:
            fs = h1.xpath("./following-sibling::*[1]")
            if not fs:
                break
            fs = fs[0]
            if fs.tag == "h1":
                break
            if fs.tag == "h2":
                h2s.append(fs)
            h1 = fs
        for h2 in h2s:
            name2 = "".join(h2.xpath("./text()")).strip()
            print(name2)
            hash2 = ref+"#"+name2.lower().replace(" ", "-")
            print(hash2)
            ps = []
            while True:
                fs = h2.xpath("./following-sibling::*[1]")
                if not fs:
                    break
                fs = fs[0]
                if fs.tag == "h2":
                    break
                ps.append(fs)
                h2 = fs
            if name2 == "Add trackers to torrent":
                api2 = "addTrackers"
                args = [
                    [
                        "hash",
                        str,
                        "The hash of the torrent"
                    ],
                    [
                        "urls",
                        str,
                        "%0A (aka LF newline) between trackers. Ampersand in tracker urls MUST be escaped."
                    ]
                ]
            elif name2 == "Get torrent download limit":
                api2 = "downloadLimit"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ]
                ]
            elif name2 == "Set torrent download limit":
                api2 = "setDownloadLimit"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "limit",
                        int,
                        "limit is the download speed limit in bytes per second you want to set"
                    ]
                ]
            elif name2 == "Set torrent share limit":
                api2 = "setShareLimits"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "ratioLimit",
                        float,
                        "ratioLimit is the max ratio the torrent should be seeded until. -2 means the global limit should be used, -1 means no limit"
                    ],
                    [
                        "seedingTimeLimit",
                        int,
                        "seedingTimeLimit is the max amount of time the torrent should be seeded. -2 means the global limit should be used, -1 means no limit"
                    ]
                ]
            elif name2 == "Get torrent upload limit":
                api2 = "uploadLimit"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                ]
            elif name2 == "Set torrent upload limit":
                api2 = "setUploadLimit"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "limit",
                        int,
                        "limit is the upload speed limit in bytes per second you want to set"
                    ]
                ]
            elif name2 == "Set torrent location":
                api2 = "setLocation"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "location",
                        str,
                        "location is the location to download the torrent to. If the location doesn't exist, the torrent's location is unchanged"
                    ]
                ]
            elif name2 == "Set torrent name":
                api2 = "rename"
                args = [
                    [
                        "hash",
                        str,
                        "Torrent hash"
                    ],
                    [
                        "name",
                        str,
                        "new name"
                    ]
                ]
            elif name2 == "Set torrent category":
                api2 = "setCategory"
                args = [
                    [
                        "hash",
                        str,
                        "Torrent hash"
                    ],
                    [
                        "name",
                        str,
                        "new name"
                    ]
                ]
            elif name2 == "Add new category":
                api2 = "createCategory"
                args = [
                    [
                        "category",
                        str,
                        "new category"
                    ],
                    [
                        "savePath",
                        str,
                        "save path of new category"
                    ]
                ]
            elif name2 == "Edit category":
                api2 = "editCategory"
                args = [
                    [
                        "category",
                        str,
                        "category"
                    ],
                    [
                        "savePath",
                        str,
                        "new save path of category"
                    ]
                ]
            elif name2 == "Remove categories":
                api2 = "removeCategories"
                args = [
                    [
                        "categories",
                        str,
                        "categories can contain multiple cateogies separated by \\n (%0A urlencoded)"
                    ],
                ]
            elif name2 == "Add torrent tags":
                api2 = "addTags"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "tags",
                        str,
                        "tags is the list of tags you want to add to passed torrents"
                    ],
                ]
            elif name2 == "Remove torrent tags":
                api2 = "removeTags"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "tags",
                        str,
                        "tags is the list of tags you want to remove from passed torrents. Empty list removes all tags from relevant torrents"
                    ],
                ]
            elif name2 == "Create tags":
                api2 = "createTags"
                args = [
                    [
                        "tags",
                        str,
                        "tags is a list of tags you want to create. Can contain multiple tags separated by ,"
                    ],
                ]
            elif name2 == "Delete tags":
                api2 = "deleteTags"
                args = [
                    [
                        "tags",
                        str,
                        "tags is a list of tags you want to create. Can contain multiple tags separated by ,"
                    ],
                ]
            elif name2 == "Set automatic torrent management":
                api2 = "setAutoManagement"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "enable",
                        bool,
                        "enable is a boolean, affects the torrents listed in hashes, default is false"
                    ]
                ]
            elif name2 == "Set force start":
                api2 = "setForceStart"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "value",
                        bool,
                        "value is a boolean, affects the torrents listed in hashes, default is false"
                    ]
                ]
            elif name2 == "Set super seeding":
                api2 = "setSuperSeeding"
                args = [
                    [
                        "hashes",
                        str,
                        "hashes can contain multiple hashes separated by | or set to all"
                    ],
                    [
                        "value",
                        bool,
                        "value is a boolean, affects the torrents listed in hashes, default is false"
                    ]
                ]
            else:
                try:
                    api2 = ps[0].xpath("./code/text()")[0]
                except:
                    try:
                        api2 = ps[1].xpath("./code/text()")[0]
                    except:
                        raise
                args = []
                if name2 == "Add new torrent":
                    api2 = "add"
                    tables = [_ for _ in ps if _.tag == "table" and _.xpath(".//th[contains(text(), 'Property')]")]
                else:
                    tables = [_ for _ in ps if _.tag == "table" and _.xpath(".//th[contains(text(), 'Parameter')]")]
                if len(tables) > 1:
                    raise
                if tables:
                    for tr in tables[0].xpath(".//tbody/tr"):
                        td = [" ".join([str(__) for __ in _.xpath("./{}/text()".format("code" if not _i else ""))]) for _i, _ in enumerate(tr.xpath("./td"))]
                        if len(td) != 3:
                            print(td)
                            raise
                        # print(td)
                        if td[1] == "string":
                            td[1] = str
                        elif td[1] == "bool":
                            td[1] = bool
                        elif td[1] == "integer":
                            td[1] = int
                        elif td[1] == "number":
                            td[1] = int
                        elif td[1] == "raw":
                            td[1] = bytes
                        elif td[1] == "float":
                            td[1] = float
                        td[2] = td[2].replace("\n", "\\n")
                        if type(td[1]).__name__ != "type":
                            if td[0] == "deleteFiles":
                                td[2] = td[1]
                                td[1] = bool
                            else:
                                print(td[1])
                                raise
                        args.append(td)
            print(api2, api.format(api2), args)
            out += "    def {}(\n{}\n    ):\n        # {}\n        data = {{k: v for k, v in {} if v}}\n        return self.post({}, data)\n\n".format(
                api2,
                "        "+",\n        ".join(["self"]+["# {}\n        {}: {} = None".format(_[2], _[0], _[1].__name__) for _ in args]),
                hash2,
                "["+", ".join(["[{}, {}]".format(json.dumps(_[0]), _[0]) for _ in args])+"]",
                json.dumps(api.format(api2))
            )
        out += "    def post(self, *args, **kwargs):\n        ...\n"
    print()
    out = prefix.replace("<init>", "\n".join(["        self.{k} = {k}()\n        self.{k}.post = self.post".format(k=_) for _ in names]))+"\n"+out
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "core.py"), "wb").write(out.encode())


if __name__ == '__main__':
    generate_core()


