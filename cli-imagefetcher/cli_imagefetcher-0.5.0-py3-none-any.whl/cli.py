import typer, json, sys, os
from .validation import validateArguments
from .search import dataApiSearch
from .order import orderApiRequest
from .imageManipulation import clipImages

app = typer.Typer(add_completion=False)


@app.command("search")
def requestArguments(
    apikey: str = typer.Argument(..., help="API Key: XXXX-XXXX-XXXX-XXXX"),
    toi: str = typer.Argument(
        ..., help="Time range of interest: YYYY-MM-DD, YYYY-MM-DD"
    ),
    aoi: str = typer.Argument(..., help="Path to the AOI geojson"),
):
    """
    API search for items matching an area & time range of interest.
    """
    try:
        welcomeMessage = typer.style(
            "cli-imagefetcher search tool", fg=typer.colors.BRIGHT_YELLOW
        )
        typer.echo(welcomeMessage)

        # Application Loop
        ## Validation
        with open(aoi, "r") as f:
            aoiJson = json.load(f)
        validated = validateArguments(apikey, toi, aoiJson)

        if validated["status"] == False:
            raise Exception(validated["message"])
        ## Search Data API
        featureIdArray = dataApiSearch(apikey, toi, aoiJson)
        ## Download from Order API
        itemPathsArray = orderApiRequest(apikey, featureIdArray)
        ## TODO: clip image
        # modifiedImagePath = clipImages(itemPathsArray)
        modifiedImagePath = itemPathsArray
        # ReRun or Terminated Session
        typer.echo(f"Completed Order Location: {modifiedImagePath}")
        response = str(typer.prompt("Would you like to search again? y/n"))
        if response.lower() == "y":
            # TODO: loop by asking for user input.
            pass
        else:
            endMessage = typer.style(
                "cli-imagefetcher Terminated.", fg=typer.colors.YELLOW
            )
            typer.echo(endMessage)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_message = typer.style(
            f"Error: {e} - {exc_type, fname, exc_tb.tb_lineno}",
            fg=typer.colors.RED,
        )
        typer.echo(error_message)


@app.command("api-docs")
def openDocs():
    """
    Open the API documentation in a web browser.
    """
    typer.echo("Opening API Help Documentation...")
    typer.launch("https://developers.planet.com/docs")


def main():
    app(prog_name="cli-imagefetcher")
