import os
import shutil

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class HyphenateDistBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'hyphenated-dist-directory'

    def finalize(self, version, build_data, artifact_path):
        self._copy_to_dist_hyphenated(artifact_path)

    def _copy_to_dist_hyphenated(self, artifact_path):
        """Copy the contents in the 'dist' directory, renaming filenames with hyphens instead of underscores.

        > This enables using hyphenated package naming when using pypi.uoregon.edu.

        Args:
            artifact_path (str): The path to the 'dist' directory that will be copied.
        """
        dist_dir = f'{os.path.dirname(artifact_path)}-hyphenated'
        os.makedirs(dist_dir, exist_ok=True)
        dist_filename = os.path.basename(artifact_path)
        dist_filename = dist_filename.replace('_','-')
        new_artifact_path = os.path.join(dist_dir, dist_filename)
        shutil.copyfile(artifact_path, new_artifact_path)
        print(f'Final hyphenated package path: {new_artifact_path}')
