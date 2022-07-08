import json
import os
import random
import sys

import peewee
from pyexpat import model

from oss.oss import main as vectory
from oss.oss.exceptions import (
    CreatingIndexError,
    DimensionsDismatchError,
    IDFieldNotUnique,
    IsNotAColumnError,
    OperationNotAllowedError,
    RecursiveOperationNotAllowedError,
)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
import typer

import oss.cli.embeddings as embeddings
from oss.db.models import (
    Dataset,
    ElasticSearchIndex,
    EmbeddingSpace,
    Experiment,
    create_tables,
    KNNBulkRelationship,
)
from oss.es.utils import load_csv_with_headers

app = typer.Typer()
app.add_typer(embeddings.app, name="embeddings")


valid_add_completion_items = [
    (
        "experiment",
        "Add an experiment to the database, "
        "this represents a trained model with a certian database and parameters",
    ),
    (
        "dataset",
        "Add a dataset to the database. \n"
        "This represents an csv file with headers that contain the labels or metadata "
        "of the embeddings. Eeach row should coincide with the embedding in the "
        "2D matrix from the embedding space",
    ),
    (
        "embedding_space",
        "Add an embedding space to the database, this should be a 2D matrix saved as "
        "a npz file",
    ),
]


def complete_object(incomplete: str):
    for name, help_text in valid_add_completion_items:
        if name.startswith(incomplete):
            yield (name, help_text)


@app.command()
def add(
    object: str = typer.Argument(
        ...,
        help="Object to register onto the local database, can be either: \n"
        "experiment, dataset or embedding_space",
        autocompletion=complete_object,
    ),
    name: str = typer.Option(None, help="Name of the object to create"),
    csv_path: str = typer.Option(
        None, help="Path to the csv file when adding a dataset"
    ),
    id_field: str = typer.Option(
        "_idx",
        help="Name of the field to use as id for elasticsearch index. If none given, random ids will be generated with the name '_idx'",
    ),
    dataset: str = typer.Option(
        None,
        help="When adding an experiment: "
        "Name of the train dataset used for the experiment \n"
        "When adding an embedding space: "
        "Name of the dataset to to generate the embedding space from",
    ),
    model: str = typer.Option(None, help="Name of the model used for an experiment"),
    params: str = typer.Option(
        None, help="Parameters used for a trained experiment, in json format"
    ),
    params_path: str = typer.Option(
        None, help="Path to json with parameters used for a trained experiment"
    ),
    experiment: str = typer.Option(
        None, help="Name of the experiment used to generate an embedding space"
    ),
    npz_path: str = typer.Option(
        None, help="Path to the npz file to load embeddings to an embedding space"
    ),
    dims: int = typer.Option(None, help="Number of dimensions in the embedding space"),
):
    """
    Register new datasets, experiments or embedding spaces in the database.
    """
    create_tables()

    if object == "dataset":

        if None in [name, csv_path]:
            typer.echo("Must provide name and csv_path")
            raise typer.Abort()

        try:
            vectory.add_dataset(name, csv_path, id_field)
        except (
            FileNotFoundError,
            IsNotAColumnError,
            IDFieldNotUnique,
            peewee.IntegrityError,
            TypeError,
        ) as e:
            typer.echo(e)
            raise typer.Abort()
        # except FileNotFoundError:
        #     csv_abs_path = os.path.abspath(csv_path)
        #     typer.echo(f"Could not find file {csv_abs_path}")
        #     raise typer.Abort()
        # except IsNotAColumnError:
        #     typer.echo(f"Error: {id_field} is not a columns of the given csv")
        #     raise typer.Abort()
        # except IDFieldNotUnique:
        #     typer.echo("Error: the id field column must have unique values")
        #     raise typer.Abort()
        # except peewee.IntegrityError:
        #     typer.echo(f"Error: {name} is already a dataset")
        #     raise typer.Abort()

    elif object == "experiment":
        if None in [name, dataset, model]:
            typer.echo("Must provide name, dataset_name, model_name and params")
            raise typer.Abort()

        if params is None:
            params = {}

        try:
            vectory.add_experiment(name, dataset, model, params, params_path)
        except (Dataset.DoesNotExist, peewee.IntegrityError, TypeError) as e:
            typer.echo(e)
            raise typer.Abort()

    elif object == "embedding_space":
        if None in [name, experiment, dataset, npz_path, dims]:
            typer.echo(
                "Must provide name, experiment_name, dataset_name, npz_path and dims"
            )
            raise typer.Abort()
        try:
            vectory.add_embedding_space(name, npz_path, dims, experiment, dataset)
        except (
            FileNotFoundError,
            Dataset.DoesNotExist,
            Experiment.DoesNotExist,
            peewee.IntegrityError,
            TypeError,
            ValueError,
        ) as e:
            typer.echo(e)
            raise typer.Abort()

    else:
        typer.echo(
            f"Unknown object {object}, try one of:\n "
            f"- experiment\n - dataset\n - embedding_space"
        )
        raise typer.Abort()


@app.command()
def add_interactive(
    object: str = typer.Argument(
        ...,
        help="Object to register onto the local database, can be either: \n"
        "experiment, dataset or embedding_space",
        autocompletion=complete_object,
    ),
):

    create_tables()

    if object == "dataset":
        name = typer.prompt("Dataset's name")

        csv_path = typer.prompt("Path to csv file")
        csv_abs_path = os.path.abspath(csv_path)
        if not os.path.isfile(csv_abs_path):
            typer.echo(f"Could not find file {csv_abs_path}")
            raise typer.Abort()

        id_field = typer.prompt("id-field", default="_idx")
        rows, _, header = load_csv_with_headers(csv_abs_path, id_field)
        if id_field not in header:
            typer.echo(f"Error: {id_field} is not a columns of the given csv")
            raise typer.Abort()
        ids = []
        for row in rows:
            ids.append(row[id_field])
        if len(ids) != len(set(ids)):
            typer.echo("Error: the id field column must have unique values")
            raise typer.Abort()

        Dataset.create(name=name, csv_path=csv_abs_path, id_field=id_field)

    elif object == "experiment":
        name = typer.prompt("Experiment's name")

        dataset_name = typer.prompt("Dataset name")
        try:
            dataset = Dataset.get(name=dataset_name)
        except Dataset.DoesNotExist:
            typer.echo(f"{dataset_name} is not a Dataset")
            raise typer.Abort()

        model_name = typer.prompt("Name of the model used")

        params = typer.prompt("Experiment's parameters (in json format)")
        params_json = json.loads(params)

        Experiment.create(
            name=name, model=model_name, train_dataset=dataset, params=params_json
        )

    elif object == "embedding_space":
        name = typer.prompt("Embedding space's name")

        experiment_name = typer.prompt(
            "Experiment's name that was used to generate this embedding"
        )
        try:
            experiment = Experiment.get(name=experiment_name)
        except Experiment.DoesNotExist:
            typer.echo(f"{experiment_name} is not an Experiment")
            raise typer.Abort()

        dataset_name = typer.prompt(
            "Name of the dataset that was used to generate this embeddings"
        )
        try:
            dataset = Dataset.get(name=dataset_name)
        except Dataset.DoesNotExist:
            typer.echo(f"{dataset_name} is not a Dataset")
            raise typer.Abort()

        npz_path = typer.prompt("Path to npz file")
        npz_abs_path = os.path.abspath(npz_path)

        if not os.path.isfile(npz_abs_path):
            typer.echo(f"Could not find file {npz_abs_path}")
            raise typer.Abort()

        dims = typer.prompt("Dimensions of the embeddings in this space [integer]")

        EmbeddingSpace.create(
            name=name,
            npz_path=npz_abs_path,
            dims=dims,
            experiment=experiment,
            dataset=dataset,
        )

    else:
        typer.echo(
            f"Unknown object {object}, try one of:\n "
            f"- experiment\n - dataset\n - embedding_space"
        )
        raise typer.Abort()


@app.command()
def quick_add(
    name: str = typer.Option(None, help="Name of the embedding_space to create"),
    csv_path: str = typer.Option(None, help="Path to the csv file"),
    npz_path: str = typer.Option(
        None, help="Path to the npz file to load embeddings to the embedding space"
    ),
    dataset_name: str = typer.Option(
        None,
        help="Name of the dataset to generate the embedding space from. If none given, a random name will be generated.",
    ),
    experiment_name: str = typer.Option(None, help="Name of the experiment to create"),
    model_name: str = typer.Option(
        None,
        help="Name of the model used for the experiment. If none given, a random one will be generated.",
    ),
    id_field: str = typer.Option(
        "_idx",
        help="Name of the field to use as id for elasticsearch index. If none given, random ids will be generated with the name '_idx'",
    ),
    params: str = typer.Option(
        None,
        help="Parameters used for a trained experiment, in json format. If none given, this field will remain empty.",
    ),
    params_path: str = typer.Option(
        None, help="Path to json with parameters used for a trained experiment"
    ),
    dims: int = typer.Option(None, help="Number of dimensions in the embedding space"),
):
    if None in [name, csv_path, npz_path, dims]:
        typer.echo("Must provide a name, a csv_path and a npz_path.")
        raise typer.Abort()

    if dataset_name is None:
        dataset_name = "Dataset#" + str(random.randint(1000, 9999))
        while len(Dataset.select().where(Dataset.name == dataset_name)) != 0:
            dataset_name = "Dataset#" + str(random.randint(1000, 9999))

    if experiment_name is None:
        experiment_name = "Experiment" + str(random.randint(1000, 9999))
        while len(Experiment.select().where(Experiment.name == experiment_name)) != 0:
            experiment_name = "Experiment" + str(random.randint(1000, 9999))

    if model_name is None:
        model_name = "Model" + str(random.randint(1000, 9999))

    if params is None:
        params = {}

    try:
        vectory.add_dataset(dataset_name, csv_path, id_field)
    except (
        FileNotFoundError,
        IsNotAColumnError,
        IDFieldNotUnique,
        peewee.IntegrityError,
        TypeError,
    ) as e:
        typer.echo(e)
        raise typer.Abort()

    try:
        vectory.add_experiment(
            experiment_name, dataset_name, model, params, params_path
        )
    except (Dataset.DoesNotExist, peewee.IntegrityError, TypeError) as e:
        vectory.delete_dataset(dataset_name)
        typer.echo(e)
        raise typer.Abort()

    try:
        vectory.add_embedding_space(name, npz_path, dims, experiment_name, dataset_name)
    except (
        FileNotFoundError,
        Dataset.DoesNotExist,
        Experiment.DoesNotExist,
        peewee.IntegrityError,
        TypeError,
        ValueError,
    ) as e:
        vectory.delete_dataset(dataset_name, allow_recursive=True)
        typer.echo(e)
        raise typer.Abort()


@app.command()
def list(
    object: str = typer.Argument(
        ...,
        help="List objects that are registered on the local database, can be either: \n"
        "experiments, datasets or embedding_spaces",
        autocompletion=complete_object,
    ),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Only show names"),
):

    create_tables()

    if object == "datasets":
        query = vectory.get_datasets()
        if len(query) == 0:
            typer.echo("No datasets in the database, try running `oss add dataset`")
            raise typer.Abort()
        if quiet:
            typer.echo("")
            for dataset in query:
                typer.echo(f"{dataset.name}")
            typer.echo("")
        else:
            typer.echo(f"Total results: {len(query)}\n")
            rows = []
            rows.append(["NAME", "CSV PATH", "CREATED TIME", "ID FIELD\n"])
            col_widths = []
            col_widths.append([len(word) for word in rows[0]])
            for dataset in query:
                row = [
                    f"{dataset.name}",
                    f"{dataset.csv_path}",
                    f"{dataset.created.strftime('%Y-%m-%d %H:%M:%S')}",
                    f"{dataset.id_field}",
                ]
                rows.append(row)
                col_widths.append([len(word) for word in row])
            widths = [
                max([b[i] + 2 for b in col_widths]) for i in range(len(col_widths[0]))
            ]
            for row in rows:
                typer.echo(
                    f"{row[0]:{widths[0]}}{row[1]:{widths[1]}}{row[2]:{widths[2]}}{row[3]:{widths[3]}}"
                )
            typer.echo("")

    elif object == "experiments":
        query = Experiment.select()
        if len(query) == 0:
            typer.echo(
                "No experiments in the database, try running `oss add experiment`"
            )
            raise typer.Abort()
        if quiet:
            typer.echo("")
            for experiment in query:
                typer.echo(f"{experiment.name}")
            typer.echo("")

        else:
            typer.echo(f"Total results: {len(query)}\n")
            rows = []
            rows.append(["NAME", "MODEL", "PARAMS", "TRAIN DATASET", "CREATED TIME\n"])
            col_widths = []
            col_widths.append([len(word) for word in rows[0]])
            for experiment in query:
                row = [
                    f"{experiment.name}",
                    f"{experiment.model}",
                    f"{experiment.params}",
                    f"{experiment.train_dataset.name}",
                    f"{experiment.created.strftime('%Y-%m-%d %H:%M:%S')}",
                ]
                rows.append(row)
                col_widths.append([len(word) for word in row])
            widths = [
                max([b[i] + 2 for b in col_widths]) for i in range(len(col_widths[0]))
            ]
            for row in rows:
                typer.echo(
                    f"{row[0]:{widths[0]}}{row[1]:{widths[1]}}{row[2]:{widths[2]}}"
                    f"{row[3]:{widths[3]}}{row[4]:{widths[4]}}"
                )
            typer.echo("")

    elif object == "embedding_spaces":
        query = EmbeddingSpace.select()
        if len(query) == 0:
            typer.echo(
                "No embedding spaces in the database, "
                "try running `oss add embedding_space`"
            )
            raise typer.Abort()
        if quiet:
            typer.echo("")
            for embedding_space in query:
                typer.echo(f"{embedding_space.name}")
            typer.echo("")
        else:
            typer.echo(f"Total results: {len(query)}\n")
            rows = []
            rows.append(
                ["NAME", "NPZ PATH", "EXPERIMENT", "DATASET", "DIMS", "CREATED TIME\n"]
            )
            col_widths = []
            col_widths.append([len(word) for word in rows[0]])
            for embedding_space in query:
                row = [
                    f"{embedding_space.name}",
                    f"{embedding_space.npz_path}",
                    f"{embedding_space.experiment.name}",
                    f"{embedding_space.dataset.name}",
                    f"{embedding_space.dims}",
                    f"{embedding_space.created.strftime('%Y-%m-%d %H:%M:%S')}",
                ]
                rows.append(row)
                col_widths.append([len(word) for word in row])
            widths = [
                max([b[i] + 2 for b in col_widths]) for i in range(len(col_widths[0]))
            ]
            for row in rows:
                typer.echo(
                    f"{row[0]:{widths[0]}}{row[1]:{widths[1]}}{row[2]:{widths[2]}}"
                    f"{row[3]:{widths[3]}}{row[4]:{widths[4]}}{row[5]:{widths[5]}}"
                )
            typer.echo("")

    elif object == "indices":
        query = ElasticSearchIndex.select()
        if len(query) == 0:
            typer.echo("No indices in the database, try running `oss embeddings load`")
            raise typer.Abort()
        if quiet:
            typer.echo("")
            for index in query:
                typer.echo(f"{index.name}")
            typer.echo("")
        else:
            typer.echo(f"Total results: {len(query)}\n")
            rows = []
            rows.append(["NAME", "EMBEDDING SPACE", "MODEL", "SIMILARITY\n"])
            col_widths = []
            col_widths.append([len(word) for word in rows[0]])
            for index in query:
                row = [
                    f"{index.name}",
                    f"{index.embedding_space.name}",
                    f"{index.model}",
                    f"{index.similarity}",
                ]
                rows.append(row)
                col_widths.append([len(word) for word in row])
            widths = [
                max([b[i] + 2 for b in col_widths]) for i in range(len(col_widths[0]))
            ]
            for row in rows:
                typer.echo(
                    f"{row[0]:{widths[0]}}{row[1]:{widths[1]}}{row[2]:{widths[2]}}"
                    f"{row[3]:{widths[3]}}"
                )
            typer.echo("")
    else:

        typer.echo(
            f"Unknown object {object}, try one of:\n "
            f"- experiments\n - datasets\n - embedding_spaces"
        )
        raise typer.Abort()


@app.command()
def delete(
    object: str = typer.Argument(
        ...,
        help="Object to delete from the local database, can be either: \n"
        "experiment, dataset or embedding_space",
        autocompletion=complete_object,
    ),
    object_name: str = typer.Argument(
        ...,
        help="Name of the object",
    ),
    delete_indices: bool = typer.Option(False, "-di"),
    allow_recursive: bool = typer.Option(False, "-r"),
):
    if object == "dataset":
        try:
            deleted_rows = vectory.delete_dataset(
                name=object_name,
                allow_recursive=allow_recursive,
                delete_indices=delete_indices,
            )
        except (RecursiveOperationNotAllowedError, ValueError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} deleted. {deleted_rows} deleted")

    elif object == "experiment":
        try:
            deleted_rows = vectory.delete_experiment(
                name=object_name,
                allow_recursive=allow_recursive,
                delete_indices=delete_indices,
            )
        except (RecursiveOperationNotAllowedError, ValueError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} deleted. {deleted_rows} deleted")

    elif object == "embedding_space":
        try:
            deleted_rows = vectory.delete_embedding_space(
                name=object_name,
                allow_recursive=allow_recursive,
                delete_indices=delete_indices,
            )
        except (RecursiveOperationNotAllowedError, ValueError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} deleted. {deleted_rows} deleted")

    elif object == "index":
        typer.echo("ERROR: To delete an index, use 'vectory embeddings delete-index'")
        typer.Abort()

    else:
        typer.echo(
            f"Unknown object {object}, try one of:\n "
            f"- experiment\n - dataset\n - embedding_space"
        )
        raise typer.Abort()


@app.command()
def edit(
    object: str = typer.Argument(
        ...,
        help="Object to delete from the local database, can be either: \n"
        "experiment, dataset or embedding_space",
        autocompletion=complete_object,
    ),
    object_name: str = typer.Argument(
        ...,
        help="Name of the object",
    ),
    column: str = typer.Argument(
        ...,
        help="Name of the column to be updated",
    ),
    new_value: str = typer.Argument(
        ...,
        help="New value",
    ),
    edit_indices: bool = typer.Option(False, "-ei"),
    allow_recursive: bool = typer.Option(False, "-r"),
):
    if object == "dataset":
        try:
            edited_rows = vectory.edit_dataset(
                name=object_name,
                column=column,
                new_value=new_value,
                allow_recursive=allow_recursive,
                edit_indices=edit_indices,
            )
        except (ValueError, RecursiveOperationNotAllowedError, FileNotFoundError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} edited. {edited_rows} edited")

    elif object == "experiment":
        try:
            edited_rows = vectory.edit_experiment(
                name=object_name,
                column=column,
                new_value=new_value,
                allow_recursive=allow_recursive,
                edit_indices=edit_indices,
            )
        except (ValueError, RecursiveOperationNotAllowedError, FileNotFoundError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} edited. {edited_rows} edited")

    elif object == "embedding_space":
        try:
            edited_rows = vectory.edit_embedding_space(
                name=object_name,
                column=column,
                new_value=new_value,
                edit_indices=edit_indices,
            )
        except (ValueError, RecursiveOperationNotAllowedError, FileNotFoundError) as e:
            typer.echo(e)
            raise typer.Abort()

        typer.echo(f"{object_name} edited. {edited_rows} edited")

    elif object == "index":
        typer.echo(
            "ERROR: Indices cannot be edited. In order to change an index, please"
            "use `oss embeddings delete` and `oss embeddings load`"
        )
        typer.Abort()

    else:
        typer.echo(
            f"Unknown object {object}, try one of:\n "
            f"- experiments\n - datasets\n - embedding_spaces"
        )
        raise typer.Abort()


@app.command()
def compare(
    embedding_space_a: str = typer.Argument(
        ...,
        help="First embedding space to compare",
    ),
    embedding_space_b: str = typer.Argument(
        ...,
        help="Second embedding space to compare",
    ),
    metric_a: str = typer.Option(
        "euclidean",
        "-ma",
        help="Distance metric to use for kNN search in embedding space a",
    ),
    metric_b: str = typer.Option(
        "euclidean",
        "-mb",
        help="Distance metric to use for kNN search in embedding space b",
    ),
    precompute_knn: bool = typer.Option(
        False,
        "---precompute",
        help="Allow precompute knn when calculating jaccard similarity. This operation may be expensive.",
    ),
    calculate_histogram: bool = typer.Option(
        False, "--histogram", help="Calculate similarity histogram"
    ),
):
    try:
        similarity, _, fig, _ = vectory.compare_spaces(
            embedding_space_a=embedding_space_a,
            embedding_space_b=embedding_space_b,
            metric_a=metric_a,
            metric_b=metric_b,
            allow_precompute_knn=precompute_knn,
            histogram=calculate_histogram,
        )
    except KNNBulkRelationship.DoesNotExist:
        typer.echo("Precompute knn not allowed.")
        raise typer.Abort()

    typer.echo(f"The mean of the Jaccard similarity for each query is {similarity}")
    if calculate_histogram:
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    app()
