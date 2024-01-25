from django import forms
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta



class DateRangeForm(forms.Form):
    date_range_choices = [
        ('past_7_days', 'Past 7 Days'),
        ('past_15_days', 'Past 15 Days'),
        ('past_month', 'Past Month'),
        ('custom', 'Custom View'),
    ]

    date_range = forms.ChoiceField(choices=date_range_choices, required=True)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        date_range = cleaned_data.get('date_range')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if date_range == 'custom' and start_date and end_date:
            date_difference = end_date - start_date
            if date_difference.days > 60:
                raise ValidationError('Date range for custom option cannot exceed 60 days.')

            # Adjust end_date if it's more than 60 days from start_date
            if date_difference.days > 60:
                cleaned_data['end_date'] = start_date + timedelta(days=60)

        return cleaned_data
