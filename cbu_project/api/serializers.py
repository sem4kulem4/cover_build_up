from rest_framework import serializers

from .models import Curve


class CurveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curve
        fields = ('unit', 'reach',)
        read_only_fields = ('user',)
