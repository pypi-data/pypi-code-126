from edalize.tools.edatool import Edatool
from edalize.utils import EdaCommands

# Copyright 2019-2022 Olof Kindgren <olof.kindgren@gmail.com>
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
import lxml
import os

logging.basicConfig(level=logging.DEBUG)

import ipyxact.ipxact2014 as ipxact
from ipyxact.verilogwriter import Instance, ModulePort, Port, VerilogWriter, Wire


class IPXactLibrary(object):
    instances = {}

    ports = {}
    wires = []
    library = {}

    def __init__(self):
        self.module_ports = {}

    def set_top_component(self, vlnv):
        self.top_component = self.library[tuple(vlnv.split(":"))]

    def set_top_view(self, view_name):
        self.top_view_name = view_name

    def add_file(self, f):
        try:
            obj = ipxact.parse(f, True)
            vlnv = None
            vlnv = (obj.vendor, obj.library, obj.name, obj.version)
            if isinstance(obj, ipxact.Component):
                self.library[vlnv] = obj
                logging.debug("Adding component from " + f)
            elif isinstance(obj, ipxact.design):
                self.library[vlnv] = obj
                logging.debug("Adding design from " + f)
            elif isinstance(obj, ipxact.designConfiguration):
                self.library[vlnv] = obj
                logging.debug("Adding designConfig from " + f)
            elif isinstance(obj, ipxact.busDefinition):
                self.library[vlnv] = obj
                logging.debug("Adding busDefinition from " + f)
            elif isinstance(obj, ipxact.abstractionDefinition):
                self.library[vlnv] = obj
                logging.debug("Adding abstractionDefinition from " + f)
            else:
                logging.debug(
                    "Not adding {}. Unhandled type {}".format(f, obj.__class__.__name__)
                )

        except lxml.etree.XMLSyntaxError as e:
            logging.warning("Failed to parse {} : {}".format(f, e.msg))

    def find(self, x):
        vlnv = (x.vendor, x.library, x.name, x.version)
        return self.library[vlnv]

    def get_component_instantiation(self, component, view_name):
        view = self.get_view(component, view_name)
        comp_inst_ref = view.componentInstantiationRef

        for (
            componentInstantiation
        ) in component.model.instantiations.componentInstantiation:
            if componentInstantiation.name == comp_inst_ref:
                return componentInstantiation
        raise KeyError("FIXME: Couldn't find componentInstantiation " + comp_inst_ref)

    def get_design(self, view):
        for (
            designInstantiation
        ) in self.top_component.model.instantiations.designInstantiation:
            if designInstantiation.name == view.designInstantiationRef:
                return self.find(designInstantiation.designRef)
        raise KeyError("FIXME: Couldn't find designRef")

    def get_external_ports(self):
        return self.get_ports(self.top_component)

    def get_ports(self, component):
        module_ports = {}
        for port in component.model.ports.port:
            name = port.name
            left = 0
            right = 0

            if port.wire.Vectors:
                if len(port.wire.Vectors.Vector) > 1:
                    raise NotImplementedError("No clue how to handle multiple vectors")
                left = port.wire.Vectors.Vector[0].left.parse_uint()
                right = port.wire.Vectors.Vector[0].right.parse_uint()
            _dir = {"in": "input", "out": "output", "inout": "inout", "phantom": None}[
                port.wire.direction
            ]
            if _dir:
                module_ports[name] = ModulePort(
                    name,
                    dir=_dir,
                    width=left + 1 - right,
                    low=right,
                    asc=(right > left),
                )
        return module_ports

    def get_design_cfg(self, view):
        design_cfg_name = view.designConfigurationInstantiationRef
        for (
            designConfigurationInstantiation
        ) in self.top_component.model.instantiations.designConfigurationInstantiation:
            if designConfigurationInstantiation.name == design_cfg_name:
                return self.find(
                    designConfigurationInstantiation.designConfigurationRef
                )

        raise KeyError("FIXME design_cfg")

    def get_instances(self, view):
        if not self.instances:
            design = self.get_design(view)
            design_cfg = self.get_design_cfg(view)
            for componentInstance in design.componentInstances.componentInstance:
                instance_name = componentInstance.instanceName
                component = self.find(componentInstance.componentRef)

                # Fixme: Check instance_view_name
                for viewConfiguration in design_cfg.viewConfiguration:
                    if viewConfiguration.instanceName == instance_name:
                        instance_view_name = viewConfiguration.view.viewRef

                self.instances[instance_name] = self.add_instance(
                    component, instance_view_name, instance_name
                )

        return self.instances

    def get_view(self, component, view_name):
        for view in component.model.views.view:
            if view.name == view_name:
                return view
        raise KeyError("FIXME: Couldn't find view " + view_name)

    def add_instance(self, component, instance_view_name, instance_name):

        instantiation = self.get_component_instantiation(component, instance_view_name)
        module_name = instantiation.moduleName
        ports = []
        for name, comp_port in self.get_ports(component).items():
            port = Port(comp_port.name)
            port.direction = comp_port.dir
            port.width = comp_port.width
            ports.append(port)
            # ports.append(Port(port.name, port_value))

        instance = Instance(module_name, instance_name, [], ports)
        return instance

    # self.instances[instance_name] = component.add_instance(view_name, instance_name)

    def get_component_ref_from_instance_name(self, design, instance_name):
        for componentInstance in design.componentInstances.componentInstance:
            if componentInstance.instanceName == instance_name:
                return componentInstance
        raise KeyError("FIXME")

    def get_top_bus_interface(self, bus_name):
        return self.get_bus_interface(self.top_component, bus_name)

    def get_instance_bus_interface(self, design, instance_name, bus_name):
        component_instance = self.get_component_ref_from_instance_name(
            design, instance_name
        )
        component_ref = component_instance.componentRef
        component = self.find(component_ref)
        return self.get_bus_interface(component, bus_name)

    def get_bus_interface(self, component, bus_name):
        for busInterface in component.BusInterfaces.BusInterface:
            if busInterface.name == bus_name:
                return busInterface
        raise KeyError("No bus today")

    def get_abstraction_type(self, busInterface, view_name):
        for abstractionType in busInterface.AbstractionTypes.abstractionType:
            if not abstractionType.viewRef or view_name in [
                x.valueOf_ for x in abstractionType.viewRef
            ]:
                return abstractionType
        raise KeyError("Fail")

    def find_wire_width_in_abs_def(self, abs_def, wire_name, bus_mode):
        for port in abs_def.ports.port:
            if port.logicalName == wire_name:
                mode_info = getattr(port.wire, bus_mode)
                if mode_info.width:
                    return mode_info.width.parse_uint()
                else:
                    return 0
        raise Exception("No bus mode for " + wire_name)

    def add_interconnection(self, design, interconnection):
        ic_name = interconnection.name

        logical_ports = {}

        def _add_logical_ports(instance_name, busInterface, logical_ports):
            if hasattr(busInterface, "master"):
                bus_mode = "onMaster"
            elif hasattr(busInterface, "slave"):
                bus_mode = "onSlave"
            else:
                raise Exception("bus mode not handled")
            abstractionType = self.get_abstraction_type(
                busInterface, "rtl"
            )  # FIXME: How??
            abs_def = self.find(abstractionType.abstractionRef)
            for portMap in abstractionType.portMaps.portMap:
                log_port = portMap.logicalPort
                log_name = log_port.name
                if not log_name in logical_ports:
                    # Sanity check that logical port width is equal on all (both?) sides?
                    left = -1
                    right = 0
                    port_width = 0
                    if hasattr(log_port, "Range") and log_port.Range:
                        left = log_port.Range.left.parse_uint()
                        right = log_port.Range.right.parse_uint()
                    port_width = left + 1 - right
                    wire_width = self.find_wire_width_in_abs_def(
                        abs_def, log_name, bus_mode
                    )
                    logical_ports[log_name] = {
                        "endpoints": [],
                        "wire_width": wire_width,
                        "port_width": port_width,
                    }
                logical_ports[log_name]["endpoints"].append(
                    (instance_name, portMap.physicalPort.name)
                )

        for activeInterface in interconnection.activeInterface:
            instance_name = activeInterface.componentRef
            bus_name = activeInterface.busRef
            busInterface = self.get_instance_bus_interface(
                design, instance_name, bus_name
            )
            _add_logical_ports(instance_name, busInterface, logical_ports)

        for hierInterface in interconnection.hierInterface:
            instance_name = (
                None  # No support for fancy hierarchies. Assume current toplevel
            )
            bus_name = hierInterface.busRef
            busInterface = self.get_top_bus_interface(bus_name)
            _add_logical_ports(instance_name, busInterface, logical_ports)

        for k, log_port in logical_ports.items():
            port_width = log_port["port_width"]
            wire_width = log_port["wire_width"]
            endpoints = log_port["endpoints"]
            for endpoint in endpoints:
                if not endpoint in self.ports:
                    port = Port()
                    port.width = port_width  # fixme
                    self.ports[endpoint] = port
            if len(endpoints) > 1:
                wire = Wire(ic_name + "_" + k)
                wire.width = wire_width
                wire.endpoints = endpoints
                self.wires.append(wire)

                for endpoint in endpoints:
                    self.ports[endpoint].wires.append(wire)

    def infer_width_from_ports(self, wire):
        for endpoint in wire.endpoints:
            width = self.ports[endpoint].width
            if not width:
                # No width in logical port. Try physical port
                if endpoint[0]:
                    instance = self.instances[endpoint[0]]
                    for port in instance.ports:
                        if port.name == endpoint[1]:
                            width = port.width
                            break

            if wire.width and width != wire.width:
                raise Exception(
                    f"Width mismatch for {wire.name}. Wire width is {wire.width}. Port {endpoint[0]}.{endpoint[1]} width is {width}"
                )
            wire.width = width

    def connect(self):
        view_name = self.top_view_name
        component = self.top_component

        view = self.get_view(self.top_component, view_name)

        design = self.get_design(view)

        self.module_ports = self.get_external_ports()  # FIXME: 1-bit vectors

        self.instances = self.get_instances(view)
        if design.adHocConnections:
            for adHocConnection in design.adHocConnections.adHocConnection:
                wire = Wire(adHocConnection.name)
                wire.endpoints = []

                for pr in adHocConnection.portReferences.internalPortReference:
                    endpoint = (pr.componentRef, pr.portRef)
                    wire.endpoints.append(endpoint)

                    if not endpoint in self.ports:
                        port = Port()
                        port.width = 0  # Correct width is inferred later
                        self.ports[endpoint] = port
                    self.ports[endpoint].wires.append(wire)
                for pr in adHocConnection.portReferences.externalPortReference:
                    endpoint = (None, pr.portRef)
                    wire.endpoints.append(endpoint)
                    if not endpoint in self.ports:
                        port = Port()
                        port.width = 0  # Correct width is inferred later
                        self.ports[endpoint] = port
                    self.ports[endpoint].wires.append(wire)

                self.wires.append(wire)

        if design.interconnections or True:
            if design.interconnections:
                for interconnection in design.interconnections.interconnection:
                    self.add_interconnection(design, interconnection)

            def merge_wires(wires):
                alpha_wire = wires[0]
                for beta_wire in wires[1:]:
                    while beta_wire.endpoints:
                        endpoint = beta_wire.endpoints.pop()
                        for i in range(len(self.ports[endpoint].wires)):
                            if self.ports[endpoint].wires[i] == beta_wire:
                                self.ports[endpoint].wires[i] = alpha_wire
                        if not endpoint in alpha_wire.endpoints:
                            alpha_wire.endpoints.append(endpoint)
                return alpha_wire

            # If a port is connected to multiple wires, merge these wires
            for port in self.ports:
                wires = self.ports[port].wires
                if len(wires) > 1:
                    self.ports[port].wires = [merge_wires(wires)]

            # Remove all wires that are now unconnected
            self.wires[:] = [wire for wire in self.wires if len(wire.endpoints) > 1]
            # Fix wire names
            for w in self.wires:
                for e in w.endpoints:
                    if not e[0]:
                        w.external = True
                        w.name = e[1]

            # Negotiate wire widths
            for w in self.wires:
                if not w.width:
                    self.infer_width_from_ports(w)
                min_width = 1000000  # FIXME
                for endpoint in w.endpoints:
                    min_width = min(min_width, self.ports[endpoint].width)
                if min_width == 1000000:
                    raise Exception("No way this is happening")
                if min_width:
                    w.width = min_width

            # Connect instance ports to wires
            for (inst_name, port_name), port in self.ports.items():
                wires = port.wires
                if inst_name and wires:
                    instance = self.instances[inst_name]
                    for inst_port in instance.ports:
                        if inst_port.name == port_name:
                            inst_port.value = wires[0].name

    def write(self, view_name, module_name, output_file):
        vw = VerilogWriter(module_name)  # FIXME
        vw.header = "//design2v did this\n"
        for module_port in self.module_ports.values():
            vw.add(module_port)
        for wire in self.wires:
            if not hasattr(wire, "external"):
                vw.add(wire)
        for instance in self.instances.values():
            vw.add(instance)
        vw.write(output_file)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate structural verilog from an IP-XACT file"
    )
    parser.add_argument("vlnv", help="VLNV of toplevel")
    parser.add_argument("view", help="View of toplevel")
    parser.add_argument("-d", action="append")
    parser.add_argument("-m", dest="module_name")
    parser.add_argument("-o", dest="output_file", help="Write output to file")
    return parser.parse_args()


# if __name__ == '__main__':
#    args = parse_args()
#
#    i = IPXactLibrary()
#    for _dir in args.d:
#        for f in os.listdir(_dir):
#            if f.endswith('.xml'):
#                i.add_file(os.path.join(_dir, f))
#    i.set_top_component(args.vlnv)
#    view_name = args.view
#    i.set_top_view(view_name)
#    try:
#        i.connect()
#    except Exception as e:
#        print(f"Error: {e}")
#        exit(1)
#
#    module_name = args.module_name or i.top_component.name
#
#    i.write(view_name, module_name, args.output_file)


class Ipxact2v(Edatool):

    description = "IP-XACT to Verilog conversion"

    TOOL_OPTIONS = {
        "ipxact2v_options": {
            "type": "str",
            "desc": "Additional options for ipxact2v",
            "list": True,
        },
        "vlnv": {
            "type": "str",
            "desc": "VLNV for toplevel parsed by ipxact2v",
        },
    }

    def configure(self, edam):
        super().configure(edam)

        incdirs = []
        sv_files = []
        unused_files = []

        i = IPXactLibrary()
        for f in self.files:
            if f["file_type"] == "ipxact":
                i.add_file(os.path.join(self.work_root, f["name"]))
            else:
                unused_files.append(f)

        output_file = self.name + ".v"
        self.edam = edam.copy()
        self.edam["files"] = unused_files
        self.edam["files"].append(
            {
                "name": output_file,
                "file_type": "verilogSource",
            }
        )

        sv2v_options = self.tool_options.get("sv2v_options", [])

        print("VLNV=" + self.tool_options.get("vlnv"))
        i.set_top_component(self.tool_options.get("vlnv"))
        view_name = self.tool_options.get("view", "hierarchical")
        i.set_top_view(view_name)
        try:
            i.connect()
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

        module_name = self.tool_options.get("module_name", i.top_component.name)
        i.write(view_name, module_name, output_file)

        #        commands = EdaCommands()
        #        commands.add(
        #            ["sv2v", "-w", output_file]
        #            + sv2v_options
        #            + ["-I" + d for d in incdirs]
        #            + sv_files,
        #            [output_file],
        #            sv_files,
        #        )

        self.commands = []  # commands.commands
