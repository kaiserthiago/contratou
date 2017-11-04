from django.forms import ModelForm

from contratou.models import Profissional, Contratante, Segmento, Area, AvaliacaoProfissional, AvaliacaoContratante


class FormProfissional(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormProfissional, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Profissional
        fields = ['nome', 'cpf', 'rg', 'orgao_expeditor', 'data_nascimento', 'logradouro', 'complemento', 'cep', 'uf',
                  'cidade', 'email', 'telefone', 'foto', 'area']


class FormContratante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormContratante, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Contratante
        fields = ['nome', 'cpf', 'rg', 'orgao_expeditor', 'data_nascimento', 'logradouro', 'complemento', 'cep', 'uf',
                  'cidade', 'email', 'telefone']


class FormSegmento(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSegmento, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Segmento
        fields = ['descricao']

class FormArea(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormArea, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Area
        fields = ['segmento', 'descricao']

class FormAvaliacaoProfissional(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormAvaliacaoProfissional, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = AvaliacaoProfissional
        fields = ['profissional', 'contratante', 'servico', 'comentario', 'campo1', 'campo2', 'campo3', 'campo4', 'campo5']

class FormAvaliacaoContratante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormAvaliacaoContratante, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = AvaliacaoContratante
        fields = ['profissional', 'contratante', 'servico', 'campo1', 'campo2', 'campo3', 'campo4', 'campo5', 'comentario']