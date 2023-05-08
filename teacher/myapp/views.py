from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Problem, ProblemFilter, Teacher
from .forms import CategoryForm, TeacherForm, ProblemFilterForm, ProblemForm
from django.db.models import Count
from django.core.paginator import Paginator
from django.db.models import Count, Q


def index(request):
    problem_count = Problem.objects.count()
    category_count = Category.objects.count()
    teacher_count = Teacher.objects.count()
    problems = Problem.objects.all()[:10]  # limit to 10 problems
    categories = Category.objects.annotate(
        problem_count=Count("problem")
    )  # get problem count for each category
    context = {
        "problem_count": problem_count,
        "category_count": category_count,
        "teacher_count": teacher_count,
        "problems": problems,
        "categories": categories,
    }
    return render(request, "myapp/index.html", context)


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_categories")
    else:
        form = CategoryForm()
    return render(request, "myapp/add_category.html", {"form": form})


def list_categories(request):
    categories = Category.objects.annotate(
        problem_count=Count("problem"),
        solved_problem_count=Count("problem", filter=Q(problem__solved=True)),
    )
    return render(request, "myapp/list_categories.html", {"categories": categories})


def view_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # get category or 404
    problems = category.problem_set.all()  # get problems for this category
    return render(
        request,
        "myapp/view_category.html",
        {"category": category, "problems": problems},
    )


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_teachers")
    else:
        form = TeacherForm()
    return render(request, "myapp/add_teacher.html", {"form": form})


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "myapp/list_teachers.html", {"teachers": teachers})


def view_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)  # get teacher or 404
    problems = teacher.problem_set.all()  # get problems for this teacher
    return render(
        request, "myapp/view_teacher.html", {"teacher": teacher, "problems": problems}
    )


def add_problem(request):
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_problems")
    else:
        form = ProblemForm()
    return render(request, "myapp/add_problem.html", {"form": form})


def list_problems(request):
    problems = Problem.objects.all()
    paginator = Paginator(problems, 10)  # paginate by 10 problems per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "myapp/list_problems.html", {"page_obj": page_obj})


def view_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)  # get problem or 404
    return render(request, "myapp/view_problem.html", {"problem": problem})


def filter_problems(request):
    if request.method == "POST":
        form = ProblemFilterForm(request.POST)
        if form.is_valid():
            problem_filter = form.save(commit=False)  # create instance of ProblemFilter
            problems = problem_filter.get_problems()  # get filtered problems
            paginator = Paginator(problems, 10)  # paginate by 10 problems per page
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            return render(
                request,
                "myapp/list_problems.html",
                {"page_obj": page_obj},
            )
    else:
        form = ProblemFilterForm()
    return render(request, "myapp/filter_problems.html", {"form": form})


def delete_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)  # get problem or 404
    problem.delete()
    return redirect("list_problems")


def problem_statistics(request):
    problem_count = Problem.objects.count()
    teacher_count = (
        Teacher.objects.filter(problem__isnull=False)
        .annotate(problem_count=Count("problem"))
        .order_by("-problem_count")
    )  # get teachers with at least one problem and order by problem count
    return render(
        request,
        "myapp/problem_statistics.html",
        {"problem_count": problem_count, "teacher_count": teacher_count},
    )


def edit_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect("list_problems")
    else:
        form = ProblemForm(instance=problem)
    return render(request, "myapp/edit_problem.html", {"form": form})
