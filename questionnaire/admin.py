from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum

from .models import Questionnaire


# Register your models here.

class AverageChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(AverageChangeList, self).get_results(*args, **kwargs)
        avg = self.result_list.aggregate(sum=Sum('average'))
        self.average = f"average of all questionnaires is {avg['sum'] / Questionnaire.objects.count()}"


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'confidence', 'penetration', 'intercourse', 'completion', 'satisfaction', 'score')

    def get_changelist(self, request):
        return AverageChangeList

    class Meta:
        model = Questionnaire


admin.site.register(Questionnaire, QuestionnaireAdmin)
