from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Owner
from .models import Betetkonyv_User
from .forms import BetetkonyvUserForm
from django.contrib.auth.decorators import login_required

from django.forms import inlineformset_factory
# Create your views here.
@login_required
def index(request):

    template = loader.get_template('gknybk/index.html')
    if request.method == 'POST':
        cuccok = Betetkonyv_User.objects.all()[:10]
    else:
        cuccok = Betetkonyv_User.objects.all()[:10]
    context = {
        'cuccok' : cuccok,
        'ossz': Betetkonyv_User.objects.all().count()
    }
    return HttpResponse(template.render(context, request))


def login(request):
    return render(request, 'gknybk/login.html')

@login_required
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
                tol,ig=form.cleaned_data['betetkonyv'].split("-")
                for x in range(int(tol), int(ig)+1):
                    newbetet = Betetkonyv_User(betetkonyv = str(x), owner = form.cleaned_data['owner'], ertek = form.cleaned_data['ertek'])
                    newbetet.save()
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

@login_required
def remove_betetkonyv(request, pk):
    betet = get_object_or_404(Betetkonyv_User, pk=pk)
    betet.delete()
    return redirect('index')
