from django.db import models
from django.utils.text import slugify

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    dataInicio = models.DateField("Data de Inicio")
    dataFinal = models.DateField("Data final")
    def __str__(self):
        return self.nome
    def alunos(self):
        lista = Aluno.objects.filter(turma=self)
        return lista

class Aluno(models.Model):
    turma = models.ForeignKey(Turma,on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    matricula = models.IntegerField()
    image = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True)
    def save(self, *args, **kwargs):
    	if not self.pk:
    		self.slug = slugify(self.nome)
    	super(Aluno, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.PROTECT)
    data_com_hora = models.DateTimeField(
        blank=True, null=True,verbose_name="Data e Hora")
    def __str__(self):
        return str(self.aluno.nome)+ ' - ' + str(self.data_com_hora.ctime())




