from rest_framework import serializers
from .models import employees, CHAMBRE
from .models import reservation
from .models import CHAMBREDEP
from .models import CHAMBREARR
from .models import CHAMBREHORS
from .models import client


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'


class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'


class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = '__all__'


class CHAMBREDEPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHAMBREDEP
        fields = '__all__'


class CHAMBREARRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHAMBREARR
        fields = '__all__'


class CHAMBREHORSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHAMBREHORS
        fields = '__all__'


class CHAMBRESerializer(serializers.ModelSerializer):
    class Meta:
        model = CHAMBRE
        fields = '__all__'
