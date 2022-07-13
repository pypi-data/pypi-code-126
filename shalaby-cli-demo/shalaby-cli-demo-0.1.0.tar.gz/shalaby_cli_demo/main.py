import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Shalaby-CLI-demo for testing how to build a cli using typer 
    and poetry.
    """


@app.command("hi")
def say_hi(user_name: str = typer.Option(...,help="Add your name so we can great you", prompt=True)):
    if user_name:
        typer.echo(f"Hello, {user_name}.")
    else:
        typer.echo("Hello, buddy.")


@app.command("bye")
def goodbye():
    """
    say goodbye 
    """
    typer.echo("goodbye")

