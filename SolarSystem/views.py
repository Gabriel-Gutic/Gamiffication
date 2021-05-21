from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, Http404
from django.template import loader
from .models import Question, Propose
from .forms import ProposeForm

def game(request, question_ID):
    question = get_object_or_404(Question, id=question_ID)
    data = {
        'question': question,
    }
    return render(request, 'SolarSystem/Game-Page.html', data)


def result(request, question_ID, variant):
    question = get_object_or_404(Question, id=question_ID)
    size = Question.objects.count()

    if variant is 1:
        question.votes_for_1 += 1
    elif variant is 2:
        question.votes_for_2 += 1
    else:
        raise Http404("Variant " + str(variant) + " doesn't exist!")

    question.save()
    data = {
        'question': question,
        'next_id': question_ID + 1,
        'size': size,
    }
    return render(request, 'SolarSystem/Result-Page.html', data)


def propose(request, next_id):

    if request.method == 'POST':
        form = ProposeForm(request.POST)
        if form.is_valid():
            var_1 = form.cleaned_data['variant_1']
            var_2 = form.cleaned_data['variant_2']
            _propose = Propose.objects.create(variant_1=var_1, variant_2=var_2)
            _propose.refresh_from_db()

    template = loader.get_template('SolarSystem/Add-Question.html')
    size = Question.objects.count()
    form = ProposeForm()
    context = {
        'next_id': next_id,
        'size': size,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


