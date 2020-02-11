from rest_framework import serializers

from core.models import Consumption_type


class Consumption_typeSerializer(serializers.ModelSerializer):
    """Serializer for consumption type object"""

    class Meta:
        model = Consumption_type
        fields = ("id", "cons_type")
        read_only_Fields = ("id",)
