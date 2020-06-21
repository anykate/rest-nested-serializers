import requests

from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Student, Marks
from .forms import MarksInsertForm
from .serializers import MarksSerializer, StudentSerializer


class StudentsViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MarksViewset(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer


def savemarks(request):
    form = MarksInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            student = form.cleaned_data.pop('student')
            form.cleaned_data['student'] = student.id
            post_data = requests.post(
                'http://localhost:8000/api/marks/',
                headers={'Content-Type': 'application/json'},
                json=form.cleaned_data
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
