from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model): 
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    parent_categoria = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
