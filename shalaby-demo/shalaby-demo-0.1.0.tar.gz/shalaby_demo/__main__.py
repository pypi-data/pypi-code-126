import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Hi this is my first project uploaded to 
    PyPi by using Typer and Poetry.
    """

@app.command("hi")
def say_hi():
    typer.echo("Hello, World")

@app.command("bye")
def say_bye():
    typer.echo("Goodbye, buddy")

