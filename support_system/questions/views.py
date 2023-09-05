from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def questions_home(request):
    questions = Articles.objects.order_by('-date')
    return render(request, 'questions/questions_home.html', {'questions': questions})


class QuestionsDetailView(DetailView):
    model = Articles
    template_name = 'questions/details_view.html'
    context_object_name = 'article'


class QuestionsUpdateView(UpdateView):
    model = Articles
    template_name = 'questions/create.html'

    form_class = ArticlesForm


class QuestionsDeleteView(DeleteView):
    model = Articles
    succes_url = ''
    template_name = 'questions/questions-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'questions/create.html', data)
