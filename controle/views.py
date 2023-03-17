from django.shortcuts import render,redirect
from http.client import HTTPResponse
from controle.forms import DadosForm
from controle.models import Dados_c

# Create your views here.



def dados(request):
    if request.method == 'POST':
        form = DadosForm(request.POST,request.FILES)
        if form.is_valid():
            #form = Dados_c.save(commit=False)
            form.save()
            #print(form) 
        return redirect('lista')
                   
    else:
        form = DadosForm()
        return render(request, 'controle/dados_Cli.html',{'form':form})
       
def lista(request):
    dados =  Dados_c.objects.all()
    #print(dados)
    return render(request,  'controle/home.html',{'dados':dados})
 