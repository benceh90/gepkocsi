from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Owner
from .models import Betetkonyv_User
from .forms import BetetkonyvUserForm

from django.forms import inlineformset_factory
# Create your views here.
def index(request):

    template = loader.get_template('gknybk/index.html')
    if request.method == 'POST':
        cuccok = Betetkonyv_User.objects.all()
    else:
        cuccok = Betetkonyv_User.objects.all()
    context = {
        'cuccok' : cuccok,
    }
    return HttpResponse(template.render(context, request))

def rogzites(request):
    if request.method == 'POST':

        #BookFormSet = inlineformset_factory(Betetkonyv, Betetkonyv_User, fields=('ertek','sorszam'))

        #formset = BookFormSet(request.POST)
        form = BetetkonyvUserForm(request.POST)

        #betetkonyv = form.cleaned_data['betetkonyv']
        #print (betetkonyv)
        if form.is_valid():
            #print form.cleaned_data['my_form_field_name']

            if "-" in form.cleaned_data['betetkonyv']:
                print("Itt még annyi mentést kell csinálni, ahány betétkönyv van")
            else:
                form.save()
            return redirect('index')
        #else:
            #return messages.error(request, form.errors)
        print("VALIDÁLÁSUTÁN ")
    else:
        form = BetetkonyvUserForm()
        #for row in form.fields.values(): print(row)
        return render(request, 'gknybk/rogzites.html', {'form': form})

def owner(request,owner_id):
    return HttpResponse("Userek betétkönyvei, ez éppen a következő useré: %s" % owner_id)

def sorsoltak(request):
    return HttpResponse("Itt lesz az összes kisorsolt betétkönyv")
