import django.db
import django.db.backends.base.base

import django_clickhouse_engine.client
import django_clickhouse_engine.creation
import django_clickhouse_engine.features
import django_clickhouse_engine.introspection
import django_clickhouse_engine.operations


class DatabaseWrapper(django.db.backends.base.base.BaseDatabaseWrapper):
    client_class = django_clickhouse_engine.client.DatabaseClient
    creation_class = django_clickhouse_engine.creation.DatabaseCreation
    features_class = django_clickhouse_engine.features.DatabaseFeatures
    introspection_class = django_clickhouse_engine.introspection.DatabaseIntrospection
    ops_class = django_clickhouse_engine.operations.DatabaseOperations

    class Database:
        DataError = django.db.DataError
        OperationalError = django.db.OperationalError
        IntegrityError = django.db.IntegrityError
        InternalError = django.db.InternalError
        ProgrammingError = django.db.ProgrammingError
        NotSupportedError = django.db.NotSupportedError
        DatabaseError = django.db.DatabaseError
        InterfaceError = django.db.InterfaceError
        Error = django.db.Error
