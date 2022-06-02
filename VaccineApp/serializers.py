from rest_framework import serializers
from VaccineApp.models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = (
            'HumanId', 'firstName', 'lastName', 'dateOfBirth', 'address', 'City', 'zipCode', 'landLine', 'cellularPhone',
            'infected', 'conditions')
