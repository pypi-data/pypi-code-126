from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer


class ManipulationSerializer(ModelSerializer):
    inserted_at: DateTimeField = DateTimeField(read_only=True)
    updated_at: DateTimeField = DateTimeField(read_only=True)

    class Meta:
        fields = ["inserted_at", "updated_at"]
