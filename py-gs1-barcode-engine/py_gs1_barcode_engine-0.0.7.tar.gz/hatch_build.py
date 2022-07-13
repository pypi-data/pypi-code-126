from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def finalize(self,version, build_data, artifact_path) :
        print(version)
        print(build_data)
        print(artifact_path)
        print('finalizing')
        