import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import typer

import oss.oss.main as vectory
from oss.db.models import ElasticSearchIndex, EmbeddingSpace
from oss.es.api import Mapping, Vec
from oss.es.client import ElastiKNNClient
from oss.es.utils import load_csv_with_headers, load_embeddings_from_numpy

app = typer.Typer()


@app.command()
def load(
    index_name: str = typer.Argument(
        ..., help="Name of the index to load embeddings into"
    ),
    embedding_space_name: str = typer.Argument(
        ..., help="Name of the embedding space to load"
    ),
    model: str = typer.Option(
        "lsh", help="Model to use for embedding kNN search [lsh, exact]:"
    ),
    similarity: str = typer.Option(
        "cosine", help="Similarity function to use for kNN search [cosine, l2]:"
    ),
    num_threads: int = typer.Option(
        4, "--num-threads", "-t", help="Number of threads to use"
    ),
    chunk_size: int = typer.Option(1000, "--chunk-size", "-c", help="Chunk size"),
    k: int = typer.Option(1, "-k", help="Hyperparameter for kNN search"),
    L: int = typer.Option(
        99, "-L", help="Hyperparameter for kNN search with 'lsh' model"
    ),
    w: int = typer.Option(
        3, "-w", help="Hyperparameter for kNN search with l2 smililarity"
    ),
    number_of_shards: int = typer.Option(
        1, "--num-shards", "-n", help="Number of shards to use"
    ),
) -> None:
    es = ElastiKNNClient()

    if index_name in es.list_indices():
        typer.echo(f"Error: {index_name} is already loaded")
        es.close()
        raise typer.Abort()

    try:
        embedding_space = EmbeddingSpace.get(name=embedding_space_name)
    except EmbeddingSpace.DoesNotExist:
        typer.echo(f"Error: {embedding_space_name} is not an embedding space")
        es.close()
        raise typer.Abort()
    if model == "lsh":
        if similarity == "cosine":
            mapping = Mapping.CosineLsh(dims=embedding_space.dims, L=L, k=k)
        elif similarity == "l2":
            mapping = Mapping.L2Lsh(dims=embedding_space.dims, L=L, k=k, w=w)
        else:
            typer.echo(f"Invalid similarity {similarity}, try cosine or l2")
            raise typer.Abort()
    elif model == "exact":
        mapping = Mapping.DenseFloat(dims=embedding_space.dims)
    else:
        typer.echo(f"Invalid model {model}, try lsh or exact")
        es.close()
        raise typer.Abort()
    successes = vectory.load_index(
        index_name=index_name,
        embedding_space_name=embedding_space_name,
        mapping=mapping,
        chunk_size=chunk_size,
        num_threads=num_threads,
    )

    typer.echo(f"Finished loading {successes} embeddings!")


@app.command()
def load_interactive(
    num_threads: int = typer.Option(
        4, "--num-threads", "-t", help="Number of threads to use"
    ),
    chunk_size: int = typer.Option(1000, "--chunk-size", "-c", help="Chunk size"),
    number_of_shards: int = typer.Option(
        1, "--num-shards", "-n", help="Number of shards to use"
    ),
    k: int = typer.Option(1, "-k", help="Hyperparameter for kNN search"),
    L: int = typer.Option(
        99, "-L", help="Hyperparameter for kNN search with 'lsh' model"
    ),
    w: int = typer.Option(
        3, "-w", help="Hyperparameter for kNN search with l2 smililarity"
    ),
) -> None:

    es = ElastiKNNClient()

    index_name = typer.prompt("Index name")
    if index_name in es.list_indices():
        typer.echo(f"Error: {index_name} is already loaded")
        es.close()
        raise typer.Abort()

    embedding_space_name = typer.prompt("Name of the embedding space to load into ES")

    embedding_space = EmbeddingSpace.get(name=embedding_space_name)

    embeddings = load_embeddings_from_numpy(embedding_space.npz_path)
    rows, header_mapping, header = load_csv_with_headers(
        embedding_space.dataset.csv_path
    )
    typer.echo(f"Loaded {len(rows)} rows with header: {header}")

    model = typer.prompt("Model to use for embedding kNN search [lsh, exact]")

    if model not in ["lsh", "exact"]:
        typer.echo(f"Invalid model {model}, try lsh or exact")
        es.close()
        raise typer.Abort()

    if model == "lsh":
        similarity = typer.prompt(
            "Similarity function to use for kNN search [cosine, l2]"
        )
        if similarity == "cosine":
            mapping = Mapping.CosineLsh(dims=embedding_space.dims, L=L, k=k)
        elif similarity == "l2":
            mapping = Mapping.L2Lsh(dims=embedding_space.dims, L=L, k=k, w=w)
        else:
            typer.echo(f"Invalid similarity {similarity}, try cosine or l2")
            es.close()
            raise typer.Abort()
    elif model == "exact":
        mapping = Mapping.DenseFloat(dims=embedding_space.dims)

    vecs = []
    for embedding in embeddings:
        vecs.append(Vec.DenseFloat(list(embedding)))

    if len(rows) != len(vecs):
        typer.echo(
            "Error: number of rows in csv file doesn't match the number of embeddings"
            "in npz file"
        )
        es.close()
        raise typer.Abort()

    response = es.create_index(
        index_name=index_name,
        mapping=mapping,
        header_mapping=header_mapping,
        number_of_shards=number_of_shards,
    )

    if not response["acknowledged"]:
        typer.echo("An error occurred while creating the index.")
        es.close()
        raise typer.Abort()

    try:
        successes = es.index(
            index=index_name,
            vecs=vecs,
            metadata=rows,
            id_field=embedding_space.dataset.id_field,
            num_threads=num_threads,
            chunk_size=chunk_size,
        )
    except Exception as e:
        typer.echo(e)
        es.delete_index(index_name=index_name)
        raise typer.Abort()

    es.close()

    try:
        assert successes == len(rows)
    except AssertionError:
        vectory.delete_index(index_name=index_name)

    ElasticSearchIndex.create(
        name=index_name,
        embedding_space=embedding_space,
        model=model,
        similarity=similarity,
        num_threads=num_threads,
        chunk_size=chunk_size,
        k=k,
        L=L,
        w=w,
        number_of_shards=number_of_shards,
    )

    typer.echo(f"Finished loading {successes} embeddings!")


@app.command()
def delete_index(
    index_name: str = typer.Argument(..., help="Name of the index to delete"),
):
    result = vectory.delete_index(index_name=index_name)
    typer.echo(f"Index {index_name} deleted")
    typer.echo(result)


@app.command()
def delete_all_indices():
    confirmation = typer.confirm("Are you sure you want to delete all the indices?")

    if not confirmation:
        typer.echo("Not deleting")
        raise typer.Abort()

    es = ElastiKNNClient()
    for index_name in es.list_indices():
        if index_name != ".geoip_databases":
            vectory.delete_index(index_name=index_name)
            typer.echo(f"Index {index_name} deleted")

    typer.echo("All indices deletes!")
    es.close()


@app.command()
def list_indices():
    typer.echo(vectory.list_indices())


@app.command()
def match_query(
    indices_name: list[str] = typer.Argument(
        ..., help="Name of the index to load embeddings into"
    ),
    id: str = typer.Argument(..., help="Value of the id to match with"),
    k: int = typer.Option(10, "-k", help="Number of results to return"),
    fetch_source: bool = typer.Option(
        False, "--fetch", help="Return the `_source` of the document, not only the ID"
    ),
) -> None:

    results = vectory.match_query(
        indices_name=indices_name, query_id=id, k=k, fetch_source=fetch_source
    )
    for index, result in results.items():
        typer.echo(
            "\n +--------------------------------------------------------------------"
            "-----------------------+ \n"
        )
        typer.echo(f"Index: {index} \n")

        for r in result:
            typer.echo(f"index: {r[0]}, score: {r[1]}")
    typer.echo(
        "\n +-------------------------------------------------------------------------"
        "------------------+ \n"
    )


@app.command()
def random_query(
    indices_name: list[str] = typer.Argument(
        ..., help="Name of the index to load embeddings into"
    ),
    k: int = typer.Option(10, "-k", help="Number of results to return"),
    fetch_source: bool = typer.Option(
        False, "--fetch", help="Return the `_source` of the document, not only the ID"
    ),
) -> None:
    results, query_id = vectory.match_query(
        indices_name=indices_name, k=k, random_query=True, fetch_source=fetch_source
    )
    for index, result in results.items():
        typer.echo(
            "\n +--------------------------------------------------------------------"
            "-----------------------+ \n"
        )
        typer.echo(f"Index: {index} \n")

        for r in result:
            typer.echo(f"index: {r[0]}, score: {r[1]}")
    typer.echo(
        "\n +-------------------------------------------------------------------------"
        "------------------+ \n"
    )
