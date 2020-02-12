from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Consumption_type, Consumption_record

from consumption import serializers


class Consumption_typeViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """Manage consumption type in the database"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Consumption_type.objects.all()
    serializer_class = serializers.Consumption_typeSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by(
            "-cons_type"
        )

    def perform_create(self, serializer):
        """Create a new consumption type"""
        serializer.save(user=self.request.user)


class Consumption_recordViewSet(viewsets.ModelViewSet):
    """Manage consumption records in the database"""

    serializer_class = serializers.Consumption_recordSerializer
    queryset = Consumption_record.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the consumption records for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return serializers.Consumption_recordDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new consumption record"""
        serializer.save(user=self.request.user)
