from .models import Questionnaire
from rest_framework import serializers


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'user', 'confidence', 'penetration', 'intercourse', 'completion', 'satisfaction', 'average', 'score',
            'created_at',
        )
        read_only_fields = (
            'created_at',
            'average',
            'score',
        )

    def create(self, validated_data):
        request = self.context['request']
        confidence = int(request.data['confidence'])
        penetration = int(request.data['penetration'])
        intercourse = int(request.data['intercourse'])
        completion = int(request.data['completion'])
        satisfaction = int(request.data['satisfaction'])
        score = confidence + penetration + intercourse + completion + satisfaction
        average = (confidence + penetration + intercourse + completion + satisfaction) / 5
        if request.user.is_authenticated:
            user = request.user
        else:
            user = 1

        return Questionnaire.objects.create(
            user_id=1,
            average=average,
            score=score,
            **validated_data,
        )
