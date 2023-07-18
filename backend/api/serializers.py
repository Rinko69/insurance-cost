from rest_framework import serializers

from insurance_cost.models import (CargoType, InsuranceCost, Rate)


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
        read_only_fields = '__all__',


class CargoTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CargoType
        fields = '__all__'
        read_only_fields = '__all__',


class InsuranceCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceCost
        fields = '__all__'
        read_only_fields = '__all__',


class CostSummSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceCost
        fields = ('cargo_type', 'rate')


class CostShowSerializer(serializers.ModelSerializer):

    rate = serializers.PrimaryKeyRelatedField(queryset=Rate.objects.all())
    cargo_type = serializers.PrimaryKeyRelatedField(queryset=CargoType.objects.all())

    class Meta:
        model = InsuranceCost
        fields = ('cargo_type', 'rate', 'date', 'cost')

    def validate(self, data):
        cargo_type = data['cargo_type']
        cargo_type_list = []
        for cargo in cargo_type:
            cargo_id = cargo['id']
            if cargo_id in cargo_type_list:
                raise serializers.ValidationError({
                    'cargo_type': 'Вид груза должен быть уникальным!'
                })
            cargo_type_list.append(cargo_id)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return CostSummSerializer(instance, context=context).data
