from rest_framework import serializers

from core.models import Consumption_type, Consumption_record


class Consumption_typeSerializer(serializers.ModelSerializer):
    """Serializer for consumption type object"""

    class Meta:
        model = Consumption_type
        fields = ("id", "cons_type")
        read_only_Fields = ("id",)


class Consumption_recordSerializer(serializers.ModelSerializer):
    """Serialize a consumption record"""

    consumption_types = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Consumption_type.objects.all()
    )

    class Meta:
        model = Consumption_record
        fields = (
            "id",
            "cons_type",
            "date_time",
            "amount",
        )
        read_only_fields = ("id",)
