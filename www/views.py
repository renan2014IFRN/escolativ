from django.shortcuts import render, redirect
from .models import Aluno, Frequencia, Turma
from .forms import AlunoForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    aluno = Aluno.objects.all()
    turmas = Turma.objects.all()
    #aluno_da_turma = Turma.alunos()
    for t in turmas:
        alunosdaturma = Aluno.objects.filter(turma_id=t.id)

        print(alunosdaturma)
        dict_turma = {}
        for al in alunosdaturma:
            frequencias = []
            for p in Frequencia.objects.all():
                if p.aluno == al:
                    frequencias.append(p.data_com_hora)
            print("FRE.",al.nome,frequencias)
    #for t in turmas:
       # alunos = Aluno.objects.filter(pk=t.pk)

    return render(request, 'index.html', {'aluno': aluno, 'turmas':turmas, 'frequencias':frequencias})


def detalhes(request, slug):
    aluno = Aluno.objects.get(slug=slug)
    frequencias = []
    for p in Frequencia.objects.all():
        if p.aluno==aluno:
            frequencias.append(p.data_com_hora)
    return render(request, 'detalhes.html', {'aluno': aluno, 'frequencias': frequencias})



def editar(request, slug):
    aluno = Aluno.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = AlunoForm(data=request.POST, instance=aluno)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse('detalhes', args=[slug, ]))
    else:
        ##aluno_dict = model_to_dict(aluno)
        form = AlunoForm(instance=aluno)
        return render(request, 'editar.html', {'form': form})
