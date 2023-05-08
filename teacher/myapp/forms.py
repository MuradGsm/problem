from django import forms
from .models import Category, Problem, ProblemFilter, Teacher


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "info"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "info": forms.Textarea(attrs={"class": "form-control"}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject", "info"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "info": forms.Textarea(attrs={"class": "form-control"}),
        }


class ProblemFilterForm(forms.ModelForm):
    class Meta:
        model = ProblemFilter
        fields = ["name", "start_date", "end_date", "category", "teacher", "solved"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "teacher": forms.Select(attrs={"class": "form-control"}),
            "solved": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = [
            "name",
            "created_by",
            "solved",
            "measures_taken",
            "category",
            "result",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "created_by": forms.Select(attrs={"class": "form-control"}),
            "solved": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "measures_taken": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "result": forms.Textarea(attrs={"class": "form-control"}),
        }
