from django.shortcuts import render
from django.contrib import messages
from .forms import TermoModelForm

def index(request):
    return render(request, 'index.html')

def termo(request):
    if str(request.method) == 'POST':
        form = TermoModelForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Produto salvo com sucesso.')
            form = TermoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = TermoModelForm()
    context = {
        'form': form
    }
    return render(request, 'termo.html', context)

