import logging
import os
import threading
from typing import Optional

from faas.context.platform.network.api import NetworkService
from faas.context.platform.network.inmemory import InMemoryNetworkService
from faas.context.platform.zone.inmemory import StaticZoneService
from galileofaas.context.platform.deployments.rds import PodExtractedDeploymentService
from galileofaas.context.platform.nodes.rds import TelemcNodeService
from galileofaas.context.platform.pod.rds import RedisPodService
from galileofaas.context.platform.traces.rds import RedisTraceService
from telemc import TelemetryController

from galileofaas.connections import RedisClient
from galileofaas.context.model import GalileoFaasContext
from galileofaas.context.platform.telemetry.rds import RedisTelemetryService

logger = logging.getLogger(__name__)


class DefaultGalileoContextDaemon:
    # TODO inject context and start the services
    def __init__(self, fn_pattern: str, network_service: NetworkService = None):
        """

        :param fn_pattern: tells the services which Pods and Deployments should be considered (i.e., if you
        deploy a Deployment called 'nginx-deployment' and another one called 'nginx-function', while passing '-function'
        as the pattern. Only the pods belonging to 'nginx-function' will be considered as deployment
        """
        self.fn_pattern = fn_pattern
        self.t = None
        self._context = None
        self.rds = None
        self.pod_service = None
        self.deployment_service = None
        self.telemc = None
        self.node_service = None
        self.trace_service = None
        self.telemetry_service = None
        self.zone_service = None
        self.network_service = network_service

    def run(self):
        logging.basicConfig(level=logging._nameToLevel[os.environ.get('galileo_context_logging', 'DEBUG')])

        self.rds = RedisClient.from_env()
        self.zone_service = StaticZoneService(['zone-a', 'zone-b', 'zone-c'])
        self.telemc = TelemetryController(self.rds.conn())
        self.node_service = TelemcNodeService(self.telemc)
        self.pod_service = RedisPodService(self.rds, self.node_service)
        self.deployment_service = PodExtractedDeploymentService(self.pod_service, self.fn_pattern)
        telemetry_window_size = int(os.environ.get('galileo_context_telemetry_window_size', 60))
        traces_window_size = int(os.environ.get('galileo_context_trace_window_size', 60))
        self.telemetry_service = RedisTelemetryService(telemetry_window_size, self.rds, self.node_service)
        if self.network_service is None:
            self.network_service = InMemoryNetworkService.from_env()
        self.trace_service = RedisTraceService(traces_window_size, self.rds, self.pod_service, self.node_service,
                                               self.network_service)
        self._context = GalileoFaasContext(
            pod_service=self.pod_service,
            telemetry_service=self.telemetry_service,
            deployment_service=self.deployment_service,
            node_service=self.node_service,
            trace_service=self.trace_service,
            telemc=self.telemc,
            zone_service=self.zone_service,
            network_service=self.network_service,
            rds=self.rds,
        )

        self.telemetry_service.start()
        self.trace_service.start()
        self.pod_service.start()

    @property
    def context(self) -> Optional[GalileoFaasContext]:
        return self._context

    def start(self):
        self.t = threading.Thread(target=self.run)
        self.t.start()

    def stop(self):
        if self.t is not None:
            self.t.join()
