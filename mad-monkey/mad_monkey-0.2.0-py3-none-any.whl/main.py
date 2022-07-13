import typer
import os
from rich import print

app = typer.Typer()

@app.command(name="view", help="view content of a file")
def main(path: str):
    try:
        if (os.path.exists(path)):
            file = open(path, "r")
            print(file.read())
        else:
            print(":monkey_face: [bold red]viki! - file not found[/bold red]")
    except Exception:
        print(":monkey_face: [bold red]viki! - Error [/bold red]")


if __name__ == "__main__":
    app()