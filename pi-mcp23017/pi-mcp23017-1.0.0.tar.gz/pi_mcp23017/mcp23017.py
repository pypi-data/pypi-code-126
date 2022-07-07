"""
contains classes for interfacing the MCP23017
"""
import enum
import logging
import threading
import time

import RPi.GPIO as gpio
import smbus


logger = logging.getLogger("MCP23017")


class Banks(enum.Enum):
    A = 0
    B = 1


class Registers(enum.Enum):
    IODIRA = 0x00
    IODIRB = 0x01
    IPOLA = 0x02
    IPOLB = 0x03
    GPINTENA = 0x04
    GPINTENB = 0x05
    DEFVALA = 0x06
    DEFVALB = 0x07
    INTCONA = 0x08
    INTCONB = 0x09
    IOCON = 0x0a
    GPPUA = 0x0c
    GPPUB = 0x0d
    INTFA = 0x0e
    INTFB = 0x0f
    INTCAPA = 0x10
    INTCAPB = 0x11
    GPIOA = 0x12
    GPIOB = 0x13
    OLATA = 0x14
    OLATB = 0x15


class PullUp(enum.Enum):
    DISABLED = 0
    ENABLED = 1


class Directions(enum.Enum):
    INPUT = 1
    OUTPUT = 0


class MCP23017:
    # static methods

    @staticmethod
    def byte_to_list(b: int) -> list:
        """
        converts on byte into a list of 8 bits, containing either 1 or 0 based on the bit value.
        list[0] is the most right bit
        :param b: byte to convert
        :return: byte represented as a list
        """
        res = []
        for i in range(8):
            if (b & (1 << i)) >= 1:
                res.append(True)
            else:
                res.append(False)
        return res

    @staticmethod
    def get_bank_of_pin(pin: int) -> Banks:
        """
        returns in which bank a pin is found on the MCP
        :param pin:
        :return:
        """
        if 0 <= pin < 8:
            return Banks.A
        elif 7 < pin < 16:
            return Banks.B
        else:
            raise ValueError("Only Pins in [0, 15] are addressable")

    @staticmethod
    def pin_to_register(pin: int) -> tuple:
        """
        returns GPIO Register and bit mask for this specific pin on the MCP
        :param pin: pin in [0, 15]
        :return: (a, b) a: GPIOA or GPIOB, b: mask of the pin as one byte
        """
        if not 0 <= pin < 16:
            raise ValueError("Only Pins in [0, 15] are addressable")
        bank = MCP23017.get_bank_of_pin(pin)

        if bank == Banks.A:
            reg = Registers.GPIOA
        else:
            reg = Registers.GPIOB

        mask = 1 << (pin % 8)

        return reg, mask

    @staticmethod
    def get_active_pin(b: int) -> int:
        """
        returns the index of the active byte. If multiple are active None is returned
        :param b:
        :return:
        """

        lut = {
            0b11111110: 0,
            0b00000001: 0,
            0b11111101: 1,
            0b00000010: 1,
            0b11111011: 2,
            0b00000100: 2,
            0b11110111: 3,
            0b00001000: 3,
            0b11101111: 4,
            0b00010000: 4,
            0b11011111: 5,
            0b00100000: 5,
            0b10111111: 6,
            0b01000000: 6,
            0b01111111: 7,
            0b10000000: 7,
        }

        if b in lut:
            return lut[b]
        else:
            return -1

    # magic methods

    def __init__(self, addr: int = 0x20, int_pin: int = -1, bus: int = 0):
        """
        opens the connection to an MCP23017 portexpander on the given address
        :param addr: absolute i2c address of the port expander
        :param int_pin: the gpio pin in BCM notation of which the interrupt pin is connected to,
        set to -1 to disable interrupt handling
        """
        logger.debug("configuring mcp23017 on address 0x{:X}".format(addr))
        logger.debug("Interrupt Pin is: {}".format(int_pin))
        self.addr = addr
        self.int_pin = int_pin
        gpio.setmode(gpio.BCM)

        self._i2c_dev = smbus.SMBus(bus)
        self.int_en = False  # Flag to determine whether interrupts are enabled

        # lookups for configured inputs and outputs on the MCP
        self._io_lookup = {}
        self._int_lookup = {}

        logger.debug("clearing pending interrupts")
        self._i2c_read(Registers.GPIOA)
        self._i2c_read(Registers.GPIOB)

        # global lock for the interrupt clear loop
        self._int_lock = threading.Lock()

        # interrupts get enabled automatically if a pin is set
        if int_pin != -1:
            # assume MCP INT signal is configured to be active low
            gpio.setup(int_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
            self._initialize_interrupts()
            self.int_en = True

    def __del__(self):
        self._i2c_read(Registers.GPIOA)
        self._i2c_read(Registers.GPIOB)
        self._i2c_dev.close()
        gpio.cleanup()

    def __str__(self):
        return "MCP23017 at 0x{:X} | INT: {}".format(self.addr, self.int_pin)

    # public methods

    def setup_port(self, bank: Banks, direction: Directions, pud: PullUp):
        """
        setup a whole bank of ports as either input or output
        :param bank: Bank to setup
        :param direction: desired direction of all ports
        :param pud: desired pullup mode
        :return: None
        """
        if bank == Banks.A:
            io_dir_reg = Registers.IODIRA
            pud_reg = Registers.GPPUA
            for i in range(8):
                self._io_lookup[i] = direction
        else:
            io_dir_reg = Registers.IODIRB
            pud_reg = Registers.GPPUB
            for i in range(8, 16):
                self._io_lookup[i] = direction

        iodir_val = 0xFF if direction == Directions.INPUT else 0x00
        pud_val = 0xFF if pud == PullUp.ENABLED else 0x00

        self._i2c_write(io_dir_reg, iodir_val)
        self._i2c_write(pud_reg, pud_val)

        if self.int_en:
            self._enable_interrupts()

    def read_port(self, bank: Banks) -> int:
        """
        reads one port of the IO expander (either A or B)
        :param bank: enum value Banks.A or Banks.B
        :return: byte
        """
        if bank == Banks.A:
            reg = Registers.GPIOA
        else:
            reg = Registers.GPIOB

        return self._i2c_read(reg)

    def write_port(self, bank: Banks, state: bool):
        """
        sets the output of one whole port
        :param bank: A or B bank
        :param state: True or False
        :return: None
        """
        if bank == Banks.A:
            reg = Registers.GPIOA
        else:
            reg = Registers.GPIOB

        val = 0
        if state:
            val = 0b11111111

        self._i2c_write(reg, val)

    def setup_pin(self, pin_num, direction: Directions, pud: PullUp):
        """
        setup a whole bank of ports as either input or output
        :param pin_num: Bank to setup
        :param direction: desired direction of all ports
        :param pud: desired pullup mode
        :return: None
        """

        bank = MCP23017.get_bank_of_pin(pin_num)
        if bank == Banks.A:
            iodir_reg = Registers.IODIRA
            pud_reg = Registers.GPPUA
        else:
            iodir_reg = Registers.IODIRB
            pud_reg = Registers.GPPUB

        iodir_val = self._i2c_read(iodir_reg)
        pud_val = self._i2c_read(pud_reg)

        _, mask = MCP23017.pin_to_register(pin_num)

        if direction == direction.INPUT:
            iodir_val |= (1 << (pin_num % 8))
            self._io_lookup[pin_num] = Directions.INPUT

            if pud == PullUp.ENABLED:
                pud_val |= (1 << (pin_num % 8))
            else:
                pud_val &= (~(1 << (pin_num % 8)))
            self._i2c_write(pud_reg, pud_val)
        else:
            iodir_val &= (~(1 << (pin_num % 8)))  # invert prior bitmask to and out the according bit
            self._io_lookup[pin_num] = Directions.OUTPUT

        self._i2c_write(iodir_reg, iodir_val)

        if self.int_en:
            self._enable_interrupts()

    def read_pin(self, pin_num: int) -> bool:
        """
        reads the status of one pin
        :param pin_num: pin to read out
        :return: state of the pin
        """
        reg, mask = MCP23017.pin_to_register(pin_num)
        data = self._i2c_read(reg)
        return (data & mask) >= 1

    def write_pin(self, pin_num: int, state: bool):
        """
        sets the state of one output pin
        :param pin_num: pin to switch
        :param state: desired state of the pin
        :return: None
        """
        if self._io_lookup[pin_num] is not Directions.OUTPUT:
            raise ValueError("Pin {} isn't configured as output".format(pin_num))
        port_state = self.read_port(self.get_bank_of_pin(pin_num))
        reg, mask = MCP23017.pin_to_register(pin_num)
        if state:
            # pin should be switched on
            pin_val = (1 << (pin_num % 8))  # or current state and the new pin together
            self._i2c_write(reg, port_state | pin_val)
        else:
            # pin should be switched off
            pin_val = ~(1 << pin_num % 8)  # effectively wiping the bit of the pin
            self._i2c_write(reg, port_state & pin_val)

    def attach_interrupt(self, pin: int, callback):
        """
        attaches or replaces the callback on one falling edge interrupt event of the given pin
        :param pin: pin to attach the interrupt to
        :param callback: function, callback function, executed when interrupt happens
        :return: None
        """
        if pin not in self._io_lookup:
            raise ValueError("Pin {} is not configured".format(pin))
        if self._io_lookup[pin] is not Directions.INPUT:
            raise ValueError("can't register interrupts on outputs. Given pin was: {}".format(pin))
        self._int_lookup[pin] = callback

    def detach_interrupt(self, pin: int):
        """
        removes the callback of the given pin if it exists
        :param pin: pin to remove the interrupt from
        :return: None
        """
        if self._int_lookup[pin]:
            del self._int_lookup[pin]

    # internal methods
    def _initialize_interrupts(self):
        """
        setting initial values for interrupt operation
        :return:
        """

        logger.debug("initializing interrupts")
        # setting IOCON
        # mirror INT pins, leave rest as is, INT pin is active low
        io_con = self._i2c_read(Registers.IOCON)
        new_val = io_con | 0b01000000
        self._i2c_write(Registers.IOCON, new_val)

        # setting DEFVAL registers => detect only falling edges
        self._i2c_write(Registers.DEFVALA, 0xFF)
        self._i2c_write(Registers.DEFVALB, 0xFF)

        # set INTOCON to 1 to enable int on pin diff to DEFVAL
        self._i2c_write(Registers.INTCONA, 0xFF)
        self._i2c_write(Registers.INTCONB, 0xFF)

        def callback(*args) -> None:
            """
            callback, executed when the RPi receives an interrupt from the MCP
            :param gpio: int, BCM number of the gpio pin
            :param level: int, 0: falling edge, 1: rising edge, 2: watchdog event
            :return: None
            """
            logger.debug("interrupt from mcp")
            # on an interrupt, since pins are mirrored:
            int_a = self._i2c_read(Registers.INTFA)
            int_b = self._i2c_read(Registers.INTFB)

            if int_a is not 0x00:  # at least one pin is active (active-low)
                # get int source
                logger.debug("interrupt on bank A")
                pin_num = MCP23017.get_active_pin(int_a)

                # execute callback
                if pin_num in self._int_lookup:
                    self._int_lookup[pin_num](pin_num)

                # clear interrupt
                self._clear_int_loop()

            elif int_b is not 0x00:
                # get int source
                logger.debug("interrupt on bank B")
                pin_num = MCP23017.get_active_pin(int_b) + 8

                # execute callback
                if pin_num in self._int_lookup:
                    self._int_lookup[pin_num](pin_num)

                # clear interrupts
                self._clear_int_loop()

        # activate interrupt line and set callback on RPi GPIO
        gpio.add_event_detect(self.int_pin, gpio.FALLING, callback=callback)

        self.int_en = True

    def _enable_interrupts(self):
        """
        recalculates and sets the GPINTEN Registers when changes in IODIR occur
        :return:
        """
        logger.debug("recalculate GPINTEN")
        # setting GPINTEN
        # calculate which pins must be enabled for interrupt operation
        a = 0
        b = 0
        for k, v in self._io_lookup.items():
            if v is Directions.OUTPUT:
                continue
            if 0 <= k < 8:  # A Bank
                a |= (1 << k)
            elif 8 <= k < 16:  # B Bank
                b |= (1 << (k - 8))

        self._i2c_write(Registers.GPINTENA, a)
        self._i2c_write(Registers.GPINTENB, b)

    def _i2c_write(self, reg, val):
        """
        shortcut for writing to i2c bus
        :param reg: Register from registers enum
        :param val: byte
        :return: None
        """
        self._i2c_dev.write_byte_data(self.addr, reg.value, val)

    def _i2c_read(self, reg) -> int:
        """
        shortcut for reading from the i2c bus
        :param reg: Register to read out from the Registers enum
        :return: byte, data of the register
        """
        return self._i2c_dev.read_byte_data(self.addr, reg.value)

    def _clear_int_loop(self):
        """
        loop for reading GPIO registers, until the interrupt is cleared.
        Should be executed in a thread
        :return:
        """
        # make sure threaded callbacks from RPi.GPIO don't clear each other
        # otherwise there might be an uncleared interrupt

        self._int_lock.acquire()
        while not gpio.input(self.int_pin):
            self._i2c_read(Registers.GPIOA)
            self._i2c_read(Registers.GPIOB)
            time.sleep(5e-3)
        self._int_lock.release()
