#Feed Indexer tests [316-000000-043]

#Author: P.P.A. Kotze
#Date: 1/9/2020
#Version: 
#0.1 Initial
#0.2 Update after feedback and correction from HN email dated 1/8/2020
#0.3 Rework scu_get and scu_put to simplify
#0.4 attempt more generic scu_put with either jason payload or simple params, remove payload from feedback function
#0.5 create scu_lib
#0.6 1/10/2020 added load track tables and start table tracking also as debug added 'field' command for old scu


#Import of Python available libraries
import numpy as np
import json


import datetime, pytz

#scu_ip = '10.96.64.10'
# port = '8080'

#define some preselected sensors for recording into a logfile
hn_feed_indexer_sensors=[
'acu.time.act_time_source',
'acu.time.internal_time',
'acu.time.external_ptp',
'acu.general_management_and_controller.state',
'acu.general_management_and_controller.feed_indexer_pos',
'acu.azimuth.state',
'acu.azimuth.p_set',
'acu.azimuth.p_act',
'acu.azimuth.v_act',
'acu.elevation.state',
'acu.elevation.p_set',
'acu.elevation.p_act',
'acu.elevation.v_act',
'acu.feed_indexer.state',
'acu.feed_indexer.p_set',
'acu.feed_indexer.p_shape',
'acu.feed_indexer.p_act',
'acu.feed_indexer.v_shape',
'acu.feed_indexer.v_act',
'acu.feed_indexer.motor_1.actual_velocity',
'acu.feed_indexer.motor_2.actual_velocity',
'acu.feed_indexer.motor_1.actual_torque',
'acu.feed_indexer.motor_2.actual_torque',
'acu.general_management_and_controller.act_power_consum',
'acu.general_management_and_controller.power_factor',
'acu.general_management_and_controller.voltage_phase_1',
'acu.general_management_and_controller.voltage_phase_2',
'acu.general_management_and_controller.voltage_phase_3',
'acu.general_management_and_controller.current_phase_1',
'acu.general_management_and_controller.current_phase_2',
'acu.general_management_and_controller.current_phase_3'
]

#hn_tilt_sensors is equivalent to "Servo performance"
hn_tilt_sensors=[
'acu.time.act_time_source',
'acu.time.internal_time',
'acu.time.external_ptp',
'acu.general_management_and_controller.state',
'acu.general_management_and_controller.feed_indexer_pos',
'acu.azimuth.state',
'acu.azimuth.p_set',
'acu.azimuth.p_act',
'acu.azimuth.v_act',
'acu.elevation.state',
'acu.elevation.p_set',
'acu.elevation.p_act',
'acu.elevation.v_act',
'acu.general_management_and_controller.act_power_consum',
'acu.general_management_and_controller.power_factor',
'acu.general_management_and_controller.voltage_phase_1',
'acu.general_management_and_controller.voltage_phase_2',
'acu.general_management_and_controller.voltage_phase_3',
'acu.general_management_and_controller.current_phase_1',
'acu.general_management_and_controller.current_phase_2',
'acu.general_management_and_controller.current_phase_3',
'acu.pointing.act_amb_temp_1',
'acu.pointing.act_amb_temp_2',
'acu.pointing.act_amb_temp_3',
'acu.general_management_and_controller.temp_air_inlet_psc',
'acu.general_management_and_controller.temp_air_outlet_psc',
'acu.pointing.incl_signal_x_raw',
'acu.pointing.incl_signal_x_deg',
'acu.pointing.incl_signal_x_filtered',
'acu.pointing.incl_signal_x_corrected',
'acu.pointing.incl_signal_y_raw',
'acu.pointing.incl_signal_y_deg',
'acu.pointing.incl_signal_y_filtered',
'acu.pointing.incl_signal_y_corrected',
'acu.pointing.incl_temp',
'acu.pointing.incl_corr_val_az',
'acu.pointing.incl_corr_val_el'
]


# mocks the SCU api to a degree as needed for developing

import json


import time
import astropy

import datetime

from mke_sculib.mock_telescope import Telescope
import mke_sculib.scu as scu




def get_routes(telescope: Telescope) -> dict:
    dc_routes_get = {
        '/datalogging/currentState': lambda args: telescope.datalogging_currentState(*args),
        '/devices/statusValue': lambda args: telescope.devices_statusValue(args),
        '/datalogging/lastSession': lambda args: telescope.datalogging_lastSession(*args),
        '/datalogging/exportSession': lambda args: telescope.datalogging_exportSession(args),
        '/datalogging/sessions': lambda args: telescope.datalogging_sessions(*args),
    }
    dc_routes_put = {
        '/devices/command': lambda payload, params, data: telescope.devices_command(payload),
        '/datalogging/start': lambda payload, params, data: telescope.datalogging_start(*params),
        '/datalogging/stop': lambda payload, params, data: telescope.datalogging_stop(*params),
        '/acuska/programTrack': lambda payload, params, data: telescope.program_track(data),
    }
    return dict(GET=dc_routes_get, PUT=dc_routes_put)


class MockRequest():
    def __init__(self, url, body) -> None:
        self.url = url
        self.body = body


class MockResponseObject():
    def __init__(self, url, status_code:int, content) -> None:
        self.status_code = status_code
        self._content = content
        self.reason = 'I am a teapod!'
        self.request = MockRequest(url, content)

    def json(self):
        if not isinstance(self._content, str):
            return self._content
        else:
            return json.loads(self._content)

    @property
    def text(self):
        return str(self._content)



class scu_sim(scu.scu):
    def __init__(self, ip='localhost', port='8080', use_realtime=False, debug=True, speedup_factor=1, t_start = astropy.time.Time.now(), UPDATE_INTERVAL = .2):

        self.dc = {}

        self.t_start = t_start.datetime
        self.history = {}
        
        self.t_elapsed = 0

        self.telescope = Telescope( speedup_factor = speedup_factor, 
                                    t_start = t_start, 
                                    use_realtime = use_realtime, 
                                    UPDATE_INTERVAL = UPDATE_INTERVAL, 
                                    do_write_history=True)        

        self.routes = get_routes(self.telescope)


        scu.scu.__init__(self, ip=ip, port=port, debug=debug)


    #	def scu_get(device, params = {}, r_ip = self.ip, r_port = port):
    def scu_get(self, device, params = {}):
        '''This is a generic GET command into http: scu port + folder 
        with params=payload (OVERWRITTEN FOR SIMULATION!)'''
        URL = 'http://' + self.ip + ':' + self.port + device

        if device not in self.routes['GET']:
            r = MockResponseObject(URL, 404, {})
        else:
            fun = self.routes['GET'][device]
            res = fun(params)
            r = MockResponseObject(URL, res['status'], res['body'])

        self.feedback(r)

        return(r)

    def scu_put(self, device, payload = {}, params = {}, data=''):
        '''This is a generic PUT command into http: scu port + folder 
        with json=payload (OVERWRITTEN FOR SIMULATION!)'''
        URL = 'http://' + self.ip + ':' + self.port + device
        if device not in self.routes['PUT']:
            r = MockResponseObject(URL, 404, {})
        else:
            fun = self.routes['PUT'][device]
            res = fun(payload, params, data)
            r = MockResponseObject(URL, res['status'], res['body'])
        self.feedback(r)
        return(r)

    def scu_delete(self, device, payload = {}, params = {}):
        '''This is a generic DELETE command into http: scu port + folder 
        with params=payload (OVERWRITTEN FOR SIMULATION!)'''
        raise NotImplementedError('Not Implemented for a simulator')
        
    #SIMPLE PUTS
    def print_scu(self, *args, **kwargs):
        print('t = {:10.1f}s SCU_SIM: '.format(self.t_elapsed), end='')
        print(*args, **kwargs)
        
    #wait seconds, wait value, wait finalValue
    def wait_duration(self, seconds):
        self.print_scu('wait for {:.1f}s'.format(seconds), end="")
        self.t_elapsed += seconds

        # move until n seconds reached
        ti = 0
        while ti < seconds:
            stepsize = min(seconds - ti, self.telescope.UPDATE_INTERVAL)
            ti += stepsize
            self.telescope.update(stepsize)

        print(' done *')


    def get_history_df(self, interval_ms = None):
        return self.telescope.get_log('history', interval_ms)


if __name__ == '__main__':
   print("main")

        
        
        
