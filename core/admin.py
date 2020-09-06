from django.contrib import admin
from .models import Question, Score, Prize


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question',)


@admin.register(Score)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('username', 'score',)


@admin.register(Prize)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount',)
