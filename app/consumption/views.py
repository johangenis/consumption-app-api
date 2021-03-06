from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Consumption_type, Consumption_record

from consumption import serializers


class BaseConsumptionAttrViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """Base viewset for user owned consumption records attributes"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by(
            "-cons_type"
        )

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class Consumption_typeViewSet(BaseConsumptionAttrViewSet):
    """Manage consumption types in the database"""

    queryset = Consumption_type.objects.all()
    serializer_class = serializers.Consumption_typeSerializer


class Consumption_recordViewSet(viewsets.ModelViewSet):
    """Manage consumption records in the database"""

    serializer_class = serializers.Consumption_recordSerializer
    queryset = Consumption_record.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the consumption records for the authenticated user"""
        cons_type = self.request.query_params.get("cons_type")
        queryset = self.queryset
        if cons_type:
            cons_type_ids = self._params_to_ints(cons_type)
            queryset = queryset.filter(cons_type__id__in=cons_type_ids)

        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return serializers.Consumption_recordDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new consumption record"""
        serializer.save(user=self.request.user)
