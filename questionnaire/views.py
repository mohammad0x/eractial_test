from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView

from .models import Questionnaire
from .serializers import QuestionnaireSerializer


# TODO: create questionnaire in db
class QuestionnaireListCreateAPI(ListCreateAPIView):
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Questionnaire.objects.filter(user_id=self.request.user)
        else:
            return Questionnaire.objects.none()


# TODO: show user questionnaires by user_id
class UserQuestionnairesViewAPI(ListAPIView):
    pass


# TODO: show single questionnaire by questionnaire id
class QuestionnaireViewAPI(RetrieveAPIView):
    pass
