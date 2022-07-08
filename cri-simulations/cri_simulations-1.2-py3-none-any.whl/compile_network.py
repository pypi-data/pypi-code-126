import numpy as np
from cri_simulations.config import *
import sys
from ast import literal_eval
from math import ceil
from bidict import bidict
import logging

try:
    from cri_simulations.partitioning_code.hierarchical_partition import partition as netPart
    partLoad = True
except:
    partLoad = False
    logging.warning("partitioning library failed to load, multicore disabled")

################################################################
# Note: ARCH, N_NG, PTRS_PER_ROW, and DATA_PER_ROW are read in #
# from a YAML config. These values are specific to the current #
# itteration of the CRI hardware and should NOT be altered     #
# unless the corresponding parameters in the hardware change   #
################################################################
"""
class mergedNetwork:
    def __init__(self,axons,connections):
        self.axons = axons
        self.connections = connections
        self.mergeDict = {}
        self.symbol2index = {}

    def merge(self):
        #breakpoint()
        #breakpoint()
        axonKeys =  self.axons.keys()
        connectionKeys = self.connections.keys()
        #ensure keys in axon and neuron dicts are mutually exclusive
        #map those keys to indicies
        mapDict = {} #holds maping from symbols to indicies
        #breakpoint();
        mergeDict = {}
        #construct axon dictionary with ordinal numbers as keys
        for idx, symbol in enumerate(axonKeys):
            mergeDict[idx] = self.axons[symbol]
            mapDict[(symbol,'axons')] = idx
        connectionsStartOffset = idx+1
        #construct connections dicitonary with ordinal numbers as keys
        for idx, symbol in enumerate(connectionKeys):
            currIndex = idx+connectionsStartOffset
            mergeDict[currIndex] = self.connections[symbol]
            mapDict[(symbol,'connections')] = currIndex

        self.symbol2index = bidict(mapDict)
        
        #go through and change symbol based postsynaptic neuron values to corresponding index
        for idx in mergeDict:
            for listIdx in range(len(mergeDict[idx])):
                oldTuple = mergeDict[idx][listIdx]
                newTuple = (self.symbol2index[(oldTuple[0],'connections')],oldTuple[1]) #we now the post synaptic neuron is originially from the connections dict because users never define a connection with a postsynaptic axon
                mergeDict[idx][listIdx] = newTuple

        self.mergeDict = mergeDict

        return mergeDict

    def bifurcate_assignments(self,assignments):
        axonAssignments = {}
        neuronAssignments = {}
        
        for index in assignments.keys():
            symbol = self.symbol2index.inverse[index]
            if (symbol[1] == "axons"):
                axonAssignments[symbol[0]] = assignments[index]
            elif (symbol[1] == "connections"):
                neuronAssignments[symbol[0]] = assignments[index]
            else:
                raise Exception("Invalid neuron catagory")
        return axonAssignments,neuronAssignments
"""
sixteen_flag = True
# 4 ways to load into the network

# - simple text file including the source,destination, weight,

# - ONNX format for deep learning models

# - Networkx connectivity graph

# Some format to accomodate the SpheyreNet Models

def generate_local_neurons(axons,connections,axonAssignments , neuornAssignments,n_cores):
    masterDict = {}
    for i in range(n_cores):
        masterDict[i] = {}
        masterDict[i]["axons"] = {}
        masterDict[i]["connections"] = {}
    for axonKey in axons.keys():
        core = axonAssignments[axonKey] #problem, how do we handle axon indicies across cores?
        masterDict[core]["axons"][axonKey] = axons[axonKey]
    for neuronKey in connections.keys():
        core = neuronAssignments[neuronKey] #problem, how do we handle axon indicies across cores?
        masterDict[core]["connections"][neuronKey] = connections[neuronKey]

        


def get_cores():
    """Get's the number of cores to map the network to
    Returns
    -------
    n_cores : int
        The number of cores to map the network to
    """
    # Get the number of cores to map to
    n_cores = 0
    for fpga_cluster_num, fpga_cluster in enumerate(ARCH):
        for fpga_num, fpga in enumerate(fpga_cluster["FPGA"]):
            for core_cluster_num, core_cluster, in enumerate(fpga["Core_cluster"]):
                for core_num in range(int(core_cluster["Cores"])):
                    n_cores += 1
    return n_cores


def load_network(input, connex, output):
    """Loads the network specification.

    This function loads the inputs and connections specified for the network.
    Also determines the number of FPGA cores to be used.

    Parameters
    ----------
    input : str, optional
        Path to file specifying network inputs. (the default is the path in config.yaml)
    connex : str, optional
        Path to file specifying network connections. (the default is the path in config.yaml)

    Returns
    -------
    axons : dict
        Dictionary specifying axons in the network. Key: axon number Value: Synapse Weights
    connections : dict
        Dictionary specifying neurons in the network. Key: Neuron Number Value: Synapse Weights
    inputs : dict
        Dictionary specifying inputs to the network. Key, Time Step Value, axon
    outputs : dict
        TODO: I'm not sure what the outputs are for. I belive it's unused
    ncores : int
        The number of cores peresent in the CRI system

    """
    axons = {}
    connections = {}
    inputs = {}
    outputs = {}

    # Load in the connectivity file
    ax = None
    with open(connex, "r") as f:
        for line in f:
            if not line.startswith("#"):
                if "axons" in line.lower():
                    ax = True
                elif "neurons" in line.lower():
                    ax = False
                else:
                    pre, post = line.split(":")
                    weights = literal_eval(post.strip())
                    weights = [(int(i[0]), float(i[1])) for i in weights]
                    if ax:
                        axons[int(pre.strip())] = weights
                    else:
                        connections[int(pre.strip())] = weights

    # Load in the inputs file
    with open(input, "r") as f:
        for line in f:
            if not line.startswith("#"):
                pre, post = line.split(":")
                inputs[int(pre.strip())] = literal_eval(post.strip())

    with open(output, "r") as f:
        for line in f:
            if not line.startswith("#"):
                pre, post = line.split(":")
                outputs[int(pre.strip())] = literal_eval(post.strip())

    # Get the number of cores to map to
    # n_cores = 0
    # for fpga_cluster_num, fpga_cluster in enumerate(ARCH):
    #    for fpga_num, fpga in enumerate(fpga_cluster['FPGA']):
    #        for core_cluster_num, core_cluster, in enumerate(fpga['Core_cluster']):
    #            for core_num in range(int(core_cluster['Cores'])):
    #                n_cores += 1
    n_cores = get_cores()

    #print(n_cores)

    # assignment = partition(connex,n_cores)

    assert len(connections.keys()) - 1 in connections.keys()

    return axons, connections, inputs, outputs, n_cores




def partition(connectome, n_cores):
    """Creates adjacency list

    Uses the partitioning algorithm to partition the neurons in the network and return core assignments

    Parameters
    ----------
    network : dict
        Dictionary specifying neurons in the network. Key: Neuron Number Value: Synapse Weights
    ncores : int
        The number of cores peresent in the CRI system

    Returns
    -------
    dict
        Dictionary specifying neurons mapped to each core. Key: core number Value: tuple of (neuron number, core number)
    """
    networkConnectivity = connectome.get_part_format()

    # Create an adjacency list
    # Use the partitioning algorithm to partition the network and return the cluster assignments
    # it might be necessary to merge the axons and neurons into one network to get a good partitioning

    #TODO: get rid of this, it's just for some quick and dirty debugging
    #n_cores =2
    # No partitioning
    if n_cores == 1:
        membership = {k: 0 for k in range(len(networkConnectivity))}
        #return {k: 0 for k, v in connectome.connectomeDict.items()}
         #return {k: 0 for k, v in axons.items()},{k: 0 for k, v in connections.items()}

    # Partition the network
    else:
        if (partLoad):
            membership = netPart(data = networkConnectivity,n_clusters = n_cores) #n_clusters is just the number of cores to partition the network across
        else:
            logging.error("partitioning library failed to load, multicore partitioning skipped")

    connectome.apply_partition(membership)
    #breakpoint()


def external_input_optimization():
    return
    # TODO

"""
def map_to_hbm(axons, network, input, assignment, n_cores):

    # Should operate indpendent of the number of clusters
    # Return a dict of hbm ptrs and data for each cluster

    hbm = {}

    length = 0
    for i in axons:
        length += len(axons[i])
    for i in network:
        length += len(network[i])

    print("LENGTH ", length)

    for i in range(n_cores):
        cluster_nodes = {k: v for k, v in assignment.items() if v == i}
        # print('here')
        # print(cluster_nodes)

        axon_ptrs = len(axons.keys()) * [None]
        neuron_ptrs = len(network.keys()) * [None]

        # ptrs = (len(network.keys()) + len(axons.keys())) * [None]
        counter = 0
        data = []
        print(len(axons))
        # Create the external pointers section of the HBM
        for neuron in range(len(axons)):
            next = counter + int(np.ceil(len(axons[neuron]) / DATA_PER_ROW)) - 1
            if next < counter:
                next = counter
            axon_ptrs[neuron] = (counter, next)
            counter = counter + int(np.ceil(len(axons[neuron]) / DATA_PER_ROW))

        # If there we need more pointers to fit to the data_per_row size, append
        # pointers pointing to the empty data row

        if len(axons) % DATA_PER_ROW != 0:
            for j in range(DATA_PER_ROW - len(axons) % DATA_PER_ROW):
                axon_ptrs.append((counter, counter))
            counter += 1

        # print(axon_ptrs)

        # Create the internal pointers section of the hbm
        for neuron in range(len(network)):

            if assignment[neuron] == i:
                next = counter + int(np.ceil(len(network[neuron]) / DATA_PER_ROW)) - 1
                if next < counter:
                    next = counter
                neuron_ptrs[neuron] = (counter, next)
                counter = counter + int(np.ceil(len(network[neuron]) / DATA_PER_ROW))

        # If there we need more pointers to fit to the data_per_row size, append
        # pointers pointing to the empty data row

        # print(len(neuron_ptrs), len(network))

        if len(network) % DATA_PER_ROW != 0:
            for j in range(DATA_PER_ROW - len(network) % DATA_PER_ROW):
                neuron_ptrs.append((counter, counter))
            counter += 1

        # print(len(axon_ptrs), len(neuron_ptrs))
        dt = np.dtype("object,object")

        ptrs = np.array(axon_ptrs + neuron_ptrs, dtype=dt).reshape((-1, DATA_PER_ROW))

        # Create the data section of the hbm For axons
        for neuron in range(len(axons)):

            row_data = []

            if len(axons[neuron]) <= DATA_PER_ROW:
                for k in range(len(axons[neuron])):
                    row_data.append((0, axons[neuron][k][0], axons[neuron][k][1]))

            else:
                for k in range(len(axons[neuron])):
                    row_data.append((0, axons[neuron][k][0], axons[neuron][k][1]))
                    if k != 0 and k % DATA_PER_ROW == 0:
                        data.append(row_data)
                        row_data = []

            if len(row_data) < DATA_PER_ROW:
                for k in range(len(row_data), DATA_PER_ROW):
                    row_data.append((0, 0, 0))

            data.append(row_data)

        data.append([(0, 0, 0) for j in range(DATA_PER_ROW)])

        # Create data section of HBM for neurons
        for neuron in range(len(network)):

            row_data = []

            for k in range(len(network[neuron])):
                row_data.append((0, network[neuron][k][0], network[neuron][k][1]))
                if len(row_data) % DATA_PER_ROW == 0:
                    data.append(row_data)
                    row_data = []
            if 0 < len(row_data) < DATA_PER_ROW:
                for k in range(len(row_data), DATA_PER_ROW):
                    row_data.append((0, 0, 0))

            if row_data:
                data.append(row_data)

        # Add an emtpy data row to the end for any neurons that aren't important
        data.append([(0, 0, 0) for j in range(DATA_PER_ROW)])

        hbm[i] = (ptrs, data)

    print("Axon Pointers:")
    for i in axon_ptrs:
        print(i)

    print("Neuron Pointers:")
    for i in neuron_ptrs:
        print(i)

    print("HBM DATA")
    for i in data:
        print(i)

    return hbm
"""

def map_to_hbm_fpga(connectome, n_cores, to_fpga=True):
    """Creates HBM Data Structure

    Creates a representation of the axon pointers, neuron pointers, and synapse weights in HBM memory

    Parameters
    ----------
    axons : dict
        Dictionary specifying axons in the network. Key: Axon Number Value: Synapse Weights
    network : dict
        Dictionary specifying neurons in the network. Key: Neuron Number Value: Synapse Weights
    assignment : dict
        Dictionary specifying neurons mapped to each core. Key: core number Value: tuple of (neuron number, core number)
    n_cores : int
        The number of cores peresent in the CRI system
    to_fpga : bool, optional
        This parameter is depracated and has no effect. (the default is True)

    Returns
    -------
    hbm : dict
        Dictionary specifying the structure of data in memory for each core. Key: core number Value: tuple of (pointer,data) where pointer is a numpy array of tuples representing offsets into hbm memory and data is a list of lists tuples representing synapses.
    """

    # Should operate indpendent of the number of clusters
    # Return a dict of hbm ptrs and data for each cluster

    hbm = {}

    rows_per_ptr = ceil(N_NG / DATA_PER_ROW)

    for i in range(n_cores):
        #cluster_nodes = {k: v for k, v in assignment.items() if v == i}

        current = 0

        axon_ptrs = []
        axon_data = []

        ############################
        # Handle the Axons
        ############################
        axons = connectome.get_axons()
        for axonKey in axons:
            axon = axons[axonKey]
            weights = axon.get_synapses()
            used_weights = np.ones(len(weights))
            num_rows = 0
             


            if not weights:
                logging.warning("Axon with no synapses detected")
                if sixteen_flag:
                    # if there is no weights we append NG_Num number of rows of empty synapses and a pointer to those rows
                    for i in range(rows_per_ptr):
                        axon_data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    axon_ptrs.append((current, current + (rows_per_ptr - 1)))
                    current += rows_per_ptr
                else:
                    axon_data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    axon_ptrs.append((current, current))
                    current += 1
                continue

            while sum(used_weights) != 0:
                row = np.zeros(N_NG).astype(object)
                for w in range(len(weights)):
                    if used_weights[w] != 0:
                        column = weights[w].get_postsynapticNeuron().get_coreTypeIdx() % N_NG
                        if row[column] == 0:
                            row[column] = (
                                0,
                                np.floor(weights[w].get_postsynapticNeuron().get_coreTypeIdx() / N_NG),
                                weights[w].get_weight(),
                            )
                            used_weights[w] = 0
                row = [r if r != 0 else (0, 0, 0) for r in row]
                if sixteen_flag:
                    num_rows += rows_per_ptr
                    temp = np.empty(len(row), dtype=object)
                    temp[:] = row
                    axon_row_list = temp.reshape(-1, DATA_PER_ROW)
                    axon_row_list = np.flip(axon_row_list, axis=0)
                    for axon_row in axon_row_list:
                        axon_data.append(axon_row.tolist())
                else:
                    num_rows += 1  # For the pointers
                    axon_data.append(row)
            if sixteen_flag:
                axon_ptrs.append((current, current + num_rows - 1))
                current += num_rows
            else:
                axon_ptrs.append((current, current + num_rows - 1))
                current += num_rows

        if sixteen_flag:
            if len(axon_ptrs) % N_NG != 0:
                # make sure the row is filled with axon pointers TODO: do we just care the row is full or should the number
                # of axon pointers be divisable by 16
                # The correct answer is the total number of axon pointers should be evenly divisable by N_NG
                for j in range(N_NG - len(axon_ptrs) % N_NG):
                    axon_ptrs.append((current, current + rows_per_ptr - 1))
                    current += rows_per_ptr
                    for i in range(rows_per_ptr):
                        axon_data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
        else:
            if len(axon_ptrs) % DATA_PER_ROW != 0:
                for j in range(DATA_PER_ROW - len(axon_ptrs) % DATA_PER_ROW):
                    axon_ptrs.append((current, current))
                    current += 1
                    axon_data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])

        dt = np.dtype("object,object")
        if sixteen_flag:
            axon_ptrs = np.array(axon_ptrs, dtype=dt).reshape((-1, DATA_PER_ROW))
        else:
            axon_ptrs = np.array(axon_ptrs, dtype=dt).reshape((-1, DATA_PER_ROW))

        #################################
        # Handle the Neurons
        #################################
        ptrs = []
        data = []
        neurons = connectome.get_neurons()
        for neuronKey in neurons:
            neuron = neurons[neuronKey]
            weights = neuron.get_synapses()
            used_weights = np.ones(len(weights))
            num_rows = 0

            if not weights:
                if sixteen_flag:
                    # if no weights create a pointer to NG_num rows of zero synapses
                    for i in range(rows_per_ptr):
                        data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    # data.append([(0,0,0) for r in range(DATA_PER_ROW)])
                    ptrs.append((current, current + (rows_per_ptr - 1)))
                    current += rows_per_ptr
                else:
                    data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    ptrs.append((current, current))
                    current += 1
                continue

            space_for_spike = False
            while sum(used_weights) != 0:
                # Create a row
                row = np.zeros(N_NG).astype(object)

                for w in range(len(weights)):
                    if used_weights[w] != 0:
                        column = weights[w].get_postsynapticNeuron().get_coreTypeIdx() % N_NG
                        if row[column] == 0:
                            row[column] = (
                                0,
                                np.floor(weights[w].get_postsynapticNeuron().get_coreTypeIdx() / N_NG),
                                weights[w].get_weight(),
                            )
                            used_weights[w] = 0

                row = [r if r != 0 else (0, 0, 0) for r in row]
                if sixteen_flag:
                    num_rows += rows_per_ptr
                else:
                    num_rows += 1  # For the pointers
                if (0, 0, 0) in row:
                    space_for_spike = True

                if not row:
                    logging.info("empty neuron row found")
                if sixteen_flag:
                    # num_rows += rows_per_ptr
                    temp = np.empty(
                        len(row), dtype=object
                    )  # numpy get's weird about reshaping object arrays
                    temp[:] = row
                    # print(temp)
                    neuron_row_list = temp.reshape(-1, DATA_PER_ROW)
                    neuron_row_list = np.flip(neuron_row_list, axis=0)
                    # print(axon_row_list)
                    # print(DATA_PER_ROW)
                    for neuron_row in neuron_row_list:
                        # print(axon_row.tolist())
                        data.append(neuron_row.tolist())
                else:
                    data.append(row)

            # No place for spike data, we add an additional empty row
            # TODO: is it sufficient to simply add one extra row or does in
            # need to be rows_per_ptr number of empty rows?
            # I'm pretty sure it needs to be rows_per_ptr number of empty rows
            if not space_for_spike:
                if sixteen_flag:
                    for i in range(rows_per_ptr):
                        data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    # data.append([(0,0,0) for r in range(DATA_PER_ROW)])
                    num_rows += rows_per_ptr
                else:
                    data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
                    num_rows += 1

            ptrs.append((current, current + num_rows - 1))
            current += num_rows

        if len(ptrs) % N_NG != 0:
            #print("need to pad neuron pointers")
            #print(ptrs)
            if sixteen_flag:
                for j in range(N_NG - len(ptrs) % N_NG):
                    ptrs.append((current, current + (rows_per_ptr - 1)))
                    current += rows_per_ptr
                    for i in range(rows_per_ptr):
                        data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])
            else:
                for j in range(DATA_PER_ROW - len(ptrs) % DATA_PER_ROW):
                    ptrs.append((current, current))
                    current += 1
                    data.append([(0, 0, 0) for r in range(DATA_PER_ROW)])

        dt = np.dtype("object,object")
        if sixteen_flag:
            ptrs = np.array(ptrs, dtype=dt).reshape((-1, DATA_PER_ROW))
        else:
            ptrs = np.array(ptrs, dtype=dt).reshape((-1, DATA_PER_ROW))

        data = axon_data + data


        hbm[i] = (axon_ptrs, ptrs, data)

        ptrs = np.vstack((axon_ptrs, ptrs))
        

       

    return hbm  # TODO this will need to be fixed for when we move to multicore, it currently only returns hbm for a single core


def compileNetwork(
    loadFile=False, connectome=None, inputs=None, outputs=None):
    """Creates simulation and FPGA data structures

    Creates a representation of the axon pointers, neuron pointers, and synapse weights in HBM memory both in the format used to produce the commands to program the actual FPGA and in the format expected by the hardware simulator.

    Parameters
    ----------
    loadFile : bool
        if True network topology is read from files on disk
    connectome : obj
        object encapsulating axons and connections
    axons : dict
        Dictionary specifying axons in the network. Key: axon number Value: Synapse Weights
    connections : dict
        Dictionary specifying neurons in the network. Key: Neuron Number Value: Synapse Weights
    inputs : dict
        Dictionary specifying inputs to the network. Key, Time Step Value, axon
    outputs : dict
        TODO: I'm not sure what the outputs are for. I belive it's unused
    Returns
    -------
   input : dict
        Dictionary specifying inputs to the network. Key, Time Step Value, TODO are these axons or neurons
    hbm : dict
        Dictionary specifying the hbm structure for each core expected by the hardware simulator. Key: core number Value: tuple of (pointer,data) where pointer is a numpy array and data is a list of lists of tuples.
    outputs : dict
        TODO: I'm not sure what the outputs are for
    axonLength : int
        number of axons specified in the network

"""
    if loadFile:
        axons, network, input, output, n_cores = load_network()
    else:
        if connectome == None or outputs == None:
            raise ValueError(
                "compileNetwork was called with loadFile set to False and one or more input dicitonary was empty"
            )
        # normally load_network returns n_cores, instead we'll just do it explicetly

        n_cores = get_cores()

    partition(connectome, n_cores)
    #generate_local_neurons(axons,connections,axonAssignments , neuornAssignments, n_cores)
    #you're going to have to generate an hbm mapping for every core
    fpga = map_to_hbm_fpga(connectome, n_cores)
    axonLength = len(connectome.get_axons())
    if loadFile:
        return outputs, fpga, axonLength
    else:
        return fpga, axonLength


def main():
    compileNetwork()


if __name__ == "__main__":
    main()
