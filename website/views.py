from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Automato, Maquina, Expressao
from .forms import SequenciaForm, AutomatoForm, MaquinaForm, ExpressaoForm

def index(request):
    return render(request, 'website/index.html')

def validarAutomato(request, automato_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).validaSequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'website/automato/validarAutomato.html', context)

def automatosFinitos(request):

    context = {'automatosFinitos': Automato.objects.all()}
    return render(request, 'website/automato/automatosFinitos.html', context)

def novoAutomato(request):

    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        novoAutomato = form.save()
        novoAutomato.desenhaDiagrama()
        novoAutomato.save()
        return HttpResponseRedirect(reverse('website:automatosFinitos'))
    
    context = {'form': form}
    return render(request, 'website/automato/novoAutomato.html', context)


def editarAutomato(request, automato_id):
    instance = Automato.objects.get(id=automato_id)
    form = AutomatoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenhaDiagrama()
        a.save()
        return HttpResponseRedirect(reverse('website:automatosFinitos'))

    context = {'form': form, 'automato_id':automato_id}
    return render(request, 'website/automato/editarAutomato.html', context)

def apagarAutomato(request, automato_id):
    Automato.objects.filter(id=automato_id).delete()
    context = {'automasFinitos': Automato.objects.all()}
    return render(request, 'website/automato/automatosFinitos.html', context)

def validarMaquina(request, maquina_id):
    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Maquina.objects.get(id=maquina_id).validaSequencia(sequencia)

    context = {
        'maquina': Maquina.objects.get(id=maquina_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'website/turing/validarMaquina.html', context)

def maquinasTuring(request):
    context = {'maquinasTuring': Maquina.objects.all()}
    return render(request, 'website/turing/maquinasTuring.html', context)

def novoMaquina(request):

    form = MaquinaForm(request.POST or None)
    if form.is_valid():
        novoMaquina = form.save()
        novoMaquina.desenhaDiagrama()
        novoMaquina.save(force_update=True)
        return HttpResponseRedirect(reverse('website:maquinasTuring'))
    
    context = {'form': form}
    return render(request, 'website/turing/novoMaquina.html', context)


def editarMaquina(request, maquina_id):
    instance = Maquina.objects.get(id=maquina_id)
    form = MaquinaForm(request.POST or None, instance=instance)

    if form.is_valid():
        m = form.save()
        m.desenhaDiagrama()
        m.save()
        return HttpResponseRedirect(reverse('website:maquinasTuring'))

    context = {'form': form, 'maquina_id':maquina_id}
    return render(request, 'website/turing/editarMaquina.html', context)

def apagarMaquina(request, maquina_id):
    Maquina.objects.filter(id=maquina_id).delete()
    context = {'maquinasTuring': Maquina.objects.all()}
    return render(request, 'website/turing/maquinasTuring.html', context)

def validarExpressao(request, expressao_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Expressao.objects.get(id=expressao_id).validaSequencia(sequencia)

    context = {
        'expressao': Expressao.objects.get(id=expressao_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'website/regex/validarExpressao.html', context)

def expressoesRegulares(request):
    context = {'expressoesRegulares': Expressao.objects.all()}
    return render(request, 'website/regex/expressoesRegulares.html', context)

def novoExpressao(request):

    form = ExpressaoForm(request.POST or None)
    if form.is_valid():
        novoExpressao = form.save()
        novoExpressao.save()
        return HttpResponseRedirect(reverse('website:expressoesRegulares'))
    
    context = {'form': form}
    return render(request, 'website/regex/novoExpressao.html', context)


def editarExpressao(request, expressao_id):
    instance = Expressao.objects.get(id=expressao_id)
    form = ExpressaoForm(request.POST or None, instance=instance)
    if form.is_valid():
        m = form.save()
        m.save()
        return HttpResponseRedirect(reverse('website:expressoesRegulares'))

    context = {'form': form, 'expressao_id':expressao_id}
    return render(request, 'website/regex/editarExpressao.html', context)

def apagarExpressao(request, expressao_id):
    Expressao.objects.filter(id=expressao_id).delete()
    context = {'expressoesRegulares': Expressao.objects.all()}
    return render(request, 'website/regex/expressoesRegulares.html', context)