import time
import logging

import serial
from serial.tools import list_ports

COMMON_TEST_MODE = ["AC", "DC", "IR"]
CHANNEL_VALUE = ["HIGH", "LOW", "OPEN"]

"""
TODO write functions to
- system info
- setting and getting current and voltage for ACW test
- setting and getting current and voltage for DCW test
- setting and getting current and voltage for IR test
"""

# Connection to the serial device
port = list(list_ports.comports())
hipot_tester = [str(p.device) for p in port if str(p).startswith("/dev/cu.usbserial")]
ser = serial.Serial(hipot_tester[0], baudrate=38400, timeout=1)

# Logging
logging.basicConfig(filename='hipot_tester_log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

tic = time.perf_counter()
toc = time.perf_counter()
print(f"the time it took i stg: {toc - tic:0.4f} seconds ! ")


class HipotTester:
    """
    Base class for the Sourcetronic ST9201 Hipot Tester
    """

    def system_info(self):
        """
        Gathers system info about the serial interface
        :return:
        """
        sys_version = ":SYST:VERS? \r \n"
        ser.write(sys_version.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM VERSION: {read_char}")

        idn = "*IDN? \r \n"
        ser.write(idn.encode())
        read_char = ser.read(20).decode()
        print(f":IDN: {read_char}")

        fetch = ":SYST:FETCH? \r \n"
        ser.write(fetch.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM FETCH: {read_char}")

        sys_time_pass = ":SYST:TIME:PASS? \r \n"
        ser.write(sys_time_pass.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM TIME PASS: {read_char}")

        sys_range = ":SYST:WRAN? \r \n"
        ser.write(sys_range.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM RANGE: {read_char}")

        sys_lock = ":SYST:LOCK? \r \n"
        ser.write(sys_lock.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM LOCK: {read_char}")

        sys_agc = ":SYST:DAGC? \r \n"
        ser.write(sys_agc.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM AGC: {read_char}")

        sys_offset = ":SYST:OFFSET? \r \n"
        ser.write(sys_offset.encode())
        read_char = ser.read(20).decode()
        print(f": SYSTEM OFFSET: {read_char}")

        sys_part = ":SYST:PART? \r \n"
        ser.write(sys_part.encode())
        read_resp = ser.read(20).decode()
        print(f": SYSTEM PART: {read_resp}")

        sys_arc = ":SYST:ARC? \r \n"
        ser.write(sys_arc.encode())
        read_resp = ser.read(20).decode()
        print(f": SYSTEM ARC: {read_resp}")

    # Set and get voltage for ACW/DCW/IR test
    def set_voltage(self, step, voltage, test_mode):
        """
        This function sets the voltage for the ACW/DCW/IR test
        :param step: The step for which the voltage is added in the range 1-49
        :param voltage: The voltage to be set in Volts in range 50-5000 volts for ACW test
                        and it must be set in Volts in range 50-6000 volts for DCW test
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        # Set voltage for ACW/DCW/IR test
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_voltage = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LEV {voltage} \r \n"
            ser.write(set_voltage.encode())
            read_char = ser.read(20).decode()
            print(f": SET AC VOLTAGE for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def get_voltage(self, step, test_mode):
        """
        This function checks the voltage for the ACW test
        :param step: The step for which the voltage is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_voltage = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LEV? \r \n"
            ser.write(get_voltage.encode())
            read_char = ser.read(20).decode()
            print(f": GET AC VOLTAGE for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def set_current_limits(self, step, low_limit, high_limit, test_mode):
        """
        This functions sets the lower and upper current limits for ACW/DCW test
        :param test_mode: modes being AC/DC
        :param step: The step for which the current is added in the range 1-49
        :param low_limit: Lower current limit in range 0~30.000E-3 (0 is OFF) Amps for ACW test and
                          lower current limit in range 0~10.000E-3 (0 is OFF) Amps for DCW test
        :param high_limit: Upper current limit in range 1.00E-6~30.000E-3 Amps for ACW test and
                           upper current limit in range 1.00E-6~10.000E-3 Amps for DCW test.
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_low_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:LOW {low_limit} \r \n"
            ser.write(set_low_current.encode())
            read_char = ser.read(20).decode()
            # print(f": SET AC LOW CURRENT for step 1: {read_char}")

            set_high_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:HIGH {high_limit} \r \n"
            ser.write(set_high_current.encode())
            read_char = ser.read(20).decode()
            # print(f": SET AC HIGH CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def get_current_limits(self, step, test_mode):
        """
        This function checks the lower and upper current limits set by the user/by default
        :param test_mode: modes being AC/DC/IR
        :param step: The step for which the current is added in the range 1-49
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_low_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:LOW? \r \n"
            ser.write(get_low_current.encode())
            read_char = ser.read(20).decode()
            print(f": GET LOW CURRENT LIMIT for step {step}: {read_char} Amps")

            get_high_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:HIGH? \r \n"
            ser.write(get_high_current.encode())
            read_char = ser.read(20).decode()
            print(f": GET HIGH CURRENT LIMIT for step {step}: {read_char} Amps")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def arc_set_current_limits(self, step, limit, test_mode):
        """
        This functions sets the ARC current limit for ACW/DCW test
        :param step: The step for which the current is added in the range 1-49
        :param limit: Current limit in range 0~15.0E-3 (0 is OFF) Amps for ACW test and
                      current limit in range 0~10.0E-3 (0 is OFF) Amps for DCW test.
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_arc_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:ARC {limit} \r \n"
            ser.write(set_arc_current.encode())
            read_char = ser.read(20).decode()
            # print(f": SET DC LOW CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def arc_get_current_limits(self, step, test_mode):
        """
        This functions sets the ARC current limit for ACW/DCW test
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_arc_current = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:LIM:ARC? \r \n"
            ser.write(set_arc_current.encode())
            read_char = ser.read(20).decode()
            print(f": GET ARC CURRENT LIMIT for step {step}: {read_char} Amps")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def set_ramp_time(self, step, ramp_time, test_mode):
        """
        This functions sets the RISE time for ACW/DCW/IR tests
        :param step: The step for which the current is added in the range 1-49
        :param ramp_time: Time in range  0~999.9 (0 is OFF) for ACW/DCW/IR test.
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_ramp = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:RAMP {ramp_time} \r \n"
            ser.write(set_ramp.encode())
            read_char = ser.read(20).decode()
            # print(f": SET DC LOW CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def get_ramp_time(self, step, test_mode):
        """
        This functions sets RAMP time for ACW/DCW/IR test
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_ramp = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:RAMP? \r \n"
            ser.write(get_ramp.encode())
            read_char = ser.read(20).decode()
            print(f": GET RAMP TIME for step {step}: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def set_fall_time(self, step, fall_time, test_mode):
        """
        This functions sets the FALL time for ACW/DCW/IR tests
        :param step: The step for which the current is added in the range 1-49
        :param fall_time: Time in range  0~999.9 (0 is OFF) for ACW/DCW/IR test.
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_fall_time = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:FALL {fall_time} \r \n"
            ser.write(set_fall_time.encode())
            read_char = ser.read(20).decode()
            # print(f": SET DC LOW CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def get_fall_time(self, step, test_mode):
        """
        This functions sets the FALL time for ACW/DCW/IR test
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_fall_time = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:FALL? \r \n"
            ser.write(get_fall_time.encode())
            read_char = ser.read(20).decode()
            print(f": GET FALL TIME for step {step}: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")


    def set_test_time(self, step, test_time, test_mode):
        """
        This functions sets the TEST time for ACW/DCW/IR tests
        :param step: The step for which the current is added in the range 1-49
        :param test_time: Time in range  0~999.9 (0 is OFF) for ACW/DCW/IR test.
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            set_test_time = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:FALL {test_time} \r \n"
            ser.write(set_test_time.encode())
            read_char = ser.read(20).decode()
            # print(f": SET DC LOW CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def get_test_time(self, step, test_mode):
        """
        This functions sets the TEST time for the ACW/DCW/IR test
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_test_time = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:TIME:FALL? \r \n"
            ser.write(get_test_time.encode())
            read_char = ser.read(20).decode()
            print(f": GET TEST TIME for step {step}: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode")

    def set_channel(self, step, test_mode, channel, chan_value):
        """
        This functions sets HIGH/LOW/OPEN for the scanner channel for ACW/DCW/IR test.
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :param channel: Channel in the range of 1-8
        :param chan_value: Channel values being HIGH/LOW/OPEN
        :return:
        """
        if (str(test_mode).upper() in COMMON_TEST_MODE) and (str(chan_value).upper() in CHANNEL_VALUE):
            set_channel_value = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:CHAN {channel}:{chan_value} \r \n"
            ser.write(set_channel_value.encode())
            read_char = ser.read(20).decode()
            # print(f": SET DC LOW CURRENT for step 1: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode/Channel Value")

    def get_channel(self, step, test_mode, channel):
        """
        This functions inquires about the set channel value for ACW/DCW/IR test.
        :param channel: Channel value set in the range for 1-8
        :param step: The step for which the current is added in the range 1-49
        :param test_mode: modes being AC/DC/IR
        :return:
        """
        if str(test_mode).upper() in COMMON_TEST_MODE:
            get_test_time = f":SOUR:SAFE:STEP {step}:{str(test_mode).upper()}:CHAN {channel}? \r \n"
            ser.write(get_test_time.encode())
            read_char = ser.read(20).decode()
            print(f": GET CHANNEL VALUE for step {step} and channel {channel}: {read_char}")
        else:
            raise IOError("ERROR: not the correct Test Mode/Channel Value")

    def set_ac_freq(self, step, freq):
        """
        This functions sets the test frequency for ACW test.
        :param step: The step for which the current is added in the range 1-49
        :param freq: Set value 50/60 Hz in ACW test
        :return:
        """
        set_test_time = f":SOUR:SAFE:STEP {step}:AC:TIME:FREQ {freq}\r \n"
        ser.write(set_test_time.encode())
        read_char = ser.read(20).decode()
        # print(f": SET DC LOW CURRENT for step 1: {read_char}")

    def get_ac_freq(self, step):
        """
        This functions checks the test frequency for ACW test.
        :param step: The step for which the current is added in the range 1-49
        :return:
        """
        get_test_time = f":SOUR:SAFE:STEP {step}:AC:TIME:FREQ? \r \n"
        ser.write(get_test_time.encode())
        read_char = ser.read(20).decode()
        print(f": GET FREQUENCY for step {step}: {read_char}")

ser.close()
