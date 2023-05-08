from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    solved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    measures_taken = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    result = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("problem_detail", args=[str(self.id)])


class ProblemFilter(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True
    )
    solved = models.BooleanField(blank=True, null=True)

    def get_problems(self):
        problems = Problem.objects.all()
        if self.name:
            problems = problems.filter(name__icontains=self.name)
        if self.start_date:
            problems = problems.filter(created_at__gte=self.start_date)
        if self.end_date:
            problems = problems.filter(created_at__lte=self.end_date)
        if self.category:
            problems = problems.filter(category=self.category)
        if self.teacher:
            problems = problems.filter(created_by=self.teacher)
        if self.solved is not None:
            problems = problems.filter(solved=self.solved)
        return problems
