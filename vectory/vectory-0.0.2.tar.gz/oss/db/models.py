import datetime
import os

from peewee import Model, CharField, DateTimeField, IntegerField
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField, ForeignKeyField


db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.db")

database = SqliteExtDatabase(
    db_path,
    pragmas={
        "journal_mode": "off",
        "synchronous": 0,
        "cache_size": -1 * 100000,  # 64MB
        "locking_mode": "exclusive",
        "temp_store": "memory",
        "foreign_keys": 1,
    },
)


class BaseModel(Model):
    class Meta:
        database = database


class Dataset(BaseModel):
    name = CharField(unique=True)
    created = DateTimeField(default=datetime.datetime.now)
    csv_path = CharField()
    id_field = CharField()

    def __str__(self):
        return self.name


class Experiment(BaseModel):
    name = CharField(unique=True)
    model = CharField()
    created = DateTimeField(default=datetime.datetime.now)
    params = JSONField()
    train_dataset = ForeignKeyField(
        Dataset, backref="experiments", on_delete="CASCADE", on_update="CASCADE"
    )

    def __str__(self):
        return self.name


class EmbeddingSpace(BaseModel):
    name = CharField(unique=True)
    created = DateTimeField(default=datetime.datetime.now)
    npz_path = CharField()
    dims = IntegerField()
    experiment = ForeignKeyField(
        Experiment,
        backref="embedding_spaces",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    dataset = ForeignKeyField(
        Dataset, backref="embedding_spaces", on_delete="CASCADE", on_update="CASCADE"
    )

    def __str__(self):
        return self.name


class ElasticSearchIndex(BaseModel):
    name = CharField(unique=True)
    embedding_space = ForeignKeyField(
        EmbeddingSpace,
        backref="elasticsearch_indices",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    model = CharField()
    similarity = CharField(null=True)
    num_threads = IntegerField()
    chunk_size = IntegerField()
    k = IntegerField(null=True)
    L = IntegerField(null=True)
    w = IntegerField(null=True)
    number_of_shards = IntegerField()

    def __str__(self):
        return self.name


class KNNBulkRelationship(BaseModel):
    embedding_space = ForeignKeyField(
        EmbeddingSpace,
        backref="knn_bulk_relationships",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    metric = CharField()

    class Meta:
        indexes = ((("embedding_space", "metric"), True),)


class KNNBulkStorage(BaseModel):
    relationship = ForeignKeyField(
        KNNBulkRelationship,
        backref="knn_bulk_storage",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    created = DateTimeField(default=datetime.datetime.now)
    npz_index = IntegerField()
    k_1 = IntegerField()
    k_2 = IntegerField()
    k_3 = IntegerField()
    k_4 = IntegerField()
    k_5 = IntegerField()
    k_6 = IntegerField()
    k_7 = IntegerField()
    k_8 = IntegerField()
    k_9 = IntegerField()
    k_10 = IntegerField()

    @staticmethod
    def get_knn(embedding_space_name: str, metric: str):
        return (
            KNNBulkStorage.select(
                KNNBulkStorage.k_1,
                KNNBulkStorage.k_2,
                KNNBulkStorage.k_3,
                KNNBulkStorage.k_4,
                KNNBulkStorage.k_5,
                KNNBulkStorage.k_6,
                KNNBulkStorage.k_7,
                KNNBulkStorage.k_8,
                KNNBulkStorage.k_9,
                KNNBulkStorage.k_10,
            )
            .join(KNNBulkRelationship)
            .where(KNNBulkRelationship.metric == metric)
            .join(EmbeddingSpace)
            .where(EmbeddingSpace.name == embedding_space_name)
            .order_by(KNNBulkStorage.npz_index)
        )


def create_tables():
    with database:
        database.create_tables(
            [
                Experiment,
                Dataset,
                EmbeddingSpace,
                ElasticSearchIndex,
                KNNBulkRelationship,
                KNNBulkStorage,
            ]
        )


def get_database():
    return database
