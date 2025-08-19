from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contato(request):
    nome="Carlos"
    idade="17"

    return render(request, 'contato.html', {'nome': nome, "idade": idade})