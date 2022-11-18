from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from . import models

def index(request):
    context={'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def tagQuestion(request, tag : str):
    context={'tag': tag, 'questions': models.QUESTIONS}
    return render(request, 'tagQuestions.html', context=context)


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    context = {'question': question_item}
    return render(request, 'question.html', context=context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')