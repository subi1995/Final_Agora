from django import forms
from django.forms import ModelForm, Textarea
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
            model = Reservation

            fields = ('name','tel_num','major','num_people',
                      'room_number','rend_date','rend_time','return_time','reservation_accept',)
            
##            widgets={ 'name': Textarea(attrs={'cols': 80, 'rows': 20}),}
