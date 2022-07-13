def get_service_name(hub, service_plugin):
    """
    Get the service name for the given service
    """
    service_name = None
    if service_plugin in ["systemd", "win_service"]:
        service_name = "salt-minion"
    elif service_plugin == "raw":
        service_name = "minion"
    return service_name
