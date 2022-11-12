
from django.shortcuts import render, get_object_or_404,redirect
from appCorridasBr.form import UsuarioForm
from appCorridasBr.models import Usuario
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, "index.html")

def areaRestrita(request):

    return render(request, "areaRestrita.html")

def cadastroUsuario(request):

    data = {}
    data['form'] = UsuarioForm()
    return render(request, "cadastroUsuario.html", data)

def logar(request):



    #login = Usuario.objects.filter(email__icontains='pain.vieira@hotmail.co')



    busca = request.GET.get("request")
    senha=request.GET.get("senha")
    login = Usuario.objects.filter(email=busca,senha=senha)



    if (login):
        return render(request, "areaRestrita.html")
    else:
        messages.info(request, 'Usuário ou Senha Incorretos')
        return redirect('home')


