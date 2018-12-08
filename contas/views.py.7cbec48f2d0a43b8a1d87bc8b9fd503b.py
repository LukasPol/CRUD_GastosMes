from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {}
    data['transacao'] = ['t1','t2', 't3']

    data['now'] = datetime.datetime.now() # pegar a hora naquela momento
    # html = '<html><body>Olá, agora é %s</body></html>' %now
    # return HttpResponse(html)

    return render(request, 'contas/home.html',data)

def listagem(request):
    data = {}
    modo_busca = request.GET.get('modo_busca')
    termo_busca = request.GET.get('pesquisa', None)

    if termo_busca:
        if modo_busca == 'nome':
            transacoes = Transacao.objects.all()
            data['transacoes'] = transacoes.filter(nome=termo_busca)
        elif modo_busca == 'valor':
            transacoes = Transacao.objects.all()
            data['transacoes'] = transacoes.filter(valor=termo_busca)
        elif modo_busca == 'pagamento':
            transacoes = Transacao.objects.all()
            data['transacoes'] = transacoes.filter(valor=termo_busca)
    else:
        data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None) # ele irá verificar se tem alguma coisa e já preenche

    if form.is_valid(): #verifica se é valido o formulário
        form.save()
        #return listagem(request) # quando salvar a página retorna para a listagem, mas replica os dados
        return redirect('url_list') # para nn replicar os dados

    data['form'] = form #mesma coisa
    return render(request, 'contas/form.html', data)


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk) # filter para retornar maisde um objeto
    form = TransacaoForm(request.POST or None, instance=transacao)
    # para não começar o form vazio

    if form.is_valid(): 
        form.save()
        return redirect('url_list')
    data = {}
    data['form'] = form 
    data['transacao']  = transacao #para deletar, pois lánn tem a variavel
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_list')
