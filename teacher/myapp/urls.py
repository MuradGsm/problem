from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_category/", views.add_category, name="add_category"),
    path("list_categories/", views.list_categories, name="list_categories"),
    path(
        "view_category/<int:category_id>/", views.view_category, name="view_category"
    ),  # add view category url
    path("add_teacher/", views.add_teacher, name="add_teacher"),
    path("list_teachers/", views.list_teachers, name="list_teachers"),
    path(
        "view_teacher/<int:teacher_id>/", views.view_teacher, name="view_teacher"
    ),  # add view teacher url
    path("add_problem/", views.add_problem, name="add_problem"),
    path("list_problems/", views.list_problems, name="list_problems"),
    path(
        "view_problem/<int:problem_id>/", views.view_problem, name="view_problem"
    ),  # add view problem url
    path("filter_problems/", views.filter_problems, name="filter_problems"),
    path(
        "delete_problem/<int:problem_id>/", views.delete_problem, name="delete_problem"
    ),  # add delete problem url
    path("problem_statistics/", views.problem_statistics, name="problem_statistics"),
    path("edit_problem/<int:problem_id>/", views.edit_problem, name="edit_problem"),
]
