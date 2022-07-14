# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(r'../'))

from hagworm.frame.stress_tests import Launcher, Daemon, Runner, TaskInterface, TimerMS


class Task(TaskInterface):

    async def run(self):

        for index in range(2):

            with TimerMS() as timer:
                await self.sleep(self.randint(123, 456) / 1000)

            if self.randhit([True, False], [50, 50]):
                self.success(f'Test{index}', timer.value)
            else:
                self.failure(f'Test{index}', timer.value)


if __name__ == r'__main__':

    Launcher(daemon=Daemon(2)).run(Runner(Task), times=2, task_num=2)
