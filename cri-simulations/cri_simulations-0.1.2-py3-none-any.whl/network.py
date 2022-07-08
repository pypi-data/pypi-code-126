from cri_simulations.compile_network import compileNetwork
from cri_simulations.FPGA_Execution.fpga_compiler import fpga_compiler
import subprocess
import numpy as np
import time
import functools
import operator
import logging
from cri_simulations.config import *
from cri_simulations.FPGA_Execution.fpga_controller import write_parameters, clear, step_input, read, execute, write_synapse_row, input_user, flush_spikes, clear_read_buffer
class network:
    """A class for creating networks to be run on the CRI hardware

    Attributes
    ----------
    inputs : dict
        Dictionary specifying inputs to the network. Key, Time Step Value, TODO are these axons or neurons
    hbmRecord : dict
        Dictionary specifying the hbm structure for each core. Key: core number Value: tuple of (pointer,data) where pointer is a numpy array and data is a list of lists of tuples.
    outputs : dict
        TODO: I'm not sure what the outputs are for
    axonLength : int
        number of axons specified in the network
    self.numNeuron : int
        number of neurons specified in the network
    """

    def __init__(self, connectome, outputs, config, simDump = False, coreOveride = 0):
        self.coreOveride = coreOveride #TODO:this is for debugging
        self.hbm, self.numAxon = compileNetwork(
            loadFile=False,
            connectome = connectome,
            outputs=outputs
            
        )
        # TODO: this will need to be generalized for multiple networks
        #print(self.hbm.keys())
        axon_ptrs, ptrs, data = self.hbm[1] #This starts at 1 for whatever reason TODO: fix this so it's zero indexed
        self.num_inputs = len(connectome.get_axons()) #number of axons in the network
        self.num_outputs = len(connectome.get_neurons())
        self.outputs = outputs
        self.numNeurons=len(connectome.get_neurons())


        #print('connection points')
        #print(len(connections))
        self.compiledNetwork = fpga_compiler(
            (axon_ptrs, ptrs, data), self.numNeurons, self.outputs, coreID = self.coreOveride
        )
        self.stepNum = None
        #self.maxTimeStep = max(inputs.keys()) #TODO: Change this
        self.neuronType = config['neuron_type']
        self.voltageThresh = config['global_neuron_params']['v_thr']
        self.simDump = simDump
        if simDump:
            self.cmdDump = []

    def initalize_network(self):
        if self.simDump:
            axon_ptrs, neuron_ptrs, synapses = self.compiledNetwork.create_script("test_config", simDump = True)
            self.cmdDump.append(axon_ptrs)
            self.cmdDump.append(neuron_ptrs)
            self.cmdDump.append(synapses)
            #write_parameters(3, self.voltageThresh, n_outputs=length(self.connections), n_inputs=length(self.axons))
            param_cmd = write_parameters(3, self.voltageThresh, n_outputs=self.num_outputs, n_inputs=self.num_inputs, simDump = True, coreID = self.coreOveride)
            self.cmdDump.append(param_cmd)
            clear_cmd = clear(self.numNeurons, simDump = True, coreID = self.coreOveride)
            self.cmdDump.append(clear_cmd)
            self.stepNum = 0
        else:
            clear_read_buffer(coreID = self.coreOveride) #make sure no old data is still in the read buffer
            self.compiledNetwork.create_script("test_config")
            subprocess.call(["cp", "test_config_script.txt", "test_config_script.sh"])

            subprocess.call(["bash", "test_config_script.sh"])
            # subprocess.call(['sudo', 'bash', 'test_input_script.sh'])

      
            # write_parameters(neron_model, threshold, n_outputs, n_inputs)
            #TODO These parameters need to be class attributes
            write_parameters(3, self.voltageThresh, n_outputs=self.num_outputs, n_inputs=self.num_inputs) #TODO: generalize past I&F
            #write_parameters(
            #    3, self.voltageThresh, n_outputs=40, n_inputs=5
            #)
            clear(self.numNeurons)
            self.stepNum = 0

    def run_step(self,inputs,  membranePotential = False):
        if True: #self.stepNum <= self.maxTimeStep:
            if self.simDump:
                input_cmd = input_user(inputs, numAxons = self.num_inputs,  simDump = True,coreID = self.coreOveride)
                self.cmdDump.append(input_cmd)
                #time.sleep(4)
                execute_cmd = execute(simDump = True,coreID = self.coreOveride)
                self.cmdDump.append(execute_cmd)
                #time.sleep(8)
                read_cmd = read(self.numNeurons, simDump = True,coreID = self.coreOveride)
                self.cmdDump.append(read_cmd)
                self.stepNum = self.stepNum +1
                #return result
            else:
                input_user(inputs, numAxons = self.num_inputs, coreID = self.coreOveride)
                #time.sleep(4)
                execute(coreID = self.coreOveride)
                #time.sleep(8)
                spikes = flush_spikes(coreID = self.coreOveride)
                self.stepNum = self.stepNum +1
                if membranePotential:
                    result = read(self.numNeurons,coreID = self.coreOveride)  # TODO make read return the values instead of just printing to terminal
                    return result, spikes
                else: 
                    return spikes
        else:
            logging.warning("run_step did nothing, network has already finished all timesteps")

    def read_synapse(self,preIndex, postIndex, axonFlag = False):
        if self.simDump:
            logging.error("read_synapse commands not added to simDump")
        else:
            #TODO: it optionally might be nice to be able to read from the actual hardware
            if axonFlag:
                pntrs = self.hbm[1][0]
            else:
                pntrs = self.hbm[1][1]
    
            synapseRange = pntrs.flatten()[preIndex]
            synapses = self.hbm[1][2][synapseRange[0]:synapseRange[1]+1]
            columnIdx = postIndex % DATA_PER_ROW #This will correctly find you the column
            rowIdx = np.floor(postIndex / N_NG) #This will tell you what the "within neuron group


            search_synapses = [idx for idx,i in enumerate(synapses) if i[columnIdx][0] == 0 and i[columnIdx][1] == rowIdx and i[columnIdx] != (0,0,0) ]
            if (len(search_synapses) != 1):
                raise ValueError('0 or multiple valid synapses found')
            synapseIdx = (search_synapses[0], columnIdx)
            return synapses[synapseIdx[0]][synapseIdx[1]]

    def sim_flush(self, file):
        dmpStr = ""
        if self.simDump:
            cmdDump = functools.reduce(operator.concat, self.cmdDump)
            with open(file, 'w') as f:
                for item in cmdDump:
                    f.write("%s\n" % item)
                    dmpStr = dmpStr + item + "\n"
            return dmpStr
        else:
            raise Exception("simdump was not set to True at object creation. No commands to flush")

    def write_synapse(self,preIndex, postIndex, weight, axonFlag = False):
#TODO: combine read and write synapse to avoid duplicating code
        if self.simDump:
            logging.warning("write_synapse commands not added to simDump, not implemented yet")
        else:
            if axonFlag:
                pntrs = self.hbm[1][0]
            else:
                pntrs = self.hbm[1][1]

            synapseRange = pntrs.flatten()[preIndex]
            synapses = self.hbm[1][2][synapseRange[0]:synapseRange[1]+1]
            columnIdx = postIndex % DATA_PER_ROW #This will correctly find you the column
            rowIdx = np.floor(postIndex / N_NG) #This will tell you what the "within neuron group index is"


            search_synapses = [idx for idx,i in enumerate(synapses) if i[columnIdx][0] == 0 and i[columnIdx][1] == rowIdx and i[columnIdx] != (0,0,0) ]
            if (len(search_synapses) != 1):
                raise ValueError('0 or multiple valid synapses found')
            synapseIdx = (search_synapses[0], columnIdx)
            oldSynapse = synapses[synapseIdx[0]][synapseIdx[1]]
            row = synapses[synapseIdx[0]]
            row[columnIdx] = (oldSynapse[0],oldSynapse[1],weight)
            write_synapse_row(synapseRange[0]+synapseIdx[0], row, simDump = False)
           #This appears to actually update the values in hbm
                
