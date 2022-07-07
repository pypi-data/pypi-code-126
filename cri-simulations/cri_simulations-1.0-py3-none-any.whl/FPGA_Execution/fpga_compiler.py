import numpy as np
import pickle
import os
import sys
import warnings
import logging
import numpy as np
#warnings.filterwarnings('error')

def text2script(cmd_str):
    """Converts a string of hex characters into the correct format to suppyl to the adxdma dump command.

    Given a string of hex characters with the left most character containing the MSB create a string of pairs of hex characters representing bytes
    with the leftmost byte contanining the LSB in the format expected by the adxdma_dmadump binary for the data argument.

    Parameters
    ----------
    cmd_str : str
        The string of hexidecimal characters to format. The first character represents the hex character containing the MSB

    Returns
    -------
    script_txt : str
        The formated string of bytes
    """
    cmd = cmd_str
    script_txt = ''
    while cmd:
        script_txt += '0x' + cmd[-2:] + ' '
        cmd = cmd[0:-2]
    return script_txt


class fpga_compiler:
    """Produces the needed adxdma dump scripts of a given network to program HBM

    Attributes
    ----------
    input : dict
        The inputs to the network for each timestep. Key, timestep value, list of axons
    axon_ptrs : numpy array
        Array of tuples pointing to the rows containing the synapses for the corresponding Axon.
    Each tuple is (start row, end row).
    neuron_ptrs : numpy array
        Array of tuples pointing to the rows containing the synapses for the corresponding Axon.
    Each tuple is (start row, end row).
    synapses : list
        List of tuples corresponding to synapses. Each tuple is (oncore/offcore bit, synapse address (row index of destination neuron pointer in HBM calculated as floor(destination neuron index / number of neuron groups)), weight)
    HBM_WRITE_CMD : str

    HBM_OP_RW  : str
        OP code to read/write to hbm vie PCie
    NRN_BASE_ADDR : int
        Starting address of neuron pointers in HBM
    SYN_BASE_ADDR : int
        Starting address of synapses in HBM
    PTR_ADDR_BITS : int
        Number of bits used to represent pointer starting adderess
    PTR_LEN_BITS :
        Number of bits used to represent the number of rows of synapses a pointer corresponds to
    SYN_OP_BITS :
        Number of bits used to represent synapse opcode
    SYN_ADDR_BITS :
        Number of bits used to represent synapse address
    SYN_WEIGHT_BITS :
        Number of bits used to represent synapse weight

    """

    # OP code to read/write to hbm vie PCie
    #HBM_OP_RW = '02' + 28 * '00'

    PTR_ADDR_BITS = 23  # HBM row address
    PTR_LEN_BITS = 9  # (8 connections/row x 2^9 rows = 2^12 = 4K connections max)
    AXN_BASE_ADDR = 0  # axon pointer start address
    NRN_BASE_ADDR = 2 ** 14  # neuron pointer start address (2^17 axons / 8 axon pointers/row = 2^14 rows max)
    SYN_BASE_ADDR = 2 ** 15  # (2^17 neurons / 8 neuron pointers/row = 2^14 rows max -> 2^14+2^14=2^15)

    SYN_ADDR_BITS = 13  # each synapse: [31:29]=OpCode  [28:16]=address, [15:0]=weight (1 sign + 15 value, fixed-point)
    SYN_WEIGHT_BITS = 16
    SYN_OP_BITS = 3

    HBM_WRITE_CMD = 'sudo adxdma_dmadump wb 0 0 '

    WRITE = '01' + 63 * '00'

    def __init__(self, data, N_neurons, outputs, coreID = 0):
        '''
        Creates the FPGA Compiler object. Populates spike packets in synapses.

        Paramaters
        ----------
        data: list
            Takes the following format: [0]=input data, [1]=axon pointers, [2]=neuron pointers, [3]=synapses
        N_neurons : int
            Number of neurons in network
        CoreID : int
            Index of core in FPGA to write to
        '''
        coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
        coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
        self.HBM_OP_RW = '02' + coreByte + 27 * '00'
        #self.input = data[0]
        self.axon_ptrs = data[0]
        self.neuron_ptrs = data[1]
        self.synapses = data[2]

        n = 0
        errors = 0
        #This works because of how python handles references but it would be much clearer
        #to directly work with self.neuron_ptrs and self.synapses
        #Find space to insert spike packets and insert them in the numpy array representing synapses

        #only assign spike entries in HBM for neurons in the outputs list
        #for row in range(len(data[1])):
            #for col in range(len(data[1][row]))
        rowLength = len(data[1][0])
        for neuronIdx in outputs:
            row = int(np.floor(neuronIdx / rowLength))
            col = neuronIdx % rowLength
            start = data[1][row][col][0]
            end = data[1][row][col][1] + 1
            finished = False
            for r in data[2][start:end]:
                for i in range(len(r)):
                    if r[i] == (0, 0, 0) and n <= len(outputs):
                        r[i] = (1, neuronIdx)
                        #n += 1
                        finished = True
                        break

                if finished:
                    break
            if not finished:
                if n == len(outputs):
                    pass
                else:
                    
                    if n > N_neurons:
                        logging.info('neuron pointer index is greater than specified number of internal neurons, a spike entry will not be assigned to remaining neuron pointer')
                    else:
                         errors+=1
                         logging.error('neuron pointer index: '+ str(n) +' could not be assigned a spike entry')



        logging.info('spike entry assignment errors: ', errors)
        #print(self.synapses)
        #sys.exit()



    def create_axon_ptrs(self, simDump = False):
        '''
        Creates the necessary adxdma_dump commands to program the axon pointers into HBM

        Returns
        -------
        script : str
            The bash commands to run to program the axon pointers in HBM
        '''

        if simDump:
            dump = []
        axn_ptrs = np.fliplr(self.axon_ptrs)
        #print('axn_ptrs')
        #print(axn_ptrs)

        script = ''
        for r, d in enumerate(axn_ptrs):

            cmd = ''
            for p in d:
                decimal_addr = int(
                    np.binary_repr(p[1] - p[0], self.PTR_LEN_BITS) + np.binary_repr(p[0] + self.SYN_BASE_ADDR,
                                                                                    self.PTR_ADDR_BITS), 2)

                cmd += '{:0{width}x}'.format(decimal_addr, width=8)


            # append HBM write opcode and WRITE command
            cmd = self.HBM_OP_RW + '{:0{width}x}'.format(0x800000 + r, width=6) + cmd
            if simDump:
                #print("we made itttttttttt")
                dump.append(cmd)
            # append command to complete script list
            script += self.txt2script(cmd) + '\n'
        if simDump:
            return dump
        else:
            return script

    def txt2script(self, cmd_str):
        """Converts a string of hex characters into the correct format to suppyl to the adxdma dump command.

        Given a string of hex characters with the left most character containing the MSB create a string of pairs of hex characters representing bytes
        with the leftmost byte contanining the LSB in the format expected by the adxdma_dmadump binary for the data argument.

        Parameters
        ----------
        cmd_str : str
            The string of hexidecimal characters to format. The first character represents the hex character containing the MSB

        Returns
        -------
        script_txt : str
            The formated string of bytes
        """
        cmd = cmd_str
        script_txt = ''
        while cmd:
            script_txt += '0x' + cmd[-2:] + ' '
            cmd = cmd[0:-2]
        return script_txt

    def create_neuron_ptrs(self, simDump = False):
        '''
        Creates the necessary data arguments to pass to the adxdma_dump commands to program the neuron pointers into HBM.
        Data arguments for multiple adxdma_dump commands are seperated by new line characters

        Returns
        -------
        script : str
            The data arguments to provide to a series of adxdma_dump commands. Data arguments for successive adxdma_dump commands
        are seperated by newline characters
        '''
        if simDump:
            dump = []
        #print(self.neuron_ptrs)
        nrn_ptrs = np.fliplr(self.neuron_ptrs)
        script = ''
        for r, d in enumerate(nrn_ptrs):
            cmd = ''
            for p in d:
                #print(d)
                #print(p)
                cmd += '{:0{width}x}'.format(
                    int(np.binary_repr(p[1] - p[0], self.PTR_LEN_BITS) + np.binary_repr(p[0] + self.SYN_BASE_ADDR,
                                                                                        self.PTR_ADDR_BITS), 2),
                    width=8)


            # append HBM write opcode and address
            cmd = self.HBM_OP_RW + '{:0{width}x}'.format(0x800000 + self.NRN_BASE_ADDR + r, width=6) + cmd

            # append command to complete script list
            if simDump:
                dump.append(cmd)
            else:
                script += self.txt2script(cmd) + '\n'

        if simDump:
            return dump
        else:
            return script

    def create_synapses(self, simDump = False):
        '''
        Creates the necessary adxdma_dump commands to program the synapses into HBM

        Returns
        -------
        script : str
            The bash commands to run to program the synapses in HBM
        '''

        #print(self.synapses, '\n')
        #weights = np.fliplr(self.synapses)
        #print(weights)
        if simDump:
            dump = []
        weights = self.synapses
        script = ''
        n = 0
        for r, d in enumerate(weights):
            cmd = ''
            for w in d:
                if w[0] == 0:
                    # [31] = 0 for internal connections and 1 for external connections, [30:29] = unused for single core
                    # TODO: how do I know if a given synapse is an internal or external connection?
                    cmd += '{:0{width}x}'.format(int(np.binary_repr( 0, self.SYN_OP_BITS) + np.binary_repr(int(w[1]), self.SYN_ADDR_BITS) + np.binary_repr(int(w[2]),self.SYN_WEIGHT_BITS), 2),width=8)
                #TODO: looks like this format is out of date, it should be the same as the above format. It may not be hyper critical
                elif w[0] == 1:
                    #spike = str(w[0]) + 15 * '0'
                    spike = 16 * '0'
                    addr = np.binary_repr(w[1], self.SYN_ADDR_BITS)
                    #cmd += '{:0{width}x}'.format(int(spike + addr, 2), width=8)
                    cmd += '{:0{width}x}'.format(int(np.binary_repr( 4, self.SYN_OP_BITS) + 12*'0' + np.binary_repr(w[1],17), 2),width=8)



            # append HBM write opcode and address
            cmd = self.HBM_OP_RW + '{:0{width}x}'.format(0x800000 + self.SYN_BASE_ADDR + r, width=6) + cmd
            # append command to complete script list
            if simDump:
                dump.append(cmd)
            else:
                script += self.txt2script(cmd) + '\n'

            #
            n = n + 1

        # write to text file
        if simDump:
            return dump
        else:
            return script


    def gen_input(self,time_step):
            #hex_list = []
            command = "sudo adxdma_dmadump wb 0 0 "
    	  #print(self.input)
            currInput = self.input[time_step]
            opCode = "0x01"
            one_hot_bin = ["0"] * 504
            for axon in currInput:
                one_hot_bin[axon] = "1"
            #one_hot_bin = one_hot_bin[::-1]
            while one_hot_bin:
                curr_byte = one_hot_bin[:8][::-1]
                curr_byte = "".join(curr_byte)
                command = command + " 0x"+'{:0{width}x}'.format(int(curr_byte, 2), width=2)
                one_hot_bin = one_hot_bin[8:]
            command = command+" "+opCode
            return command
            
    def gen_input2(self,time_step,simDump = False):
        """Generates the input command for a given time step

        Generates the necesary bash command to run to provide inputs to the network for a given timestep

        Parameters
        ----------
        time_step : int
            The timestep you wish to generate the input command for

        Returns
        -------
        command : str
            The bash command to run to send the input to the FPGA
        """
        if simDump:
            dump = []
            command = "01"+"00"*63
            currInput = self.input[time_step]
                #opCode = "0x01"
            one_hot_bin = ["0"] * 504
            for axon in currInput:
                one_hot_bin[axon] = "1"

            one_hot_bin.reverse() #makesure LSB is on left
            one_hot_bin_reverse = "".join(one_hot_bin) #make sure LSB is on the left
            one_hot = '{:0{width}x}'.format(int(one_hot_bin_reverse, 2), width=64*2)
            dump.append(command)
            dump.append(one_hot)
            return dump

        else:
            #hex_list = []
            command = "sudo adxdma_dmadump wb 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1"
            #print(self.input)
            currInput = self.input[time_step]
            #opCode = "0x01"
            one_hot_bin = ["0"] * 504
            for axon in currInput:
                one_hot_bin[axon] = "1"
            #one_hot_bin = one_hot_bin[::-1]
            while one_hot_bin:
                curr_byte = one_hot_bin[:8][::-1]
                curr_byte = "".join(curr_byte)
                command = command + " 0x"+'{:0{width}x}'.format(int(curr_byte, 2), width=2)
                one_hot_bin = one_hot_bin[8:]
            command = command+" "+"0x00"
            return command

    def create_input_script(self,num_timesteps,n_inputs,filename):


        commands = ['sudo ./hyddenn2_new.sh 31']
        if num_timesteps < len(self.input):
            hex_timesteps = "0x{:02X}".format(num_timesteps)
        commands.append('sudo adxdma_dmadump wb 0 0 %s 0x00 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0x0 0x0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7'%(hex_timesteps))
        #print(commands)
        #print(self.input)

        for i in range(num_timesteps+1):
            inputs = [0] * (n_inputs + 1)#initialize inputs
            #print(len(inputs))
            #print(self.input[0][-5:])
            for j in range(len(self.input[i])):
                inputs[self.input[i][j]] = 1

            #print(inputs)
            #Create the inputs and group by 8's
            dump = []
            while(inputs):
                tobin = inputs[:8][::-1]
                tobin = ''.join([str(k) for k in tobin])
                tobin = "0x{:02X}".format(int(tobin,2))
                dump.append(tobin)
                del inputs[:8]
                #print(dump)

            n_bits = 64 - len(dump)
            dump = " ".join(dump)
            c = 'sudo adxdma_dmadump wb 0 0 ' + dump + ' 0' * n_bits
            commands.append(c)

        with open(filename + '_input_script.txt', 'w') as f:
            for i in commands:
                f.write(i + '\n')

    def create_script(self, fname, simDump = False):
        """Generates the bash file to program HBM for the current network

        Generates the bash file needed to program the axon pointers, neuron pointers, and synapses into hbm

        Parameters
        ----------
        fname : int
            The filename to write the script to
        """
        #breakpoint()
        axon_ptrs = self.create_axon_ptrs(simDump)
        neuron_ptrs = self.create_neuron_ptrs(simDump)
        synapses = self.create_synapses(simDump)

        if simDump:
            return axon_ptrs, neuron_ptrs, synapses

        #print(axon_ptrs)
        #sys.exit()

        try:
            path = os.path.join(os.getcwd(), fname + '_script.txt')
            os.remove(path)
        except OSError:
            pass

        with open(fname + '_script.txt', 'a') as f2:
            f2.writelines('echo "Configuring Axon Pointers... "\n')

        cmd = self.HBM_WRITE_CMD

        l = 0
        axon_ptr_length = len(axon_ptrs.split('\n'))
        #print('axon_ptr, length', axon_ptr_length)
        for line in axon_ptrs.split('\n'):
            if line:
                with open(fname + '_script.txt', 'a') as f2:
                    f2.writelines(cmd + line[:-1] + '\n')#[:-1] is to get all elements in line except newline character
                    if l == int(axon_ptr_length /4) or l == int(axon_ptr_length /2) or l == int(axon_ptr_length * 3/4):
                        f2.writelines('echo "Finished with %d out of %d"\n' % (l,axon_ptr_length))
            l+=1
        with open(fname + '_script.txt', 'a') as f2:
            f2.writelines('echo "Configuring Neuron Pointers... "\n')

        cmd = self.HBM_WRITE_CMD

        l = 0
        neuron_ptr_length = len(neuron_ptrs.split('\n'))
        for line in neuron_ptrs.split('\n'):
            if line:
                with open(fname + '_script.txt', 'a') as f2:
                    f2.writelines(cmd + line[:-1] + '\n')
                    if l == int(neuron_ptr_length /4) or l == int(neuron_ptr_length /2) or l == int(neuron_ptr_length * 3/4):

                        f2.writelines('echo "Finished with %d out of %d"\n'%(l, neuron_ptr_length))
            l+=1

        with open(fname + '_script.txt', 'a') as f2:
            f2.writelines('echo "Configuring Synapses... "\n')

        cmd = self.HBM_WRITE_CMD

        l = 0
        syn_length = len(synapses.split('\n'))
        for line in synapses.split('\n'):
            if line:
                with open(fname + '_script.txt', 'a') as f2:
                    f2.writelines(cmd + line[:-1] + '\n')
                    if l == int(syn_length /4) or l == int(syn_length /2) or l == int(syn_length * 3/4):

                        f2.writelines('echo "Finished with %d out of %d"\n'%(l, syn_length))
            l+=1

	

def main():
    with open('test' + '.pkl', 'rb') as f:
        data = pickle.load(f)

    f = fpga_compiler(data, 6271)

    f.create_script('test_config')
    #TODO: these values should not be hardcoded
    f.create_input_script(num_timesteps=0,n_inputs=1,filename='test_input')
    #print(f.create_neuron_ptrs().split('\n'))


if __name__ == '__main__':
    main()
