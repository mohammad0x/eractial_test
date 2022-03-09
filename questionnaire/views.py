from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Questionnaire
from .serializers import QuestionnaireSerializer


# TODO: create questionnaire in db
class QuestionnaireListCreateAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Questionnaire.objects.filter(user_id=self.request.user)
        else:
            return Questionnaire.objects.none()


# TODO: show user questionnaires by user_id
class UserQuestionnairesViewAPI(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionnaireSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        user = self.request.user.id
        queryset = self.model.objects.filter(user=user)
        return queryset.order_by('-created_at')


# TODO: show single questionnaire by questionnaire id
class QuestionnaireViewAPI(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
