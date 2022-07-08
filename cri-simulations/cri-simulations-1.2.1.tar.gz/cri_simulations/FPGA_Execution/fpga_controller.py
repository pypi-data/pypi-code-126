import click
import os
import yaml
import pickle
import io
import numpy as np
import math
import subprocess
import time
import re
import logging
from collections import defaultdict
#import .FPGA_Execution.base_functions as base_functions
from cri_simulations.config import *
import cri_simulations.FPGA_Execution.base_functions as base_functions
from cri_simulations.FPGA_Execution.fpga_compiler import text2script

#n_internal = None
#n_inputs = None
#inputs = None
ng_num = 16
debug_prints = False

def bin_format(integer, length):
    """converts an integer to a binary string of length length
    """
    return f'{integer:0>{length}b}'


def load(fromFile = False, n_internal=None, n_inputs=None, inputs=None):
    """Reads configuration values from yaml file.

    Populates the global variables n_internal, n_inputs, and inputs with
    the values of the corresponding keys in config.yaml. n_internal is the number
    of neurons in the network, n_inputs is the number of axons, inputs is a list of
    inputs to the network at different time steps. We may no longer use the input values
    read from the yaml file.

    """
    #global n_internal
    #global n_inputs
    #global inputs

    if fromFile:
        if os.path.isfile('FPGA_Execution/config.yaml'):
            with open("FPGA_Execution/config.yaml", 'r') as f:
                data = yaml.safe_load(f)

            n_internal = data['n_internal']
            n_inputs = data['n_inputs']
            inputs = data['inputs']
        else:
            raise FileNotFoundError('File Not Found, or an Error was detected. Have you ran the --init command yet?')
    else:
            n_internal = n_internal
            n_inputs = n_inputs
            inputs = inputs   

def twos_comp(val, bits):
    """compute the 2's complement of int value val

    Takes the int casting of a two's compliment binary string and the number
    of bytes in the binary string and returns the value of the two's compliment
    representation correspondin to the original binary string.

    Parameters
    ----------
    val : int
        the binary stirng to compute the two's compliment of casted to an int
    bits : int
        the number of bits corresponding to the original binary representation of val

    Return
    ------
    val : int
        the value of the original two's compliment binary string
         
    """
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def get_packet_type(string):
    """Caluclates and prints the membrane potentials corresponding to a PCIe packet from
       the FPGA

    Given the packet returned by a PCIe read from URAM this function calculates the neuron index
    and membrane potential of the neruon represented by the PCIe packet and prints those values
    to terminal

    Parameters
    ----------
    string : str
        The string returned by the PCIe command to read URAM

    """
    if debug_prints:
        print(string)
    #breakpoint()
    string = string.split('\n')[3]
    string = string.replace('INFO', '')
    new = ''
    for i in string:
    
        if i not in [':', '?', '.', '@']:
            new += i

    new = new.strip().split(' ')
    new = [i for i in list(filter(None, new)) if len(i) < 3]
    #breakpoint()
    tag = new[15]+new[14]
    return tag
    #print(new)

def read_spikes(string):
    """Caluclates and prints the incoming spikes corresponding to a PCIe packet from
       the FPGA

    Given a spike packet this function decodes the spike packet

    Parameters
    ----------
    string : str
        The string returned by the PCIe command to read spikes

    """
    if debug_prints:
        print(string)
    splitString = string.split('\n')
    processedString = []
    #breakpoint()
    for substring in splitString:
        if (substring): #ignore the empty stirng split generates after the last newline
            strippedSubstring = substring.replace('INFO', '')
            new = ''
            for i in strippedSubstring:
                #breakpoint()
                if i in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F', ' ']:
                    new += i
            new = new.strip().split(' ')
            new = [i for i in list(filter(None, new)) if len(i) < 3]
            processedString += new
    processedString.reverse()
    mergedString = "".join(processedString)
    spikeInt = int(mergedString, 16) #convert hex to dec
    binLength = len(mergedString)*4 #calculate number of bits hex string should occupy
    binary = bin_format(spikeInt, binLength) #convert to binary string
    #extract the tag
    tag = '{:0{width}x}'.format(int(binary[:32], 2), width=2)
    #extract the executionRun_counter
    executionRun_counter = int(binary[-32:], 2)
    #extract the region containing spike data
    spikeData = binary[32:-32]
    spikePacketLength = 32
    spikeList = []
    for spikePacket in [spikeData[i:i+spikePacketLength] for i in range(0, len(spikeData), spikePacketLength)]:
        subexecutionRun_counter, address = processSpikePacket(spikePacket)
        if (subexecutionRun_counter != None and address != None):
            spikeList.append((subexecutionRun_counter,address))
    #breakpoint()
    #print('spikeList: ' + str(spikeList))
    return executionRun_counter, spikeList

def processSpikePacket(spikePacket):
    """Processes an incoming binary string representing a single spike event
    """
    #breakpoint()
    valid = bool(int(spikePacket[8])) #check if it's a valid spike packet
    #valid = True #TODO: THIS IS JUST FOR DEBUGGING DELETE THIS LINE
    if valid:
        subexecutionRun_counter = int(spikePacket[0:8], 2)
        address = int(spikePacket[-17:],2)
        #breakpoint()
        return subexecutionRun_counter, address
    else:
        return None, None

def read_membranes(string):
    """Caluclates and prints the membrane potentials corresponding to a PCIe packet from
       the FPGA

    Given the packet returned by a PCIe read from URAM this function calculates the neuron index
    and membrane potential of the neruon represented by the PCIe packet and prints those values
    to terminal

    Parameters
    ----------
    string : str
        The string returned by the PCIe command to read URAM

    """
    #breakpoint()
    #if debug_prints:
    logging.debug(string)
    substring = string.partition('\n')[0]
    strippedSubstring = substring.replace('INFO', '')
    new = ''
    for i in strippedSubstring:
    
        if i not in [':', '?', '.', '@']:
            new += i

    new = new.strip().split(' ')
    new = [i for i in list(filter(None, new)) if len(i) < 3]


    #print(new)
    col = bin(int(new[6],16))[2:].zfill(8)
    #print(col)
    col = int(col[3:7],2)
    #print(col)
    row =  (bin(int(new[6],16))[2:].zfill(8))[7] + bin(int(new[5],16))[2:].zfill(8) + (bin(int(new[4],16))[2:].zfill(8))[:4]
    row = int(row,2)
    #print(row)
    mp = (bin(int(new[4],16))[2:].zfill(8))[4:] + bin(int(new[3],16))[2:].zfill(8) + bin(int(new[2],16))[2:].zfill(8) + bin(int(new[1],16))[2:].zfill(8) + bin(int(new[0],16))[2:].zfill(8)
    mp = twos_comp(int(mp,2), len(mp))
    #print(mp)
    #input("wait")
    #print('Neuron index %d, Neuron Row %d, Neuron Column %d, Membrane Potential %d'% (ng_num * row + col, row, col, mp))
    return (ng_num * row + col, row, col, mp)
    #input("press enter")
'''    while new:
        #Reverse the order
        mp = new[1] + new[0]
        addr = new[4] + new[3] + new[2]
        mp = bin(int(mp,16))[2:].zfill(16)
        addr = bin(int(addr,16))[2:].zfill(17)
        addr = addr[-17:] #only use last 17 bits
        mp = twos_comp(int(mp,2), len(mp))
#        print('row,col', int(addr[3:],2), int(addr[0:3],2))
        print('Neuron index %d, Membrane Potential %d'% (8 * int(addr[3:],2) + int(addr[0:3],2), mp))
        del new[0:5]
'''

@click.group()
def interface():
    """Untested
    """
    pass

def flush_reads():
    """Flushes any remaining reads from the FPGA

    Notes
    -----
    This function currently does not work and appears to cause issues with successive operations interacting
    with the FPGA

    """
    command = 'sudo adxdma_dmadump rb 0 0 0x40'
    while True:
        try:
            subprocess.run(command,shell=True, timeout=10, check=True)
        except:
            print("timeout expired")
            break

def clear_address_packet(row,col,simDump=False):
    rowBin = np.binary_repr(row,13)
    colBin = np.binary_repr(col,4)
    byte4 = rowBin[-4:]+'0'*4
    byte5 = rowBin[-12:-4]
    byte6 = '0'*2+'1'+np.binary_repr(col,4)+rowBin[0]

    byte4_hex = '{:0{width}x}'.format(int(byte4, 2), width=2)
    byte5_hex = '{:0{width}x}'.format(int(byte5, 2), width=2)
    byte6_hex = '{:0{width}x}'.format(int(byte6, 2), width=2)

    if simDump:
        packet = '00 00 00 00' + ' ' + byte4_hex + ' ' +  byte5_hex + ' ' + byte6_hex 
    else:
        packet = '0x00 0x00 0x00 0x00' + ' 0x' + byte4_hex + ' 0x' +  byte5_hex + ' 0x' + byte6_hex 
    return packet

#@interface.command()
def clear(n_internal, simDump = False, coreID = 0):
    """This function clears the membrane potentials on the fpga.

    """
    #updated Feb11
    #load()#is this even needed
    coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
    coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
    commandTail = ' 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ' + coreByte + ' 03'
    if simDump:
        dump = []
    for i in range(int(np.ceil(n_internal / ng_num))):
        if simDump:
            numCol = 16
            for column in range(numCol):
                #command = "03" + "00"*56 + byte + "00" + '{:0{width}x}'.format(i, width=2) + "00"*4
                command = clear_address_packet(row=i,col=column,simDump=True) + commandTail
                command = command.split(sep=' ')
                command.reverse()
                command = ''.join(command)
                dump.append(command)

            #0 0 0 0 $(($i * 16)) 0x00 0x20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0x0 0x0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3

        else:
            command = 'sudo adxdma_dmadump wb 0 0x0 '
            numCol = 16
            for column in range(numCol):
                if (column == numCol-1):
                    command = command + clear_address_packet(row=i,col=column) + commandTail #we don't need the trailing space for the last line of the command
                else:
                    command = command + clear_address_packet(row=i,col=column) + commandTail + ' '

            os.system(command)
            #print(command)
            time.sleep(1)

    if simDump:
        return dump

#@interface.command()

def read_address_packet(row,col, simDump=False):
    rowBin = np.binary_repr(row,13)
    colBin = np.binary_repr(col,4)
    byte4 = rowBin[-4:]+'0'*4
    byte5 = rowBin[-12:-4]
    byte6 = '0'*3+np.binary_repr(col,4)+rowBin[0]

    byte4_hex = '{:0{width}x}'.format(int(byte4, 2), width=2)
    byte5_hex = '{:0{width}x}'.format(int(byte5, 2), width=2)
    byte6_hex = '{:0{width}x}'.format(int(byte6, 2), width=2)

    if simDump:
        packet = '00 00 00 00' + ' ' + byte4_hex + ' ' +  byte5_hex + ' ' + byte6_hex
    else:
        packet = '0x00 0x00 0x00 0x00' + ' 0x' + byte4_hex + ' 0x' +  byte5_hex + ' 0x' + byte6_hex 
    return packet

def clear_read_buffer(coreID = 0):
    while(True):
        currentRead = subprocess.run(['sudo', 'adxdma_dmadump', 'rb', '0', '0' ,'0x40'], stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
        if(get_packet_type(currentRead) == 'FFFF'):
            break

def flush_spikes(coreID = 0):
    spikeOutput = []
    while(True):
        currentRead = subprocess.run(['sudo', 'adxdma_dmadump', 'rb', '0', '0' ,'0x40'], stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
        if(get_packet_type(currentRead) == 'FFFF'):
            break
        elif(get_packet_type(currentRead) == 'EEEE'): #TODO: this is just here for debugging
            executionRun_counter, spikeList = read_spikes(currentRead)
            spikeOutput = spikeOutput + spikeList
        else:
            logging.error("None spike packet encountered during spike flush")

    return spikeOutput



def read(n_internal, simDump = False, coreID = 0):
    """This function reads in the membrane potentials from the fpga.

    """
    #breakpoint()
    above_thresh = []
    #updated Feb11
    #load()#is this even needen
    coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
    coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
    commandTail = ' 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ' + coreByte + ' 03'
    if simDump:
        dump = []
    formated_results = [] #holds the formated output
    #spikeOutput = []
    for i in range(int(np.ceil(n_internal/ng_num))):
        if simDump:
            numCol = 16
            for column in range(numCol):
                #command = "03" + "00"*56 + byte + "00" + '{:0{width}x}'.format(i, width=2) + "00"*4
                command = read_address_packet(row=i,col=column,simDump=True) + commandTail
                command = command.split(sep=' ')
                command.reverse()
                command = ''.join(command)
                dump.append(command)
            #for i in range(ng_num):
            #    dump.append("40")
        else:
            command = 'sudo adxdma_dmadump wb 0 0x0 '
            numCol = 16
            for column in range(numCol):
                #we'll split the command into lines to make it a little easier to read if we choose to print it
                if (column == numCol-1):
                    command = command + read_address_packet(row=i,col=column) + commandTail #we don't need the slash or new line for the last line of the command

                else:
                    command = command + read_address_packet(row=i,col=column) + commandTail + ' '
            subprocess.run(command, shell=True, check=True)

            #time.sleep(1)
            result = [] #holds the raw pcie output

            for i in range(ng_num):
                #print("NEURON GROUP NUMBER: "+str(i))
                while True: #look for the next membrane potential in the fifo
                    currentRead = subprocess.run(['sudo', 'adxdma_dmadump', 'rb', '0', '0' ,'0x40'], stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
                    if(get_packet_type(currentRead) == 'CCCC'):
                        break
                    else: #TODO: this is just here for debugging
                        #executionRun_counter, spikeList = read_spikes(currentRead)
                        #spikeOutput = spikeOutput + spikeList
                        logging.error("an errant packet was detected during membrane potential readout")
                        #print(executionRun_counter)
                        #print(spikeList)

                result.append(currentRead)                
                #breakpoint()
                #time.sleep(1)
                #print(result[i])
                formated_results.append(read_membranes(currentRead))
            #print(command)
            
    if simDump:
        return dump
    else:
        return formated_results#, spikeOutput


@interface.command()
@click.option('--filename',default=None, help='Pickled Network Configuration file')
@click.option('--n_inputs', default=None, help='Number of axons')
@click.option('--n_internal',default=None, help='Number of Neurons')
def init(filename,n_inputs,n_internal):
    """Untested
    """
    if filename is None or n_inputs is None or n_internal is None:
        raise ValueError('Command Line Arguments must be specified')


    with open(filename, 'rb' ) as f:
        file = pickle.load(f)

    inp = file[0]

    try:
        n_inputs = int(n_inputs)
        n_internal = int(n_internal)
    except ValueError:
        print('Failed! Make sure the number of inputs and internal values are numbers')

    data = {'inputs' : inp, 'n_inputs': n_inputs, 'n_internal': n_internal}
    with io.open('config.yaml', 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

##PCIe commands for setting network parameters
## [511:504] --> 0x4
## [71:70] --> exec_neuron_model
## [69:34] --> 36-bit threshold
## [33:17] --> NUM OUTPUTs in the network
## [16:0] --> NUM INPUTs in the network

def write_parameters(neron_model, threshold, n_outputs, n_inputs, coreID = 0, simDump = False):
    """Writes the network parameters to the FPGA

    Parameters
    ----------
    neuron_model : int
        The type of neuron model to use (1: incremental I&F, 2: leaky I&F, 3: non-leaky I&F)
    threshold : int
        Neuron spike threshold
    n_outputs : int
        The number of neurons in the network
    n_inputs : int
        The number of axons in the network
    """
    #load()
    n_inputs_bin = np.binary_repr(n_inputs,17)
    a_bin = n_inputs_bin[9:17]
    b_bin = n_inputs_bin[1:9]
    c_bin = ["0"] * 8
    c_bin[7] = n_inputs_bin[0] #set lsb of c_bin
    n_outputs_bin = np.binary_repr(n_outputs,17)
    c_bin[:7] = n_outputs_bin[10:17] #set msb of cbit as lsb of outputs
    c_bin = "".join(c_bin)
    d_bin = n_outputs_bin[2:10]
    e_bin = ["0"] * 8
    e_bin[6:8] = n_outputs_bin[:2]
    threshold_bin = np.binary_repr(threshold,36)
    e_bin[:6] = threshold_bin[30:]
    e_bin = "".join(e_bin)
    f_bin = threshold_bin[22:30]
    g_bin = threshold_bin[14:22]
    h_bin = threshold_bin[6:14]
    i_bin = ["0"] * 8
    i_bin[2:] = threshold_bin[:6]
    n_model_bin = np.binary_repr(neron_model,2)
    i_bin[:2] = n_model_bin
    i_bin = "".join(i_bin)
    h_hex = "0x04"
    a_hex = '{:0{width}x}'.format(int(a_bin, 2), width=2)
    b_hex = '{:0{width}x}'.format(int(b_bin, 2), width=2)
    c_hex = '{:0{width}x}'.format(int(c_bin, 2), width=2)
    d_hex = '{:0{width}x}'.format(int(d_bin, 2), width=2)
    e_hex = '{:0{width}x}'.format(int(e_bin, 2), width=2)
    f_hex = '{:0{width}x}'.format(int(f_bin, 2), width=2)
    g_hex = '{:0{width}x}'.format(int(g_bin, 2), width=2)
    h_hex = '{:0{width}x}'.format(int(h_bin, 2), width=2)
    i_hex = '{:0{width}x}'.format(int(i_bin, 2), width=2)
    #print(a_hex)
    #print(c_hex)
    #print(threshold_bin)

    coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
    coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
    if simDump:
        return ["04"+coreByte+"00"*53+i_hex+h_hex+g_hex+f_hex+e_hex+d_hex+c_hex+b_hex+a_hex]

    command = "sudo adxdma_dmadump wb 0 0x0 0x$a 0x$b 0x$c 0x$d 0x$e 0x$f 0x$g 0x$h 0x$i 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
                  0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 " +"0x"+coreByte +" 0x04"
    command = command.replace('$a', a_hex)
    command = command.replace('$b', b_hex)
    command = command.replace('$c', c_hex)
    command = command.replace('$d', d_hex)
    command = command.replace('$e', e_hex)
    command = command.replace('$f', f_hex)
    command = command.replace('$g', g_hex)
    command = command.replace('$h', h_hex)
    command = command.replace('$i', i_hex)
    logging.info("programminng network parameters")
    #print(command)
    os.system(command)

#@interface.command()
def execute(simDump=False, coreID = 0):
    """ Runs a single step of the network and prints "executing a Timestep: " to the terminal
    """
    # Implement Running the Command for one timestep
    coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
    coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
    if simDump:
        command = ["06"+coreByte+"00"*62]
        return command
    else:
        #click.echo('Executing a Timestep: ')
        base_functions.execute(coreID)

@interface.command()
@click.option('--filename', default=' ', help='HBM configuration file')
def configure(filename):
    """Untested
    """
    # Implement Configuring the network
    click.echo('Starting Board Configuration')
    if not os.path.isfile(filename):
        raise FileNotFoundError('File "%s" does not exist'%(filename))

    os.system('sudo chmod +x %s'%(filename))
    os.system('sudo ./%s'%(filename))

@interface.command()
@click.option('--timestep',default=0,help='Timestep Number')
def input(timestep, n_inputs, inputs):
    """Untesetd
    """

    # Implement Configuring the network
    click.echo('Sending inputs at timestep %d to the board'%(timestep))
    #load()
    #print(inputs)
    vals = inputs[timestep]

    for i in vals:
        if i >= n_inputs or i < 0:
            raise ValueError('An input is not valid (Not in the number of external inputs)')

    binary = '0' * n_inputs
    binary = "".join(['1' if i in vals else '0' for i in range(n_inputs)])[::-1]
    final = hex(int(binary, 2))

    #Send write external input PCIe command
    os.system('sudo adxdma_dmadump wb 0 0  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1')
    os.system('sudo adxdma_dmadump wb 0 0 %s 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'%(final))

def step_input(command):
    """This just runs a command formated to be run with bash
    """
    os.system(command)

def input_user(inputs, numAxons, simDump = False, coreID=0, reserve=False):
    """Generates the input command for a given time step

    Generates the necesary bash command to run to provide inputs to the network for a given timestep

    Parameters
    ----------
    inputs : list of int
        The currently spiking axons

    Returns
    -------
    command : str
        The bash command to run to send the input to the FPGA
    """
    if simDump:
        if (reserve):
            dump = []
            command = "01"+"00"*63
            currInput = inputs
                #opCode = "0x01"

            one_hot_bin = ["0"] * 256
            for axon in currInput:
                one_hot_bin[axon] = "1"
            coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
            coreByte = '{:0{width}x}'.format(int(coreBits, 2), width=2)
            one_hot_bin = one_hot_bin

            one_hot_bin.reverse() #makesure LSB is on left
            one_hot_bin_reverse = "".join(one_hot_bin) #make sure LSB is on the left
            one_hot = "00"+coreByte+31*"00"+'{:0{width}x}'.format(int(one_hot_bin_reverse, 2), width=31*2)
            dump.append(command)
            dump.append(one_hot)
        else:
            dump = []
            command = "01"+"00"*63
            dump.append(command)
            currInput = inputs
            currInput.sort()
            for count in range(math.ceil(numAxons/512)):
                #opCode = "0x01"
                one_hot_bin = ["0"] * 512
                inputSegment = [i for i in currInput if (512*count) <= i and i < (512*count+512) ]
                for axon in inputSegment:
                    one_hot_bin[axon%512] = "1"

                one_hot_bin.reverse() #makesure LSB is on left
                one_hot_bin_reverse = "".join(one_hot_bin) #make sure LSB is on the left
                one_hot = '{:0{width}x}'.format(int(one_hot_bin_reverse, 2), width=64*2)
            #dump.append(command)
                dump.append(one_hot)
        #breakpoint()
        return dump

    else:
        if (reserve): #new format upper 256 bits are reserved
            #hex_list = []
            command = "sudo adxdma_dmadump wb 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1"
            #print(self.input)
            currInput = inputs
            #opCode = "0x01"
            one_hot_bin = ["0"] * 256
            for axon in currInput:
                one_hot_bin[axon] = "1"
            #one_hot_bin = one_hot_bin[::-1]
            while one_hot_bin:
                curr_byte = one_hot_bin[:8][::-1]
                curr_byte = "".join(curr_byte)
                command = command + " 0x"+'{:0{width}x}'.format(int(curr_byte, 2), width=2)
                one_hot_bin = one_hot_bin[8:]
            tail = 30*" 0x00"
            coreBits = np.binary_repr(coreID,5)+3*'0'#5 bits for coreID
            coreByte = "0x"+'{:0{width}x}'.format(int(coreBits, 2), width=2)
            command = command+tail+" "+coreByte +" "+"0x00"
        else:
            #hex_list = []
            
            #print(self.input)
            currInput = inputs
            currInput.sort()
            command = "sudo adxdma_dmadump wb 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1"
            #opCode = "0x01"
            for count in range(math.ceil(numAxons/512)):
                
                one_hot_bin = ["0"] * 512
                inputSegment = [i for i in currInput if (512*count) <= i and i < (512*count+512) ]
                for axon in inputSegment:
                    one_hot_bin[axon%512] = "1"
            #one_hot_bin = one_hot_bin[::-1]
                while one_hot_bin:
                    curr_byte = one_hot_bin[:8][::-1]
                    curr_byte = "".join(curr_byte)
                    command = command + " 0x"+'{:0{width}x}'.format(int(curr_byte, 2), width=2)
                    one_hot_bin = one_hot_bin[8:]
        #breakpoint()
        subprocess.run(command,shell = True, check = True)
    
@interface.command()
def fullrun():
   """Untested
   """
   os.system('sudo ./hyddenn2_new.sh 0')
   base_functions.execute()
   base_functions.flush()

def execute_step():
   """Duplicate of execute() without printing to terminal
   """
   base_functions.execute()

@interface.command()
@click.option('--nums',default=1,help='The number of the commands to flush')
def flush(nums):
    """Untested
    """
    base_functions.flush(nums)

def write_synapse_row(r, row, simDump = False, coreID = 0):
    '''
    Creates the necessary adxdma_dump commands to program the synapses into HBM

    Returns
    -------
    script : str
        The bash commands to run to program the synapses in HBM
    '''
    #breakpoint()
    commandPrefix = '02' + '{:0{width}x}'.format(coreID, width=2) + '000000000000000000000000000000000000000000000000000000'
    if simDump:
        dump = []
    #weights = self.synapses
    #script = ''
    #n = 0
    #for r, d in enumerate(weights):
    cmd = ''
    for w in row:
        if w[0] == 0:
            # [31] = 0 for internal connections and 1 for external connections, [30:29] = unused for single core
            # TODO: how do I know if a given synapse is an internal or external connection?
            cmd += '{:0{width}x}'.format(int(np.binary_repr( 0, SYN_OP_BITS) + np.binary_repr(int(w[1]), SYN_ADDR_BITS) + np.binary_repr(int(w[2]),SYN_WEIGHT_BITS), 2),width=8)
        #TODO: looks like this format is out of date, it should be the same as the above format. It may not be hyper critical
        elif w[0] == 1:
            spike = str(w[0]) + 15 * '0'
            addr = np.binary_repr(w[1], SYN_ADDR_BITS)
            #cmd += '{:0{width}x}'.format(int(spike + addr, 2), width=8)
            cmd += '{:0{width}x}'.format(int(np.binary_repr( 4, SYN_OP_BITS) + 12*'0' + np.binary_repr(w[1],17), 2),width=8)



    # append HBM write opcode and address
    #breakpoint()
    cmd = commandPrefix + '{:0{width}x}'.format(0x800000 + SYN_BASE_ADDR + r, width=6) + cmd
    # append command to complete script list
    if simDump:
        dump.append(cmd)
    else:
        hexString = text2script(cmd)
        finalCmd = HBM_WRITE_CMD + hexString[:-1]
        #
    #n = n + 1

    # write to text file
    if simDump:
        return dump
    else:
        os.system(finalCmd)


if __name__ == '__main__':
    interface()
