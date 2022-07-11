import re

_expressions = dict(
            url_to_parts = r"^(http[s]{0,1}|ftp)?(:\/\/)?(www\.?)?([^:\/\s]+)\.(\w+)\/?([\d\w\-\.\_\~\/]+)\??(.*)"
            )

def url_to_parts(url):
    """
    Convert a url to a tuple of (scheme, full domain, top level domain, sub directories, page, query).
    """
    groups = re.findall(_expressions['url_to_parts'],url)[0]
    
    return groups[0], groups[3], groups[4], groups[5].split('/'), groups[5].split('/')[-1], groups[6]



