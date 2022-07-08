import typer
import json
import subprocess

app = typer.Typer()


@app.command()
def build(path):
    with open(f"{path}/manifest.json", 'r') as file:
        manifest = json.load(file)
        namespace = manifest["namespace"]
        name = manifest["name"]
        version = manifest["version"]
        subprocess.run(
            f"docker build -t {namespace}/{name}:{version} {path}".split(" ")
        )


@app.command()
def help():
    typer.echo("build and push funcker function")
