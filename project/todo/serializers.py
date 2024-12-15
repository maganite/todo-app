from rest_framework import serializers
from .models import *

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def validate(self, attrs):
        for field in self.initial_data.keys():
            if field not in self.fields:
                raise serializers.ValidationError(f"Invalid field: {field}")
        return attrs