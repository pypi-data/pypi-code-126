import json

from faas.system import NodeState
from faas.util.constant import zone_label
from galileodb import NodeInfo

from galileofaas.system.core import KubernetesFunctionNode


def map_node_info_to_node(nodeinfo: NodeInfo) -> KubernetesFunctionNode:
    """
    :param nodeinfo: This implementation relies on that the NodeInfo is retrieved from Redis and was created by telemd.
    :return: a node
    """
    name = nodeinfo.node
    arch = nodeinfo.data['arch']
    cpus = int(nodeinfo.data['cpus'])
    ram = int(nodeinfo.data['ram'])
    boot = int(nodeinfo.data['boot'])
    disk = nodeinfo.data['disk'].split(' ')
    net = nodeinfo.data['net'].split(' ')
    netspeed = nodeinfo.data['netspeed']
    labels = json.loads(nodeinfo.data['labels'])
    zone = labels.get(zone_label, None)
    allocatable = json.loads(nodeinfo.data['allocatable'])
    cpu = allocatable.get('cpu', None)
    if cpu is not None:
        # FIXME what about situations when cpu == 2?
        if cpu == '1':
            allocatable['cpu'] = '1000m'

    return KubernetesFunctionNode(
        name,
        arch,
        cpus,
        ram,
        netspeed,
        labels,
        zone,
        allocatable,
        cluster=zone,
        boot=boot,
        disk=disk,
        net=net,
        state=NodeState.READY
    )
