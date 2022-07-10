import sqlalchemy as sa

from authx_core import GUID, authxBackend


def setup_database(engine: sa.engine.Engine) -> None:
    setup_guids(engine)


def setup_guids(engine: sa.engine.Engine) -> None:
    """
    Set up UUID generation using the uuid-ossp extension for postgres
    """
    database_backend = authxBackend._from_engine(engine)
    if database_backend == authxBackend.postgresql:  # pragma: no cover
        uuid_generation_setup_query = 'create EXTENSION if not EXISTS "pgcrypto"'
        engine.execute(uuid_generation_setup_query)


def setup_database_metadata(metadata: sa.MetaData, engine: sa.engine.Engine) -> None:
    setup_guid_server_defaults(metadata, engine)


def setup_guid_server_defaults(metadata: sa.MetaData, engine: sa.engine.Engine) -> None:
    database_backend = authxBackend._from_engine(engine)

    guid_server_defaults = {
        authxBackend.postgresql: "gen_random_uuid()",
        authxBackend.sqlite: "(lower(hex(randomblob(16))))",
    }
    for table in metadata.tables.values():
        if len(table.primary_key.columns) != 1:
            continue
        for column in table.primary_key.columns:  # pragma: no cover
            if type(column.type) is GUID:
                column.server_default = sa.DefaultClause(
                    sa.text(guid_server_defaults[database_backend])
                )
