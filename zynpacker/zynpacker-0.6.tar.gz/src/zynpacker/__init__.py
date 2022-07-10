from . import agent

class packer:
    def __init__(self, *args):
        pass

    def pack(self):
        print('Starting prep!\nNOTE: This process can take up to one minute.\nIt is NOT stalled/broken.')
        agent.stabilizeTicks()