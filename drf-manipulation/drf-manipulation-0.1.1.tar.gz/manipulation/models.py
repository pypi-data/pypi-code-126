from django.db.models import DateTimeField


class ManipulationMixinModel:
    inserted_at: DateTimeField = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at: DateTimeField = DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True
