from django import forms
from django.forms import ModelForm, CharField, Select, TextInput
from .models import Owner, Betetkonyv_User

class BetetkonyvUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    class Meta:
     model = Betetkonyv_User
     fields = {
            "betetkonyv",
            "owner" ,
            "ertek"
     }
     labels = {
        "betetkonyv": "Betétkönyv sorszáma",
        "owner" : "Tulajdonos",
        "ertek" : "Értéke",

     }
     prices = {
             ('5000','5 000 Ft'),
             ('10000','10 000 Ft'),
             ('20000','20 000 Ft'),
             ('50000','50 000 Ft'),
     }
     widgets = {
      'ertek': Select(choices=prices),
     }
     def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']

        return super(PointForm, self).save(commit=commit)
