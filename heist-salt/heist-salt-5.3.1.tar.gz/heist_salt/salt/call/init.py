import json


async def get_grains(hub, target_name, tunnel_plugin, run_dir, target_os="linux"):
    """
    Run grains.items and return the grains as a dictionary.
    """
    binary_path = hub.tool.artifacts.get_salt_path(run_dir, target_os=target_os)
    grains = await hub.tunnel[tunnel_plugin].cmd(
        target_name,
        f"{binary_path} call --config-dir {run_dir / 'root_dir' / 'conf'} "
        f"--local grains.items --out json",
        target_os=target_os,
    )
    _, sep, grains = grains.stdout.partition("{")
    grains = sep + grains
    return json.loads(grains)["local"]


async def get_id(hub, target_name, tunnel_plugin, run_dir, target_os="linux"):
    binary_path = run_dir / "salt"
    return await hub.tunnel[tunnel_plugin].cmd(
        target_name,
        f"{binary_path} call --config-dir {run_dir} --local grains.get id",
        target_os=target_os,
    )
