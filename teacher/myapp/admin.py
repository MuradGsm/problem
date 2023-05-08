from django.contrib import admin
from .models import Category, Problem, Teacher


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "info")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "info")


class ProblemAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "solved", "created_at", "category")
    list_filter = ("solved", "created_at", "category")
    search_fields = ("name",)
    actions = ["mark_solved"]

    def mark_solved(self, request, queryset):
        queryset.update(solved=True)
        self.message_user(request, "Selected problems have been marked as solved.")

    mark_solved.short_description = "Mark selected problems as solved"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Problem, ProblemAdmin)
