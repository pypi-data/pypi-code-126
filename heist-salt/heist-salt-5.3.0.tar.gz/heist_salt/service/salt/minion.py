import os
import tempfile
import textwrap


async def apply_service_config(
    hub,
    tunnel_plugin,
    target_name,
    run_dir,
    service_plugin=None,
    target_os="linux",
):
    if not service_plugin:
        service_plugin = hub.service.init.get_service_plugin()

    await getattr(hub, f"service.salt.minion.{service_plugin}_conf")(
        tunnel_plugin,
        target_name,
        run_dir,
        target_os=target_os,
    )


async def systemd_conf(hub, tunnel_plugin, target_name, run_dir, target_os="linux"):
    binary_path = hub.tool.artifacts.get_salt_path(run_dir, target_os=target_os)
    if not hub.tool.path.clean_path(
        hub.heist.init.default(target_os, "run_dir_root"), run_dir
    ):
        hub.log.error(f"The {run_dir} directory is not valid")
        return False
    contents = textwrap.dedent(
        """\
                [Unit]
                Description=The Salt Minion
                Documentation=man:salt-minion(1) file:///usr/share/doc/salt/html/contents.html https://docs.saltproject.io/en/latest/contents.html
                After=network.target salt-master.service

                [Service]
                KillMode=process
                Type=notify
                NotifyAccess=all
                LimitNOFILE=8192
                ExecStart={binary_path} minion --config-dir {conf} --pid-file={pfile}

                [Install]
                WantedBy=multi-user.target
                """
    )
    _, path = tempfile.mkstemp()
    with open(path, "w+") as wfp:
        wfp.write(
            contents.format(
                binary_path=binary_path,
                conf=hub.tool.path.path_convert("linux", run_dir, ["root_dir", "conf"]),
                pfile=hub.tool.path.path_convert("linux", run_dir, ["pfile"]),
            )
        )
    await hub.tunnel[tunnel_plugin].send(
        target_name,
        path,
        hub.service.init.service_conf_path("salt-minion", "systemd"),
    )

    await hub.tunnel[tunnel_plugin].cmd(target_name, f"systemctl daemon-reload")


async def raw_conf(hub, tunnel_plugin, target_name, run_dir, target_os="linux"):
    pass


async def win_service_conf(
    hub, tunnel_plugin, target_name, run_dir, target_os="windows"
):
    """
    Install the salt-minion service on Windows using SSM.exe.

    Args:
        tunnel_plugin (str): The tunnel plugin to use
        target_name (str): The name of the target
        run_dir (str): The location of the run_dir
        target_os (str): The target operating system
    """
    if not hub.tool.path.clean_path(
        hub.heist.init.default(target_os, "run_dir_root"), run_dir
    ):
        hub.log.error(f"The {run_dir} directory is not valid")
        return False
    # ssm commands
    binary_path = hub.tool.artifacts.get_salt_path(run_dir, target_os=target_os)
    if hub.OPT.heist.onedir:
        ssm_bin = run_dir / "salt" / "ssm.exe"
    else:
        ssm_bin = run_dir / "ssm.exe"
    await hub.tunnel[tunnel_plugin].cmd(
        target_name,
        f"{ssm_bin} install salt-minion {binary_path} minion "
        f'-c "{run_dir / "root_dir" / "conf"}"',
    )
    await hub.tunnel[tunnel_plugin].cmd(
        target_name, f"{ssm_bin} set salt-minion Description Heist Salt Minion"
    )
    await hub.tunnel[tunnel_plugin].cmd(
        target_name, f"{ssm_bin} set salt-minion Start SERVICE_AUTO_START"
    )
    await hub.tunnel[tunnel_plugin].cmd(
        target_name, f"{ssm_bin} set salt-minion AppStopMethodConsole 24000"
    )
    await hub.tunnel[tunnel_plugin].cmd(
        target_name, f"{ssm_bin} set salt-minion AppStopMethodWindow 2000"
    )
    await hub.tunnel[tunnel_plugin].cmd(
        target_name, f"{ssm_bin} set salt-minion AppStartDelay 60000"
    )


async def start(
    hub, target_name, tunnel_plugin, service_plugin, run_dir=None, target_os="linux"
):
    await hub.service.salt.minion.apply_service_config(
        tunnel_plugin,
        target_name,
        run_dir,
        service_plugin,
        target_os=target_os,
    )

    # run_cmd is used for the raw service
    run_cmd = (
        str(hub.tool.artifacts.get_salt_path(run_dir, target_os=target_os))
        + f" {hub.tool.service.get_service_name(service_plugin)}"
        + f" -c {run_dir / 'root_dir' / 'conf'}"
    )
    await hub.service[service_plugin].start(
        tunnel_plugin,
        target_name,
        "salt-minion",
        run_cmd=run_cmd,
        block=False,
        target_os=target_os,
    )

    await hub.service[service_plugin].enable(tunnel_plugin, target_name, "salt-minion")
