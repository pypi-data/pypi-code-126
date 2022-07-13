import asyncio
import pathlib

import salt.config


def accept_minion(hub, minion: str) -> bool:
    return hub.salt.key[hub.OPT.heist.key_plugin].accept_minion(minion)


def delete_minion(hub, minion: str) -> bool:
    return hub.salt.key[hub.OPT.heist.key_plugin].delete_minion(minion)


async def check_pki_dir_empty(
    hub, target_name, tunnel_plugin, key_dir, target_os="linux"
):
    """
    function to check if the pki directory is empty or not
    """
    if target_os == "windows":
        # Returns 0 exitcode if empty
        check_dir = f"$items = Get-ChildItem -Path {key_dir}; exit $items.Count"
        ret = await hub.tunnel[tunnel_plugin].cmd(target_name, check_dir)
        if ret.returncode != 0:
            hub.log.error(
                "The minion pki directory is not empty. Not generating and accepting a key"
            )
            return False
    else:
        # Returns 0 exitcode if NOT empty
        check_dir = f'[ "$(ls -A {key_dir})" ]'
        ret = await hub.tunnel[tunnel_plugin].cmd(target_name, check_dir)
        if ret.returncode == 0:
            hub.log.error(
                "The minion pki directory is not empty. Not generating and accepting a key"
            )
            return False
    return True


async def generate_keys(
    hub,
    target_name,
    tunnel_plugin,
    run_dir,
    user=None,
    minion_id=None,
    target_os="linux",
):
    binary_path = str(hub.tool.artifacts.get_salt_path(run_dir, target_os=target_os))
    if not hub.tool.path.clean_path(
        hub.heist.init.default(target_os, "run_dir_root"), run_dir
    ):
        hub.log.error(f"The path {run_dir} is not valid")
        return False
    is_windows = target_os == "windows"

    if is_windows:
        key_dir = run_dir / "root_dir" / "conf" / "pki" / "minion"
    else:
        key_dir = run_dir / "root_dir" / "etc" / "salt" / "pki" / "minion"

    hub.log.debug(f"Create and secure pki dir and parent directores: {key_dir}")
    if target_os == "windows":
        # Owner (OW), System (SY), and Administrators (BA) have Full Control
        sddl = "D:PAI(A;OICI;FA;;;OW)(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)"
        owner = r'[System.Security.Principal.NTAccount]"BUILTIN\Administrators"'
        cmd = "; ".join(
            [
                f'New-Item -Path "{key_dir}" -Type Directory',
                f'$acl = Get-Acl "{key_dir.parent}"',
                f'$acl.SetSecurityDescriptorSddlForm("{sddl}")',
                f"$acl.SetOwner({owner})",
                f'Set-Acl -Path "{key_dir.parent}" -AclObject $acl',
            ]
        )
    else:
        # mkdir will not add the correct permissions to the parent directories
        # unless each directory is specified
        perms = 0o710 if hub.tunnel.asyncssh.CONS[target_name].get("sudo") else 0o700
        cmd = f"mkdir -m{perms:o} -p {key_dir.parent.parent.parent} {key_dir.parent.parent} {key_dir.parent} {key_dir}"

    await hub.tunnel[tunnel_plugin].cmd(target_name, cmd, target_os=target_os)

    if not is_windows and user:
        await hub.tunnel[tunnel_plugin].cmd(
            target_name,
            f"chown -R {user}:{user} {key_dir.parent.parent.parent}",
        )

    hub.log.debug("Making sure the PKI directory is empty")
    if not await hub.salt.key.init.check_pki_dir_empty(
        target_name, tunnel_plugin, key_dir, target_os=target_os
    ):
        return False

    hub.log.debug(f"Generating minion keys: {key_dir}")
    cmd = f"{binary_path} key --gen-keys=minion --gen-keys-dir={key_dir}"
    ret = await hub.tunnel[tunnel_plugin].cmd(target_name, cmd, target_os=target_os)
    if ret.returncode != 0:
        hub.log.error("Failed to generate minion keys")
        return False

    hub.log.debug("Copying minion keys to the master")
    opts = salt.config.client_config(hub.salt.key.local_master.DEFAULT_MASTER_CONFIG)
    minion_key = pathlib.Path(opts["pki_dir"]) / "minions" / minion_id

    await hub.tunnel[tunnel_plugin].get(
        target_name,
        key_dir / f"minion.pub",
        minion_key,
    )
    if not minion_key.is_file():
        hub.log.error("The minion key was not accepted")
        return False

    hub.heist.CONS[target_name].update(
        {
            "minion_id": minion_id,
        }
    )
    hub.log.info(f"Accepted minion keys for {minion_id}")
    return True


async def accept_key_master(hub, target_name, tunnel_plugin, run_dir, minion_id=None):
    """
    Accept the minions key on the salt-master
    """
    if not minion_id:
        hub.log.info("Querying minion id and attempting to accept the minion's key")
        ret = await hub.salt.call.init.get_id(target_name, tunnel_plugin, run_dir)
        if ret.returncode == 0:
            minion_id = ret.stdout.split()[1]
        else:
            hub.log.error("Could not determine the minion_id")
            return False
    retry_key_count = hub.OPT.heist.get("retry_key_count", 5)
    while retry_key_count > 0:
        if hub.salt.key.init.accept_minion(minion_id):
            break
        await asyncio.sleep(5)
        retry_key_count = retry_key_count - 1
    else:
        hub.log.error(f"Could not accept the key for the minion: {minion_id}")
        return False
    hub.heist.CONS[target_name].update(
        {
            "minion_id": minion_id,
        }
    )
    hub.log.info(f"Accepted the key for minion: {minion_id}")
    return True
