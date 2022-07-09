import requests
    

class qbittorrent_rpc:
    def __init__(self, secured: bool = False, host: str = "127.0.0.1", port: int = 8080):
        self.s = requests.Session()
        self.rpc_url = "http{}://{}:{}".format("s" if secured else "", host, port)
        self.Authentication = Authentication()
        self.Authentication.post = self.post
        self.Application = Application()
        self.Application.post = self.post
        self.Log = Log()
        self.Log.post = self.post
        self.Sync = Sync()
        self.Sync.post = self.post
        self.Transfer_info = Transfer_info()
        self.Transfer_info.post = self.post
        self.Torrent_management = Torrent_management()
        self.Torrent_management.post = self.post
        self.RSS_experimental = RSS_experimental()
        self.RSS_experimental.post = self.post
        self.Search = Search()
        self.Search.post = self.post

    def post(self, api, params):
        return self.s.post(self.rpc_url+api, data=params)


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#authentication
class Authentication:
    def login(
        self,
        # Username used to access the WebUI
        username: str = None,
        # Password used to access the WebUI
        password: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#login
        data = {k: v for k, v in [["username", username], ["password", password]] if v}
        return self.post("/api/v2/auth/login", data)

    def logout(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#logout
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/auth/logout", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#application
class Application:
    def version(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-version
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/version", data)

    def webapiVersion(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-api-version
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/webapiVersion", data)

    def buildInfo(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-build-info
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/buildInfo", data)

    def shutdown(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#shutdown-application
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/shutdown", data)

    def preferences(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-preferences
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/preferences", data)

    def setPreferences(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-application-preferences
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/setPreferences", data)

    def defaultSavePath(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-default-save-path
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/app/defaultSavePath", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#log
class Log:
    def main(
        self,
        # Include normal messages (default:  true )
        normal: bool = None,
        # Include info messages (default:  true )
        info: bool = None,
        # Include warning messages (default:  true )
        warning: bool = None,
        # Include critical messages (default:  true )
        critical: bool = None,
        # Exclude messages with "message id" <=  last_known_id  (default:  -1 )
        last_known_id: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-log
        data = {k: v for k, v in [["normal", normal], ["info", info], ["warning", warning], ["critical", critical], ["last_known_id", last_known_id]] if v}
        return self.post("/api/v2/log/main", data)

    def peers(
        self,
        # Exclude messages with "message id" <=  last_known_id  (default:  -1 )
        last_known_id: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-peer-log
        data = {k: v for k, v in [["last_known_id", last_known_id]] if v}
        return self.post("/api/v2/log/peers", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#sync
class Sync:
    def maindata(
        self,
        # Response ID. If not provided,  rid=0  will be assumed. If the given  rid  is different from the one of last server reply,  full_update  will be  true  (see the server reply details for more info)
        rid: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-main-data
        data = {k: v for k, v in [["rid", rid]] if v}
        return self.post("/api/v2/sync/maindata", data)

    def torrentPeers(
        self,
        # Torrent hash
        hash: str = None,
        # Response ID. If not provided,  rid=0  will be assumed. If the given  rid  is different from the one of last server reply,  full_update  will be  true  (see the server reply details for more info)
        rid: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-peers-data
        data = {k: v for k, v in [["hash", hash], ["rid", rid]] if v}
        return self.post("/api/v2/sync/torrentPeers", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#transfer-info
class Transfer_info:
    def info(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-transfer-info
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/transfer/info", data)

    def speedLimitsMode(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-alternative-speed-limits-state
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/transfer/speedLimitsMode", data)

    def toggleSpeedLimitsMode(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#toggle-alternative-speed-limits
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/transfer/toggleSpeedLimitsMode", data)

    def downloadLimit(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-download-limit
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/transfer/downloadLimit", data)

    def setDownloadLimit(
        self,
        # The global download speed limit to set in bytes/second
        limit: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-global-download-limit
        data = {k: v for k, v in [["limit", limit]] if v}
        return self.post("/api/v2/transfer/setDownloadLimit", data)

    def uploadLimit(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-upload-limit
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/transfer/uploadLimit", data)

    def setUploadLimit(
        self,
        # The global upload speed limit to set in bytes/second
        limit: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-global-upload-limit
        data = {k: v for k, v in [["limit", limit]] if v}
        return self.post("/api/v2/transfer/setUploadLimit", data)

    def banPeers(
        self,
        # The peer to ban, or multiple peers separated by a pipe  | . Each peer is a colon-separated  host:port \n
        peers: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#ban-peers
        data = {k: v for k, v in [["peers", peers]] if v}
        return self.post("/api/v2/transfer/banPeers", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management
class Torrent_management:
    def info(
        self,
        # Filter torrent list by state. Allowed state filters:  all ,  downloading ,  seeding ,  completed ,  paused ,  active ,  inactive ,  resumed ,  stalled ,  stalled_uploading ,  stalled_downloading ,  errored \n
        filter: str = None,
        # Get torrents with the given category (empty string means "without category"; no "category" parameter means "any category" <- broken until  #11748  is resolved). Remember to URL-encode the category name. For example,  My category  becomes  My%20category \n
        category: str = None,
        # Get torrents with the given tag (empty string means "without tag"; no "tag" parameter means "any tag". Remember to URL-encode the category name. For example,  My tag  becomes  My%20tag \n
        tag: str = None,
        # Sort torrents by given key. They can be sorted using any field of the response's JSON array (which are documented below) as the sort key.
        sort: str = None,
        # Enable reverse sorting. Defaults to  false \n
        reverse: bool = None,
        # Limit the number of torrents returned
        limit: int = None,
        # Set offset (if less than 0, offset from end)
        offset: int = None,
        # Filter by hashes. Can contain multiple hashes separated by  | \n
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-list
        data = {k: v for k, v in [["filter", filter], ["category", category], ["tag", tag], ["sort", sort], ["reverse", reverse], ["limit", limit], ["offset", offset], ["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/info", data)

    def properties(
        self,
        # The hash of the torrent you want to get the generic properties of
        hash: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-generic-properties
        data = {k: v for k, v in [["hash", hash]] if v}
        return self.post("/api/v2/torrents/properties", data)

    def trackers(
        self,
        # The hash of the torrent you want to get the trackers of
        hash: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-trackers
        data = {k: v for k, v in [["hash", hash]] if v}
        return self.post("/api/v2/torrents/trackers", data)

    def webseeds(
        self,
        # The hash of the torrent you want to get the webseeds of
        hash: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-web-seeds
        data = {k: v for k, v in [["hash", hash]] if v}
        return self.post("/api/v2/torrents/webseeds", data)

    def files(
        self,
        # The hash of the torrent you want to get the contents of
        hash: str = None,
        # The indexes of the files you want to retrieve.  indexes  can contain multiple values separated by  | .
        indexes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-contents
        data = {k: v for k, v in [["hash", hash], ["indexes", indexes]] if v}
        return self.post("/api/v2/torrents/files", data)

    def pieceStates(
        self,
        # The hash of the torrent you want to get the pieces' states of
        hash: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-pieces'-states
        data = {k: v for k, v in [["hash", hash]] if v}
        return self.post("/api/v2/torrents/pieceStates", data)

    def pieceHashes(
        self,
        # The hash of the torrent you want to get the pieces' hashes of
        hash: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-pieces'-hashes
        data = {k: v for k, v in [["hash", hash]] if v}
        return self.post("/api/v2/torrents/pieceHashes", data)

    def pause(
        self,
        # The hashes of the torrents you want to pause.  hashes  can contain multiple hashes separated by  | , to pause multiple torrents, or set to  all , to pause all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#pause-torrents
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/pause", data)

    def resume(
        self,
        # The hashes of the torrents you want to resume.  hashes  can contain multiple hashes separated by  | , to resume multiple torrents, or set to  all , to resume all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#resume-torrents
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/resume", data)

    def delete(
        self,
        # The hashes of the torrents you want to delete.  hashes  can contain multiple hashes separated by  | , to delete multiple torrents, or set to  all , to delete all torrents.
        hashes: str = None,
        # If set to  true , the downloaded data will also be deleted, otherwise has no effect.
        deleteFiles: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-torrents
        data = {k: v for k, v in [["hashes", hashes], ["deleteFiles", deleteFiles]] if v}
        return self.post("/api/v2/torrents/delete", data)

    def recheck(
        self,
        # The hashes of the torrents you want to recheck.  hashes  can contain multiple hashes separated by  | , to recheck multiple torrents, or set to  all , to recheck all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#recheck-torrents
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/recheck", data)

    def reannounce(
        self,
        # The hashes of the torrents you want to reannounce.  hashes  can contain multiple hashes separated by  | , to reannounce multiple torrents, or set to  all , to reannounce all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#reannounce-torrents
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/reannounce", data)

    def add(
        self,
        # URLs separated with newlines
        urls: str = None,
        # Raw data of torrent file.  torrents  can be presented multiple times.
        torrents: bytes = None,
        # Download folder
        savepath: str = None,
        # Cookie sent to download the .torrent file
        cookie: str = None,
        # Category for the torrent
        category: str = None,
        # Tags for the torrent, split by ','
        tags: str = None,
        # Skip hash checking. Possible values are  true ,  false  (default)
        skip_checking: str = None,
        # Add torrents in the paused state. Possible values are  true ,  false  (default)
        paused: str = None,
        # Create the root folder. Possible values are  true ,  false , unset (default)
        root_folder: str = None,
        # Rename torrent
        rename: str = None,
        # Set torrent upload speed limit. Unit in bytes/second
        upLimit: int = None,
        # Set torrent download speed limit. Unit in bytes/second
        dlLimit: int = None,
        # Set torrent share ratio limit
        ratioLimit: float = None,
        # Set torrent seeding time limit. Unit in seconds
        seedingTimeLimit: int = None,
        # Whether Automatic Torrent Management should be used
        autoTMM: bool = None,
        # Enable sequential download. Possible values are  true ,  false  (default)
        sequentialDownload: str = None,
        # Prioritize download first last piece. Possible values are  true ,  false  (default)
        firstLastPiecePrio: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-new-torrent
        data = {k: v for k, v in [["urls", urls], ["torrents", torrents], ["savepath", savepath], ["cookie", cookie], ["category", category], ["tags", tags], ["skip_checking", skip_checking], ["paused", paused], ["root_folder", root_folder], ["rename", rename], ["upLimit", upLimit], ["dlLimit", dlLimit], ["ratioLimit", ratioLimit], ["seedingTimeLimit", seedingTimeLimit], ["autoTMM", autoTMM], ["sequentialDownload", sequentialDownload], ["firstLastPiecePrio", firstLastPiecePrio]] if v}
        return self.post("/api/v2/torrents/add", data)

    def addTrackers(
        self,
        # The hash of the torrent
        hash: str = None,
        # %0A (aka LF newline) between trackers. Ampersand in tracker urls MUST be escaped.
        urls: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-trackers-to-torrent
        data = {k: v for k, v in [["hash", hash], ["urls", urls]] if v}
        return self.post("/api/v2/torrents/addTrackers", data)

    def editTracker(
        self,
        # The hash of the torrent
        hash: str = None,
        # The tracker URL you want to edit
        origUrl: str = None,
        # The new URL to replace the  origUrl \n
        newUrl: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#edit-trackers
        data = {k: v for k, v in [["hash", hash], ["origUrl", origUrl], ["newUrl", newUrl]] if v}
        return self.post("/api/v2/torrents/editTracker", data)

    def removeTrackers(
        self,
        # The hash of the torrent
        hash: str = None,
        # URLs to remove, separated by  | \n
        urls: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-trackers
        data = {k: v for k, v in [["hash", hash], ["urls", urls]] if v}
        return self.post("/api/v2/torrents/removeTrackers", data)

    def addPeers(
        self,
        # The hash of the torrent, or multiple hashes separated by a pipe  | \n
        hashes: str = None,
        # The peer to add, or multiple peers separated by a pipe  | . Each peer is a colon-separated  host:port \n
        peers: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-peers
        data = {k: v for k, v in [["hashes", hashes], ["peers", peers]] if v}
        return self.post("/api/v2/torrents/addPeers", data)

    def increasePrio(
        self,
        # The hashes of the torrents you want to increase the priority of.  hashes  can contain multiple hashes separated by  | , to increase the priority of multiple torrents, or set to  all , to increase the priority of all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#increase-torrent-priority
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/increasePrio", data)

    def decreasePrio(
        self,
        # The hashes of the torrents you want to decrease the priority of.  hashes  can contain multiple hashes separated by  | , to decrease the priority of multiple torrents, or set to  all , to decrease the priority of all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#decrease-torrent-priority
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/decreasePrio", data)

    def topPrio(
        self,
        # The hashes of the torrents you want to set to the maximum priority.  hashes  can contain multiple hashes separated by  | , to set multiple torrents to the maximum priority, or set to  all , to set all torrents to the maximum priority.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#maximal-torrent-priority
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/topPrio", data)

    def bottomPrio(
        self,
        # The hashes of the torrents you want to set to the minimum priority.  hashes  can contain multiple hashes separated by  | , to set multiple torrents to the minimum priority, or set to  all , to set all torrents to the minimum priority.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#minimal-torrent-priority
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/bottomPrio", data)

    def filePrio(
        self,
        # The hash of the torrent
        hash: str = None,
        # File ids, separated by  | \n
        id: str = None,
        # File priority to set (consult  torrent contents API  for possible values)
        priority: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-file-priority
        data = {k: v for k, v in [["hash", hash], ["id", id], ["priority", priority]] if v}
        return self.post("/api/v2/torrents/filePrio", data)

    def downloadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-download-limit
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/downloadLimit", data)

    def setDownloadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # limit is the download speed limit in bytes per second you want to set
        limit: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-download-limit
        data = {k: v for k, v in [["hashes", hashes], ["limit", limit]] if v}
        return self.post("/api/v2/torrents/setDownloadLimit", data)

    def setShareLimits(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # ratioLimit is the max ratio the torrent should be seeded until. -2 means the global limit should be used, -1 means no limit
        ratioLimit: float = None,
        # seedingTimeLimit is the max amount of time the torrent should be seeded. -2 means the global limit should be used, -1 means no limit
        seedingTimeLimit: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-share-limit
        data = {k: v for k, v in [["hashes", hashes], ["ratioLimit", ratioLimit], ["seedingTimeLimit", seedingTimeLimit]] if v}
        return self.post("/api/v2/torrents/setShareLimits", data)

    def uploadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-upload-limit
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/uploadLimit", data)

    def setUploadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # limit is the upload speed limit in bytes per second you want to set
        limit: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-upload-limit
        data = {k: v for k, v in [["hashes", hashes], ["limit", limit]] if v}
        return self.post("/api/v2/torrents/setUploadLimit", data)

    def setLocation(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # location is the location to download the torrent to. If the location doesn't exist, the torrent's location is unchanged
        location: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-location
        data = {k: v for k, v in [["hashes", hashes], ["location", location]] if v}
        return self.post("/api/v2/torrents/setLocation", data)

    def rename(
        self,
        # Torrent hash
        hash: str = None,
        # new name
        name: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-name
        data = {k: v for k, v in [["hash", hash], ["name", name]] if v}
        return self.post("/api/v2/torrents/rename", data)

    def setCategory(
        self,
        # Torrent hash
        hash: str = None,
        # new name
        name: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-category
        data = {k: v for k, v in [["hash", hash], ["name", name]] if v}
        return self.post("/api/v2/torrents/setCategory", data)

    def categories(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-categories
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/torrents/categories", data)

    def createCategory(
        self,
        # new category
        category: str = None,
        # save path of new category
        savePath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-new-category
        data = {k: v for k, v in [["category", category], ["savePath", savePath]] if v}
        return self.post("/api/v2/torrents/createCategory", data)

    def editCategory(
        self,
        # category
        category: str = None,
        # new save path of category
        savePath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#edit-category
        data = {k: v for k, v in [["category", category], ["savePath", savePath]] if v}
        return self.post("/api/v2/torrents/editCategory", data)

    def removeCategories(
        self,
        # categories can contain multiple cateogies separated by \n (%0A urlencoded)
        categories: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-categories
        data = {k: v for k, v in [["categories", categories]] if v}
        return self.post("/api/v2/torrents/removeCategories", data)

    def addTags(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # tags is the list of tags you want to add to passed torrents
        tags: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-torrent-tags
        data = {k: v for k, v in [["hashes", hashes], ["tags", tags]] if v}
        return self.post("/api/v2/torrents/addTags", data)

    def removeTags(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # tags is the list of tags you want to remove from passed torrents. Empty list removes all tags from relevant torrents
        tags: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-torrent-tags
        data = {k: v for k, v in [["hashes", hashes], ["tags", tags]] if v}
        return self.post("/api/v2/torrents/removeTags", data)

    def tags(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-tags
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/torrents/tags", data)

    def createTags(
        self,
        # tags is a list of tags you want to create. Can contain multiple tags separated by ,
        tags: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#create-tags
        data = {k: v for k, v in [["tags", tags]] if v}
        return self.post("/api/v2/torrents/createTags", data)

    def deleteTags(
        self,
        # tags is a list of tags you want to create. Can contain multiple tags separated by ,
        tags: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-tags
        data = {k: v for k, v in [["tags", tags]] if v}
        return self.post("/api/v2/torrents/deleteTags", data)

    def setAutoManagement(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # enable is a boolean, affects the torrents listed in hashes, default is false
        enable: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-automatic-torrent-management
        data = {k: v for k, v in [["hashes", hashes], ["enable", enable]] if v}
        return self.post("/api/v2/torrents/setAutoManagement", data)

    def toggleSequentialDownload(
        self,
        # The hashes of the torrents you want to toggle sequential download for.  hashes  can contain multiple hashes separated by  | , to toggle sequential download for multiple torrents, or set to  all , to toggle sequential download for all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#toggle-sequential-download
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/toggleSequentialDownload", data)

    def toggleFirstLastPiecePrio(
        self,
        # The hashes of the torrents you want to toggle the first/last piece priority for.  hashes  can contain multiple hashes separated by  | , to toggle the first/last piece priority for multiple torrents, or set to  all , to toggle the first/last piece priority for all torrents.
        hashes: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-first/last-piece-priority
        data = {k: v for k, v in [["hashes", hashes]] if v}
        return self.post("/api/v2/torrents/toggleFirstLastPiecePrio", data)

    def setForceStart(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # value is a boolean, affects the torrents listed in hashes, default is false
        value: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-force-start
        data = {k: v for k, v in [["hashes", hashes], ["value", value]] if v}
        return self.post("/api/v2/torrents/setForceStart", data)

    def setSuperSeeding(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # value is a boolean, affects the torrents listed in hashes, default is false
        value: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-super-seeding
        data = {k: v for k, v in [["hashes", hashes], ["value", value]] if v}
        return self.post("/api/v2/torrents/setSuperSeeding", data)

    def renameFile(
        self,
        # The hash of the torrent
        hash: str = None,
        # The old path of the torrent
        oldPath: str = None,
        # The new path to use for the file
        newPath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-file
        data = {k: v for k, v in [["hash", hash], ["oldPath", oldPath], ["newPath", newPath]] if v}
        return self.post("/api/v2/torrents/renameFile", data)

    def renameFolder(
        self,
        # The hash of the torrent
        hash: str = None,
        # The old path of the torrent
        oldPath: str = None,
        # The new path to use for the file
        newPath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-folder
        data = {k: v for k, v in [["hash", hash], ["oldPath", oldPath], ["newPath", newPath]] if v}
        return self.post("/api/v2/torrents/renameFolder", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rss-(experimental)
class RSS_experimental:
    def addFolder(
        self,
        # Full path of added folder (e.g. "The Pirate Bay\Top100")
        path: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-folder
        data = {k: v for k, v in [["path", path]] if v}
        return self.post("/api/v2/rss/addFolder", data)

    def addFeed(
        self,
        # URL of RSS feed (e.g. " http://thepiratebay.org/rss//top100/200 ")
        url: str = None,
        # Full path of added folder (e.g. "The Pirate Bay\Top100\Video")
        path: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-feed
        data = {k: v for k, v in [["url", url], ["path", path]] if v}
        return self.post("/api/v2/rss/addFeed", data)

    def removeItem(
        self,
        # Full path of removed item (e.g. "The Pirate Bay\Top100")
        path: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-item
        data = {k: v for k, v in [["path", path]] if v}
        return self.post("/api/v2/rss/removeItem", data)

    def moveItem(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None,
        # New full path of item (e.g. "The Pirate Bay")
        destPath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#move-item
        data = {k: v for k, v in [["itemPath", itemPath], ["destPath", destPath]] if v}
        return self.post("/api/v2/rss/moveItem", data)

    def items(
        self,
        # True if you need current feed articles
        withData: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-items
        data = {k: v for k, v in [["withData", withData]] if v}
        return self.post("/api/v2/rss/items", data)

    def articleId(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None,
        # ID of article
        articleId: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#mark-as-read
        data = {k: v for k, v in [["itemPath", itemPath], ["articleId", articleId]] if v}
        return self.post("/api/v2/rss/articleId", data)

    def refreshItem(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#refresh-item
        data = {k: v for k, v in [["itemPath", itemPath]] if v}
        return self.post("/api/v2/rss/refreshItem", data)

    def setRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None,
        # JSON encoded rule definition
        ruleDef: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-auto-downloading-rule
        data = {k: v for k, v in [["ruleName", ruleName], ["ruleDef", ruleDef]] if v}
        return self.post("/api/v2/rss/setRule", data)

    def renameRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None,
        # New rule name (e.g. "The Punisher")
        newRuleName: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-auto-downloading-rule
        data = {k: v for k, v in [["ruleName", ruleName], ["newRuleName", newRuleName]] if v}
        return self.post("/api/v2/rss/renameRule", data)

    def removeRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-auto-downloading-rule
        data = {k: v for k, v in [["ruleName", ruleName]] if v}
        return self.post("/api/v2/rss/removeRule", data)

    def rules(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-auto-downloading-rules
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/rss/rules", data)

    def matchingArticles(
        self,
        # Rule name (e.g. "Linux")
        ruleName: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-articles-matching-a-rule
        data = {k: v for k, v in [["ruleName", ruleName]] if v}
        return self.post("/api/v2/rss/matchingArticles", data)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#search
class Search:
    def start(
        self,
        # Pattern to search for (e.g. "Ubuntu 18.04")
        pattern: str = None,
        # Plugins to use for searching (e.g. "legittorrents"). Supports multiple plugins separated by  | . Also supports  all  and  enabled \n
        plugins: str = None,
        # Categories to limit your search to (e.g. "legittorrents"). Available categories depend on the specified  plugins . Also supports  all \n
        category: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#start-search
        data = {k: v for k, v in [["pattern", pattern], ["plugins", plugins], ["category", category]] if v}
        return self.post("/api/v2/search/start", data)

    def stop(
        self,
        # ID of the search job
        id: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#stop-search
        data = {k: v for k, v in [["id", id]] if v}
        return self.post("/api/v2/search/stop", data)

    def status(
        self,
        # ID of the search job. If not specified, all search jobs are returned
        id: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-status
        data = {k: v for k, v in [["id", id]] if v}
        return self.post("/api/v2/search/status", data)

    def results(
        self,
        # ID of the search job
        id: int = None,
        # max number of results to return. 0 or negative means no limit
        limit: int = None,
        # result to start at. A negative number means count backwards (e.g.  -2  returns the 2 most recent results)
        offset: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-results
        data = {k: v for k, v in [["id", id], ["limit", limit], ["offset", offset]] if v}
        return self.post("/api/v2/search/results", data)

    def delete(
        self,
        # ID of the search job
        id: int = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-search
        data = {k: v for k, v in [["id", id]] if v}
        return self.post("/api/v2/search/delete", data)

    def plugins(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-plugins
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/search/plugins", data)

    def installPlugin(
        self,
        # Url or file path of the plugin to install (e.g. " https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/legittorrents.py "). Supports multiple sources separated by  | \n
        sources: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#install-search-plugin
        data = {k: v for k, v in [["sources", sources]] if v}
        return self.post("/api/v2/search/installPlugin", data)

    def uninstallPlugin(
        self,
        # Name of the plugin to uninstall (e.g. "legittorrents"). Supports multiple names separated by  | \n
        names: str = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#uninstall-search-plugin
        data = {k: v for k, v in [["names", names]] if v}
        return self.post("/api/v2/search/uninstallPlugin", data)

    def enablePlugin(
        self,
        # Name of the plugin to enable/disable (e.g. "legittorrents"). Supports multiple names separated by  | \n
        names: str = None,
        # Whether the plugins should be enabled
        enable: bool = None
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#enable-search-plugin
        data = {k: v for k, v in [["names", names], ["enable", enable]] if v}
        return self.post("/api/v2/search/enablePlugin", data)

    def updatePlugins(
        self
    ):
        # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#update-search-plugins
        data = {k: v for k, v in [] if v}
        return self.post("/api/v2/search/updatePlugins", data)

    def post(self, *args, **kwargs):
        ...
