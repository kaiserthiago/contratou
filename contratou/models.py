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
    foto = models.ImageField(upload_to='img_profissional', blank=True, null=True)
    area = models.ManyToManyField(Area)

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
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now=False)

    class Meta:
        verbose_name_plural = 'Serviços'


class AvaliacaoProfissional(models.Model):
    profissional = models.ForeignKey(Profissional)
    contratante = models.ForeignKey(Contratante)
    servico = models.ForeignKey(Servico)
    campo1 = models.IntegerField()
    campo2 = models.IntegerField()
    campo3 = models.IntegerField()
    campo4 = models.IntegerField()
    campo5 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Avaliação Profissionais'
        ordering = ['profissional', 'contratante']

    def __str__(self):
        return self.profissional


class AvaliacaoContratante(models.Model):
    profissional = models.ForeignKey(Profissional)
    contratante = models.ForeignKey(Contratante)
    servico = models.ForeignKey(Servico)
    campo1 = models.IntegerField()
    campo2 = models.IntegerField()
    campo3 = models.IntegerField()
    campo4 = models.IntegerField()
    campo5 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Avaliação Contratantes'
        ordering = ['contratante', 'profissional']

    def __str__(self):
        return self.contratante
