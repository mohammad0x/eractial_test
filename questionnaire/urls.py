from django.urls import path
from .views import *
urlpatterns = [
    path('questionnaire', QuestionnaireListCreateAPI.as_view()),
    path('questionnare/<user_id:int>', UserQuestionnairesViewAPI.as_view()),
    path('questionnare/<id:int>', QuestionnairesViewAPI.as_view())
]