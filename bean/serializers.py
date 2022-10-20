from rest_framework import serializers

from .models import Youtube, Content


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ['id', 'name', 'created_at', 'updated_at']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'name', 'created_at', 'updated_at', 'payment_rate', 'content_quote', 'youtube',
                  'content_approved']


class YoutubeStatsSerializer(serializers.ModelSerializer):
    ordered_content = serializers.IntegerField()
    approved_content = serializers.IntegerField()
    spent = serializers.FloatField()

    class Meta:
        model = Youtube
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
            'ordered_content',
            'approved_content',
            'spent'
        ]
