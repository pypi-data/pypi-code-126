from grdpcli import *

def command_update():
    print("[GRDPCLI]: Updating GRDPCLI config")
    os.remove(os.path.join(GRDPCLI_HOME_DIR, GRDPCLI_CONFIG_JSON))
    os.remove(os.path.join(GRDPCLI_HOME_DIR, GRDPCLI_PROJECT_JSON))
    input("[GRDPCLI]: Authorization is required, please ENTER to open up the browser to login or CTRL+C to cancel:")
    WEBSERVER = HTTPServer((hostName, serverPort), callbackServer)
    webbrowser.open(AUTH_ADDRESS, new=0, autoraise=True)
    print("[GRDPCLI]: Waiting for authorization is compleate ...")
    try:
        WEBSERVER.serve_forever()
    except KeyboardInterrupt:
        pass

def command_projects():
    from prettytable import PrettyTable
    IDS_LIST = []
    t = PrettyTable(['ID', 'Project Name'])
    projects = getProjectsJson()
    for id in projects:
        for key in projects[id].keys():
            name = list(projects[id].keys())[0]
            if key == 'status':
                name = list(projects[id].keys())[1]
            IDS_LIST.append(id)
            t.add_row([id,name])
            break
    active_project_id = getGRCPcliConfig()['active_project']
    active_project_id = None if active_project_id == 'None' else active_project_id

    print(t)
    while True:
        id = input("[GRDPCLI]: Please provide id of your project, current active project is `{}: {}`: ".format(active_project_id, getProjectName(active_project_id)))

        if active_project_id and id == '':
            id = getGRCPcliConfig()['active_project']
            break

        if id not in IDS_LIST:
            print("[GRDPCLI]: Project id is incorrect, please provide correct value")
        else:
            setActiveProject(id)
            break
    print("[GRDPCLI]: Current active project is `{}`".format(getProjectName(id)))
    generateKubectlConfig()

def commandHandler(commands):
    SUBCOMMANDS = ['update','projects']
    if len(commands) > 1:
        if commands[1] in SUBCOMMANDS:
            if commands[1] == 'update':
                command_update()
            if commands[1] == 'help':
                command_help()
            if commands[1] == 'projects':
                command_projects()
        else:
            del commands[0]
            options = " ".join(commands)

            active_project_id = getGRCPcliConfig()['active_project']
            active_project_id = None if active_project_id == 'None' else active_project_id

            if not active_project_id:
                command_projects()

            context = getNamespaceName(getGRCPcliConfig()['active_project'])
            exit(os.WEXITSTATUS(os.system('KUBECONFIG={} kubectl --context {} {}'.format(KUBECTL_CONFIG, context, options))))
    else:
        command_projects()
