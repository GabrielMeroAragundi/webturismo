from django.forms import ModelForm, TextInput,CheckboxInput,NumberInput

from core.models import Reserva




class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'cedula': TextInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'correo': TextInput(attrs={'type': "email", 'class': 'form-control'}),
            #'fechaInicio': TextInput(attrs={'type': "date", 'class': 'col-md-3  form-control'}),
            #'fechaFin': TextInput(attrs={'type': "date", 'class': 'col-md-3  form-control'})
            
            'fechaInicio': TextInput(attrs={'type': "date",
                                            'class': 'col-2 form-control',
                                            'id': 'fechaInicio',
                                            'onChange':'changeFechaInicio()'}),
            'fechaFin': TextInput(attrs={'type': "date",
                                         'class': 'col-2 form-control',
                                         'id': 'fechaFin',
                                         'onChange':'changeFechaFin()'}),
            'adultos': NumberInput(attrs={'type': "number",
                                         'class': '',
                                         'id': 'adultos',
                                         'onChange': 'changeAdultos()'}),
            'menores': NumberInput(attrs={'type': "number",
                                         'class': '',
                                         'id': 'menores',
                                         'onChange': 'changeMenores()'}),
            'guia': CheckboxInput(attrs={'type': "checkbox",
                                         'class': '',
                                         'id': 'guia',
                                         'onChange': 'isSelected("guia")'}),
            'lancha': CheckboxInput(attrs={'type': "checkbox",
                                           'class': '',
                                           'id': 'lancha',
                                           'onChange': 'isSelected("lancha")'}),
            'hospedaje': CheckboxInput(attrs={'type': "checkbox",
                                           'class': '',
                                           'id': 'hospedaje',
                                           'onChange': 'isSelected("hospedaje")'}),
            'sendero': CheckboxInput(attrs={'type': "checkbox",
                                                'class': '',
                                                'id': 'sendero',
                                                'onChange': 'isSelected("sendero")'}),
            'salinas': CheckboxInput(attrs={'type': "checkbox",
                                                'class': '',
                                                'id': 'salinas',
                                                'onChange': 'isSelected("salinas")'}),
            'museo': CheckboxInput(attrs={'type': "checkbox",
                                                'class': '',
                                                'id': 'museo',
                                                'onChange': 'isSelected("museo")'}),
            'carpas': CheckboxInput(attrs={'type': "checkbox",
                                                'class': '',
                                                'id': 'carpas',
                                                'onChange': 'isSelected("carpas")'})
             
             

        }

