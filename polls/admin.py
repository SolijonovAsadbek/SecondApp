from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question_text', 'pub_date', 'was_published_recently']
    list_display_links = ['question_text']
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    inlines = [ChoiceInline]
    date_hierarchy = 'pub_date'


# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['choice_text', 'votes']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
