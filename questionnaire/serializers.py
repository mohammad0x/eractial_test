from .models import Questionnaire
from rest_framework import serializers


class QuestionnaireSerializer(serializers.ModelSerializer):
    alias = serializers.SerializerMethodField()

    class Meta:
        model = Questionnaire
        fields = (
            'user_id', 'confidence', 'penetration', 'intercourse', 'completion', 'satisfaction', 'score', 'average'
        )
        read_only_fields = (
            'created_at'
        )

    def get_alias(self, short_url):
        request = self.context['request']
        hostname = request.META['HTTP_HOST']
        return f'{request.scheme}://{hostname}/r/?id={short_url.short_id}'

    def create(self, validated_data):
        request = self.context['request']
        confidence = request.data['confidence']
        penetration = request.data['penetration']
        intercourse = request.data['intercourse']
        completion = request.data['completion']
        satisfaction = request.data['satisfaction']
        score = confidence + penetration + intercourse + completion + satisfaction,
        average = (confidence + penetration + intercourse + completion + satisfaction) / 5,
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        return Questionnaire.objects.create(
            user_id=user,
            average=average,
            score=score,
            **validated_data,
        )
