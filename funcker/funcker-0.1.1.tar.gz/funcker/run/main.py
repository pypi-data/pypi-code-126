import docker
import json
import os


class Funcker:
    def __init__(self, namespace, name, version="latest"):
        self.namespace = namespace
        self.name = name
        self.version = version
        self.image = f"{namespace}/{name}:{version}"

    def run(self, *args):
        client = docker.from_env()
        serialized_args = [json.dumps(arg) for arg in args]
        res = client.containers.run(
            name=self.name,
            image=self.image,
            command=serialized_args,
            remove=True,
            volumes={os.getcwd(): {
                'bind': f"/tmp/{self.name}", 'mode': 'rw'}
            }
        ).decode()

        return json.loads(res)
