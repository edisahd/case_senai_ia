from rest_framework import serializers
from prediction.models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('id', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Class')

class PredictionInputSerializer(serializers.Serializer):
    V1 = serializers.FloatField()
    V2 = serializers.FloatField()
    V3 = serializers.FloatField()
    V4 = serializers.FloatField()
    V5 = serializers.FloatField()
    V6 = serializers.FloatField()
    V7 = serializers.FloatField()
    V8 = serializers.FloatField()
    V9 = serializers.FloatField()
    V10 = serializers.FloatField()
    V11 = serializers.FloatField()
    V12 = serializers.FloatField()
    V13 = serializers.FloatField()
    V14 = serializers.FloatField()
    V15 = serializers.FloatField()
    V16 = serializers.FloatField()
    V17 = serializers.FloatField()
    V18 = serializers.FloatField()
    V19 = serializers.FloatField()
    V20 = serializers.FloatField()
    V21 = serializers.FloatField()
    V22 = serializers.FloatField()
    V23 = serializers.FloatField()
    V24 = serializers.FloatField()
    V25 = serializers.FloatField()
    V26 = serializers.FloatField()
    V27 = serializers.FloatField()
    V28 = serializers.FloatField()
    Amount = serializers.FloatField()

class PredictionOutputSerializer(serializers.Serializer):
    Class = serializers.IntegerField()
