# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from models import Question
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from models import Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice"})
    # return HttpResponse("You're voting on question %s." % question_id)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id)))