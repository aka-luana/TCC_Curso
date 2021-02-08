from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import DoencasExistentes
from CadastroDePessoa.models import Usuario

from .forms import DoencasExistentesForm

@login_required(redirect_field_name='index_login')
def doencas_existentes(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_doencas_existentes = DoencasExistentes.objects.filter(fk_usuario_doencas_existentes=usuario.id_usuario)

    if str(request.method) == 'POST':
        print(dados_doencas_existentes)
        form = DoencasExistentesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("doencas-existentes")
        
    return render(request, "doencas-existentes.html", {"usuario": usuario, 'dados_doencas_existentes':dados_doencas_existentes})


@login_required(redirect_field_name='index_login')
def doencas_existentes_detail(request, pk):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_doencas_existentes = DoencasExistentes.objects.filter(fk_usuario_doencas_existentes=usuario.id_usuario)

    doenca_detail = DoencasExistentes.objects.get(id_doencas_existentes=pk)


    if str(request.method) == 'POST':
        form = DoencasExistentesForm(request.POST, request.FILES, instance=doenca_detail)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('doencas-existentes')

    return render(request, "doencas-existentes.html", {"usuario": usuario, 'dados_doencas_existentes': dados_doencas_existentes, 'doenca_detail': doenca_detail})


@login_required(redirect_field_name='index_login')
def doencas_existentes_delete(request, pk):
    doencas = DoencasExistentes.objects.get(id_doencas_existentes=pk)
    doencas.delete()

    return redirect('doencas-existentes')