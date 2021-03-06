from django.contrib.auth.models import User
from django.db import models


class Segmento(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Area(models.Model):
    descricao = models.CharField(max_length=150)
    segmento = models.ForeignKey(Segmento)

    class Meta:
        verbose_name_plural = 'Áreas'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.IntegerField(blank=True, null=True)
    orgao_expeditor = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(auto_now=False)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=150)
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    uf = models.CharField(max_length=20, choices=uf_escolhas, default='RO')
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='img_profissional', blank=False, null=False)
    area = models.ManyToManyField(Area)

    @property
    def question_no_answer(self):
        return self.profissionalquestion_set.filter(profissionalanswer__isnull=True)

    @property
    def question_answer(self):
        return self.profissionalquestion_set.filter(profissionalanswer__isnull=False)

    class Meta:
        verbose_name_plural = 'Profissionais'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Contratante(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.IntegerField(blank=True, null=True)
    orgao_expeditor = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(auto_now=False)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=150)
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    uf = models.CharField(max_length=20, choices=uf_escolhas, default='RO')
    cep = models.CharField(max_length=10)
    email = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='img_profissional', blank=True, null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    profissional = models.ForeignKey(Profissional)
    contratante = models.ForeignKey(Contratante)
    descricao = models.TextField(blank=False, null=False, default='Sem comentários')
    data = models.DateField(auto_now=False)

    class Meta:
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.descricao


class AvaliacaoProfissional(models.Model):
    profissional = models.ForeignKey(Profissional)
    contratante = models.ForeignKey(User)
    servico = models.CharField(max_length=255)
    data_servico = models.DateField(auto_now_add=False)
    campo1 = models.IntegerField()
    campo2 = models.IntegerField()
    campo3 = models.IntegerField()
    campo4 = models.IntegerField()
    campo5 = models.IntegerField()
    comentario = models.TextField(null=False)

    class Meta:
        verbose_name_plural = 'Avaliação Profissionais'
        ordering = ['profissional', 'contratante']


class AvaliacaoContratante(models.Model):
    profissional = models.ForeignKey(Profissional)
    contratante = models.ForeignKey(Contratante)
    servico = models.ForeignKey(Servico)
    campo1 = models.IntegerField()
    campo2 = models.IntegerField()
    campo3 = models.IntegerField()
    campo4 = models.IntegerField()
    campo5 = models.IntegerField()
    comentario = models.TextField(null=False)

    class Meta:
        verbose_name_plural = 'Avaliação Contratantes'
        ordering = ['contratante', 'profissional']


class UserProfile(models.Model):
    usuario = models.OneToOneField(User, unique=True)
    profissional = models.OneToOneField(Profissional, unique=True, blank=True, null=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=2, null=True, blank=True)
    TIPO_CHOICES = (
        ('Usuário', 'Usuário'),
        ('Profissional', 'Profissional'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="Usuário")



class ProfissionalQuestion(models.Model):
    user = models.ForeignKey(User)
    profissional = models.ForeignKey('Profissional')
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Ativo")

    class Meta:
        verbose_name_plural = 'Perguntas'


    @property
    def get_answers(self):
        return self.profissionalanswer_set.filter(status='Ativo')

    def __str__(self):
        return self.question


class ProfissionalAnswer(models.Model):
    user = models.ForeignKey(User)
    profissional_question = models.ForeignKey(ProfissionalQuestion)
    answer = models.TextField()
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Ativo")

    class Meta:
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return self.answer