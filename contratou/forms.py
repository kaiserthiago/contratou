from django import forms

from contratou.models import Profissional, Contratante, Segmento, Area, AvaliacaoProfissional, AvaliacaoContratante


class FormProfissional(forms.ModelForm):
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


class FormContratante(forms.ModelForm):
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


class FormSegmento(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSegmento, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Segmento
        fields = ['descricao']


class FormArea(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormArea, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Area
        fields = ['segmento', 'descricao']


class FormAvaliacaoProfissional(forms.ModelForm):
    class Meta:
        model = AvaliacaoProfissional
        # fields = ['profissional', 'servico', 'data_servico', 'comentario', 'campo1', 'campo2', 'campo3', 'campo4', 'campo5']
        exclude = ('contratante', 'campo1', 'campo2', 'campo3', 'campo4', 'campo5')

        widgets = {
            'profissional': forms.Select(attrs={'class': 'form-control'}),
            'servico': forms.TextInput(attrs={'class': 'form-control'}),
            'data_servico': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'profissional': "Profissional",
            'servico': "Serviço executado",
            'data_servico': "Data do serviço",
            'comentario': "Comentários",
        }


class FormAvaliacaoContratante(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormAvaliacaoContratante, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = AvaliacaoContratante
        fields = ['profissional', 'contratante', 'servico', 'campo1', 'campo2', 'campo3', 'campo4', 'campo5',
                  'comentario']
