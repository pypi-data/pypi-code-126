import hou
from ciohoudini import software

from ciocore.package_environment import PackageEnvironment

def resolve_payload(node):
    """Resolve the environment section of the payload for the given node.
    
    We build the environment from the following sources: 
    
    1. Packages. These environment entries are assumed to be valid (no append/exclusive mixing). 
    
    2. Extra env vars. These environment entries may be invalid. The user may have tried to append a
       value to a pre-existing exclusive variable. If so, we don't raise an error, we just disallow
       it and switch to the valid merge policy.
    """
    pkg_env =  PackageEnvironment()

    for package in software.packages_in_use(node):
        pkg_env.extend(package)

    extra_env = get_extra_env(node)
    for i, entry in enumerate(extra_env):
        policy = entry["merge_policy"]
        index = i+1
        try:
            pkg_env.extend([entry])
        except ValueError:
            excl_parm = node.parm("env_excl_{}".format(index))
            excl_parm.set(not excl_parm.eval())
            entry["merge_policy"] = ["append", "exclusive"][excl_parm.eval()]
            pkg_env.extend([entry])

    return {"environment":dict(pkg_env)}

def get_extra_env(node):
    """Get a list of extra env vars from the UI.

    The items also have a merge_policy flag, which is used
    in compiling the final environment that will be sent to
    Conductor.
    """
    num = node.parm("environment_kv_pairs").eval()
    result = []
    for i in range(1, num + 1):
        is_exclusive = node.parm("env_excl_{:d}".format(i)).eval()
        name = node.parm("env_key_{:d}".format(i)).eval()
        value = node.parm("env_value_{:d}".format(i)).eval()
        if name and value:
            result.append({
                "name": node.parm("env_key_{:d}".format(i)).eval(),
                "value": node.parm("env_value_{:d}".format(i)).eval(),
                "merge_policy": ["append", "exclusive"][is_exclusive]
            })
    return result

def add_variable(node, **kwargs):
    """Add a new variable to the UI.
    
    This is called by the UI when the user clicks the Add Variable button.
    """
    num_exist = node.parm("environment_kv_pairs").eval()
    node.parm("environment_kv_pairs").set(num_exist+1)


def remove_variable(node, index ):
    """Remove a variable from the UI.
    
    Remove the entry at the given index and shift all subsequent entries down.
    """
    curr_count =  node.parm("environment_kv_pairs").eval()
    for i in range(index+1, curr_count+1):
        for parm_name in ["key", "value", "excl"]:
            from_parm = node.parm("env_{}_{}".format(parm_name, i))
            to_parm = node.parm("env_{}_{}".format(parm_name, i-1))
            try:
                to_parm.set(from_parm.rawValue())
            except TypeError:
                  to_parm.set(from_parm.evalAsInt())
    node.parm("environment_kv_pairs").set(curr_count-1)
