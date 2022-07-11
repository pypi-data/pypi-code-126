import json
import logging
import threading
import time
from typing import Dict, Optional

import pandas as pd
from faas.context import TraceService, InMemoryTraceService, NetworkService, NodeService, ResponseRepresentation
from faas.util.constant import client_role_label
from galileodb.recorder.traces import TracesSubscriber

from galileofaas.connections import RedisClient
from galileofaas.context.platform.replica.k8s import KubernetesFunctionReplicaService
from galileofaas.system.core import GalileoFunctionResponse, KubernetesFunctionNode
from galileofaas.util.network import update_latencies

logger = logging.getLogger(__name__)


class RedisTraceService(TraceService):

    def __init__(self, inmemory_trace_service: InMemoryTraceService, window_size: int, rds_client: RedisClient,
                 replica_service: KubernetesFunctionReplicaService,
                 node_service: NodeService[KubernetesFunctionNode],
                 network_service: NetworkService):
        self.window_size = window_size
        self.rds_client = rds_client
        self.traces_subscriber = TracesSubscriber(rds_client.conn())
        self.replica_service: KubernetesFunctionReplicaService = replica_service
        self.node_service = node_service
        self.network_service = network_service
        self.inmemory_trace_service = inmemory_trace_service
        self.t = None

    def get_traces_for_function(self, function_name: str, start: float, end: float, zone: str = None,
                                response_status: int = None):
        now = time.time()
        return self.inmemory_trace_service.get_traces_for_function(function_name, now - self.window_size, now, zone,
                                                                   response_status)

    def get_traces_for_function_image(self, function: str, function_image: str, start: float, end: float,
                                      zone: str = None,
                                      response_status: int = None):
        now = time.time()
        return self.inmemory_trace_service.get_traces_for_function_image(function, function_image,
                                                                         now - self.window_size, now, zone,
                                                                         response_status)

    @staticmethod
    def parse_request(req: GalileoFunctionResponse) -> Optional[ResponseRepresentation]:
        sent = req.trace.sent
        done = req.trace.done
        rtt = done - sent
        headers = json.loads(req.trace.headers)
        start_ = headers.get('X-Start', None)
        if start_ is None:
            return None
        start = float(start_)
        end = float(headers['X-End'])

        return ResponseRepresentation(
            ts=done,
            function=req.replica.function.name,
            function_image=req.replica.container.fn_image.image,
            replica_id=req.replica.replica_id,
            node=req.replica.node.name,
            rtt=rtt,
            done=done,
            sent=sent,
            origin_zone=req.origin_zone,
            dest_zone=req.destination_zone,
            client=req.client,
            status=req.trace.status,
            network_latency=((start - sent) + (done - end)) * 1000
        )

    def get_traces_api_gateway(self, node_name: str, start: float, end: float,
                               response_status: int = None) -> pd.DataFrame:
        now = time.time()
        return self.inmemory_trace_service.get_traces_api_gateway(node_name, now - self.window_size, now,
                                                                  response_status)

    def find_node_for_client(self, client: str) -> Optional[KubernetesFunctionNode]:
        """
        :param pods: contains 'name', and 'nodeName'
        """
        for replica in self.replica_service.find_function_replicas_with_labels(node_labels={client_role_label: "true"}):
            if replica.pod_name in client:
                node = self.node_service.find(replica.node_name)
                return node
        return None

    def run(self):
        for trace in self.traces_subscriber.run():
            # logger.debug("Got trace %s", trace)
            if trace.status == -1:
                logger.info("Failed trace received!")
                continue
            headers = json.loads(trace.headers)
            final_host = headers.get('X-Final-Host', '').split(',')[-1].split(':')[0].replace(' ', '')
            pod = self.replica_service.get_function_replica_with_ip(final_host, running=False)
            if pod is None:
                logger.warning(f"Looked up non-existent pod ip {final_host}")
                continue
            node = self.node_service.find(pod.node_name)
            client_node = self.find_node_for_client(trace.client)
            self.update_latencies(client_node.name, trace.sent, headers)
            if node is None:
                logger.error("GalileoFaasNode was None when looking for the serving pod %s", pod.node_name)
                logger.debug("all nodes stored currently %s", str([x.name for x in self.node_service.get_nodes()]))
                continue
            pod_request_trace = GalileoFunctionResponse(pod, trace, node)
            self.add_trace(pod_request_trace)

    def add_trace(self, response: GalileoFunctionResponse):
        self.inmemory_trace_service.add_trace(response)

    def start(self):
        logger.info('Start RedisTraceService subscription thread')
        self.t = threading.Thread(target=self.run)
        self.t.start()
        return self.t

    def stop(self, timeout: float = 5):
        self.traces_subscriber.close()
        if self.t is not None:
            self.t.join(timeout)
        logger.info('Stopped RedisTraceService subscription thread')

    def update_latencies(self, client_node: str, sent: float, headers: Dict[str, str]):
        """
        Updates the latencies based on the data in headers.
        First reads X-Forwarded-For to get all nodes in the request trace, and then updates the latency between each node.
        Starting with the client-gateway connection.
        """

        updates = update_latencies(client_node, sent, headers, self.replica_service)
        for nodes, latency in updates.items():
            self.network_service.update_latency(nodes[0], nodes[1], latency)
