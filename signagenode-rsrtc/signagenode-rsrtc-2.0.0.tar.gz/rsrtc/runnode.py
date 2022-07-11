#!python

import faulthandler

from ebs.linuxnode.gui.kivy.utils.launcher import prepare_config
from ebs.linuxnode.gui.kivy.utils.launcher import prepare_environment
from ebs.linuxnode.gui.kivy.utils.launcher import prepare_kivy


def run_node():
    nodeconfig = prepare_config('rsrtc')

    prepare_environment(nodeconfig)
    prepare_kivy(nodeconfig)

    from ebs.linuxnode.core import config
    config.current_config = nodeconfig

    from .app import RsrtcApplication

    print("Creating Application : {}".format(RsrtcApplication))
    app = RsrtcApplication(config=nodeconfig)
    app.run()


if __name__ == '__main__':
    print("Starting faulthandler")
    faulthandler.enable()
    run_node()
