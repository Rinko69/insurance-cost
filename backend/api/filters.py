import django_filters as filters
from insurance_cost.models import InsuranceCost


class InsuranceCostSearchFilter(filters.FilterSet):
    date = filters.NumberFilter(field_name='date')
    cargo_type = filters.CharFilter(field_name='cargo_type', lookup_expr='icontains')

    class Meta:
        model = InsuranceCost
        fields = ('cargo_type', 'date',)