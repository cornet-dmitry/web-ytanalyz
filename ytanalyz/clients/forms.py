from django import forms
from .models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    """
    def clean(self):
        cleaned_data = super().clean()
        client_name = cleaned_data.get('client_name')
        project_name = cleaned_data.get('project_name')
        city = cleaned_data.get('city')
        contact = cleaned_data.get('contact')
        start_date = cleaned_data.get('start_date')
        status = cleaned_data.get('status')

        # Проверка на пустые поля
        if not client_name:
            self.add_error('client_name', 'Это поле обязательно для заполнения.')
        if not project_name:
            self.add_error('project_name', 'Это поле обязательно для заполнения.')
        if not city:
            self.add_error('city', 'Это поле обязательно для заполнения.')
        if not contact:
            self.add_error('contact', 'Это поле обязательно для заполнения.')
        if not start_date:
            self.add_error('start_date', 'Это поле обязательно для заполнения.')
        if not status:
            self.add_error('status', 'Это поле обязательно для заполнения.')

        return cleaned_data"""
