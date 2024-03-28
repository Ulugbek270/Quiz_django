from django.contrib import admin

from .models import Category, Question, Choice, Profile

admin.site.register(Category)


class SortQuestion(admin.ModelAdmin):
    list_display = ('question', 'get_num_choices', 'modified_at')  # Fields to display in the admin list view
    ordering = ('-modified_at',)  # Sort by modification date in descending order

    def get_num_choices(self, obj):
        return Choice.objects.filter(question=obj).count()

    get_num_choices.short_description = 'Number of Choices'  # Set a custom column header


admin.site.register(Question, SortQuestion)


class SortChoices(admin.ModelAdmin):
    list_display = ('choice', 'question', 'position', 'modified_at')  # Fields to display in the admin list view
    ordering = ('-modified_at',)  # Sort by modification date in descending order


admin.site.register(Choice, SortChoices)


class SortProfiles(admin.ModelAdmin):
    list_display = ('user', 'points', 'modified_at')  # Fields to display in the admin list view
    ordering = ('-points',)  # Sort by modification date in descending order


admin.site.register(Profile, SortProfiles)
