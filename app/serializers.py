from rest_framework import serializers

from .models import BigQuery


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = BigQuery
        fields = ['id', 'name']

