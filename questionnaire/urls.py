from django.urls import path
from .views import *
urlpatterns = [
    path('questionnaire/', QuestionnaireListCreateAPI.as_view()),
    path('questionnaires/', UserQuestionnairesViewAPI.as_view()),
    path('questionnaire/<int:id>', QuestionnaireViewAPI.as_view())
]