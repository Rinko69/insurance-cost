from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from insurance_cost.models import (CargoType, InsuranceCost, Rate)
from .filters import InsuranceCostSearchFilter
from .serializers import (CargoTypeSerializer, CostShowSerializer,
                          InsuranceCostSerializer, RateSerializer)


class RateViewSet(ReadOnlyModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RateSerializer


class CargoTypeViewSet(ReadOnlyModelViewSet):
    queryset = CargoType.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CargoTypeSerializer


class InsuranceCostViewSet(ModelViewSet):
    queryset = InsuranceCost.objects.all()
    serializer_class = InsuranceCostSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = InsuranceCostSearchFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CostShowSerializer
        return InsuranceCostSerializer
    
    @action(detail=False, methods=['get'],
            permission_classes=[AllowAny])
    def get_insurance_cost(self, request):
        rates = InsuranceCost.objects.filter(
            cargo_type__costs__rate=request.rate).values_list(
            'cost', 'rate__rate', 'date'
        )
        costs = InsuranceCost.objects.filter(
            cargo_type__costs__cost=request.cost).values_list(
            'rate', 'cost__cost', 'date'
        )
        response = rates['rate']*costs['cost']
        return response
