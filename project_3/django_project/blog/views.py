from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404, render 
from blog.models import Question,Choice
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def main(request):
     """ Render Main Page """
     return render(request, 'blog\main.html')

@login_required
def index(request):
    """ Render Login Page for user login credentials """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list}
    return render(request, 'blog\index.html', context)


@login_required
def detail(request, question_id):
    """ Render Detail Page to get particular question id """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        print("Question Does not exist")
    return render(request, r'blog/detail.html', {'question': question})


@login_required
def results(request, question_id):
    """ Render Results Page for the given question results """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, r'blog/results.html', {'question': question})


@login_required
def vote(request, question_id):
    """ Allow USer to vote for this question """
    print(1,request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, r'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
 
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
