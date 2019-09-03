from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from choose import models
from django.urls import reverse
from .forms import NewPersonForm
from .models import Person
from django.http import JsonResponse
from django.template.loader import render_to_string

import random
class CreatePerson(CreateView):
    form_class = NewPersonForm
    template_name = 'create.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        #return HttpResponseRedirect(self.get_success_url())
        return render(self.request, 'create.html', context={'form':NewPersonForm(),'added':self.object.name})

    def get_success_url(self):
        return reverse('create')

def select(request):
    togo = Person.objects.filter(presented=False)
    togo_pk = togo.values_list('pk', flat=True)
    max_id = togo.count()
    print("*****************************")
    print("Togo list")
    print(togo)
    print("*****************************")
    while True:
        pk = random.choice(togo_pk)
        person = Person.objects.filter(pk=pk).first()
        if person:
            context = {'newperson': person}
            break
    html_modal = render_to_string('modal_content.html', context, request=request)
    return JsonResponse({'html_modal': html_modal, 'person':person.pk})

def save_person_form(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            togo = Person.objects.filter(presented=False)
            done = Person.objects.filter(presented=True)
            data['html_person_list'] = render_to_string('partial_person_list.html',
                                            {'potential': togo, 'done': done})
            return render(request, 'meetings.html',  context={'potential': togo, 'done': done})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    print("HENLO HEHE")
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    print("person update henlo")
    if request.method == 'POST':
        print("post requset here ")
        form = NewPersonForm(request.POST, instance=person)
        #form.save()
    else:
        print("get request hya")
        form = NewPersonForm(instance=person)
    return save_person_form(request, form, 'partial_person_update.html')

def person_present(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'GET':
        person.presented = True
        person.save()
    togo = Person.objects.filter(presented=False)
    done = Person.objects.filter(presented=True)
    return render(request, "meetings.html", context={'potential': togo, 'done': done})

def person_create(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST)
    else:
        form = NewPersonForm()
    return save_person_form(request, form, 'partial_person_create.html')

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    data = dict()
#    if request.method == 'POST':
    person.delete()
    data['form_is_valid'] = True
    togo = Person.objects.filter(presented=False)
    done = Person.objects.filter(presented=True)
    data['html_person_list'] = render_to_string('partial_person_list.html',
                                        {'potential': togo, 'done': done})
    return render(request, 'meetings.html',  context={'potential': togo, 'done': done})



class MeetingMaker(TemplateView):
    template_name="meetings.html"
    choice = None
    def get(self, request):
        togo = Person.objects.filter(presented=False)
        done = Person.objects.filter(presented=True)
        return render(self.request, self.template_name, context={'potential': togo, 'done': done})
