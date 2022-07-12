_M='--merge'
_L='--version'
_K='--local'
_J='Comma-delimited list of services to push in the pods. It pushes all, if not specified'
_I='--message'
_H='--services'
_G='[red]Error:[/red] Input the services as a comma-delimited list'
_F='name'
_E='Name of the cloud pod'
_D=True
_C='--name'
_B='-n'
_A=False
import sys,traceback
from typing import Dict,List,Optional,Set
import click
from click import Context
from localstack.cli import console
from localstack.utils.analytics.cli import publish_invocation
from localstack_ext.bootstrap.pods.utils.common import is_comma_delimited_list
from localstack_ext.cli.click_utils import clean_command_dict,command_require_at_least_open_option,print_pods,required_if_not_cached
from localstack_ext.cli.tree_view import TreeRenderer
class PodsCmdHandler(click.Group):
	def invoke(self,ctx):
		try:return super(PodsCmdHandler,self).invoke(ctx)
		except Exception as exc:
			if isinstance(exc,click.exceptions.Exit):raise
			click.echo(f"Error: {exc}")
			if ctx.parent and ctx.parent.params.get('debug'):click.echo(traceback.format_exc())
			ctx.exit(1)
def _cloud_pod_initialized(pod_name):
	from localstack_ext.bootstrap import pods_client
	if not pods_client.is_initialized(pod_name=pod_name):console.print(f"[red]Error:[/red] Could not find local CloudPods instance '{pod_name}'");return _A
	return _D
@click.group(name='pod',help='Manage the state of your instance via local Cloud Pods',cls=PodsCmdHandler)
def pod():
	from localstack_ext.bootstrap.licensing import is_logged_in
	if not is_logged_in():console.print('[red]Error:[/red] not logged in, please log in first');sys.exit(1)
@pod.command(name='config',help='Configure a set of parameters to be used in all Cloud Pods commands',cls=command_require_at_least_open_option())
@click.option(_B,_C,help='Name of the cloud pod to set in the context')
@click.option('-s',_H,help='Comma-delimited list of services or `all` to enable all the services')
@publish_invocation
def cmd_pod_config(name,services):
	from localstack_ext.bootstrap import pods_client
	if services and not is_comma_delimited_list(services):console.print(_G);return _A
	options=clean_command_dict(options=dict(locals()),keys_to_drop=['pods_client']);pods_client.save_pods_config(options=options)
@pod.command(name='delete',help='Deletes the specified cloud pod. By default only locally')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-r','--remote',help='Whether the Pod should also be deleted remotely.',is_flag=_D,default=_A)
@publish_invocation
def cmd_pod_delete(name,remote):
	from localstack_ext.bootstrap import pods_client;result=pods_client.delete_pod(pod_name=name,remote=remote)
	if result:console.print(f"Successfully deleted {name}")
	else:console.print(f"[yellow]{name} not available locally[/yellow]")
@pod.command(name='commit',help='Commits the current expansion point and creates a new (empty) revision')
@click.option('-m',_I,help='Add a comment describing the revision')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-s',_H,help=_J)
@publish_invocation
def cmd_pod_commit(message,name,services):
	from localstack_ext.bootstrap import pods_client
	if services and not is_comma_delimited_list(services):console.print(_G);return _A
	service_list=[x.strip()for x in services.split(',')]if services else None;pods_client.commit_state(pod_name=name,message=message,services=service_list);console.print('Successfully committed the current state')
@pod.command(name='push',help='Creates a new version of a pod from the latest commit (if existing)')
@click.option(_K,'-l',default=_A,is_flag=_D,help='Keeps the pod local (does not upload it to the platform)')
@click.option('-m',_I,help='Add a comment describing the version')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-s',_H,help=_J)
@click.option('--overwrite',help='Overwrites a version with the content from the latest commit of the currently selected version',type=bool,default=_A)
@click.option('-v',_L,help='Version to overwrite. To set only together with --overwrite',type=int)
@publish_invocation
def cmd_pod_push(message,name,local,services,overwrite,version):
	from localstack_ext.bootstrap import pods_client
	if services and not is_comma_delimited_list(services):console.print(_G);return _A
	service_list=[x.strip()for x in services.split(',')]if services else None
	if overwrite:
		result=pods_client.push_overwrite(version=version,pod_name=name,comment=message,services=service_list)
		if result:console.print('Successfully overwritten state of version ')
		return
	result=pods_client.push_state(pod_name=name,comment=message,register=not local,services=service_list);console.print('Successfully pushed the current state')
	if not local:
		if result:console.print(f"Successfully registered {name} with remote!")
		else:console.print(f"[red]Error:[/red] Pod with name {name} is already registered")
@pod.command(name='inject',help='Injects the state from a locally available version into the application runtime')
@click.option(_M,is_flag=_D,default=_A,help='For each service in the application state, its backend is merged with the backend specified by the given pod and version, or added if missing.')
@click.option('-v',_L,default='-1',type=int,help='Loads the state of the specified version - Most recent one by default')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@publish_invocation
def cmd_pod_inject(merge,version,name):
	from localstack_ext.bootstrap import pods_client
	if not _cloud_pod_initialized(pod_name=name):return
	result=pods_client.inject_state(pod_name=name,version=version,merge=merge)
	if result:console.print('[green]Successfully Injected Pod State[/green]')
	else:console.print('[red]Failed to Inject Pod State[/red]')
@click.option('--inject/--no-inject',default=_D,help='Whether the latest version of the pulled pod should be injected')
@click.option(_M,is_flag=_D,default=_A,help='When injecting a pod version, it merges its state with the one of the locally running application')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@pod.command(name='pull',help='Incorporates the change from a  into the application runtime')
@publish_invocation
def cmd_pod_pull(name,inject,merge):from localstack_ext.bootstrap import pods_client;pods_client.pull_state(pod_name=name,inject=inject,merge=merge)
@pod.command(name='list',help='Lists all available pods')
@click.option(_K,'-l',help='Only lists locally available pods',is_flag=_D,default=_A)
@publish_invocation
def cmd_pod_list_pods(local):
	from localstack_ext.bootstrap import pods_client;pods=pods_client.list_pods(local=local)
	if not pods:console.print(f"[yellow]No pods available {'locally'if local else''}[/yellow]")
	print_pods(pods)
@pod.command(name='versions',help='Lists all available version numbers')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@publish_invocation
def cmd_pod_versions(name):
	from localstack_ext.bootstrap import pods_client
	if not _cloud_pod_initialized(pod_name=name):return
	version_list=pods_client.get_version_summaries(pod_name=name);result='\n'.join(version_list);console.print(result)
@pod.command(name='inspect',help='Inspect the contents of a pod')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-f','--format',help='Format (curses, rich, json)',default='curses')
@publish_invocation
def cmd_pod_inspect(name,format):
	from localstack_ext.bootstrap import pods_client
	if not _cloud_pod_initialized(pod_name=name):return
	result=pods_client.get_version_metamodel(pod_name=name,version=-1);skipped_services=['cloudwatch']
	for (account,details) in result.items():result[account]={k:v for(k,v)in details.items()if k not in skipped_services}
	TreeRenderer.get(format).render_tree(result)