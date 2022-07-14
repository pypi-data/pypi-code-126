import re

# Simple loose email regex, matches 1 email address.
SIMPLE_EMAIL_RE = re.compile(r"^\S+@\S+$")

def resolve_payload(node, **kwargs):
    """
    Resolve the notifications field for the payload.
    """
    result = {}
    addresses = resolve_email_addresses(node)
    if addresses:
        result["notify"] = addresses
    location = resolve_location(node)
    if location:
        result["location"] = location

    result["local_upload"] = not node.parm("use_daemon").eval()
    return result
 

def resolve_email_addresses(node):
    """
    Resolve the notifications field for the payload.
    """
    if not node.parm("do_email").eval():
        return []

    addresses = node.parm("email_addresses").eval() or ""
    addresses = [a.strip() for a in re.split(', ', addresses) if a and SIMPLE_EMAIL_RE.match(a)]
    return addresses

def resolve_location(node):
    """
    Resolve the location field for the payload.
    """
    location = node.parm("location_tag").eval()

    return location
