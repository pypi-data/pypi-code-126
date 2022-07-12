
from abstract_source_accessor import AbstractSourceAccessor
import subprocess
import os
from log_manager import logging
logger = logging.getLogger('source.DirlinkSourceAccessor')

class DirlinkSourceAccessor(AbstractSourceAccessor):
    """
    Permet de transformer les sources en fichiers recuperables
    La source doit pouvoir etre copie sur une machine
    """
    def __init__(self, name, global_config, source_config):
        """
        Recupere la source si besoin pour la rendre accessible en fichier
        """
        super(DirlinkSourceAccessor, self).__init__(
            name=name,
            global_config=global_config,
            source_config=source_config
        )
        # Attributs specifiques a l'implementation FileSystem
        self.dir_name = os.path.dirname(self.local_path)
        self.readonly = source_config.get('readonly', True)
