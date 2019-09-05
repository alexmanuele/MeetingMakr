from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from choose import models
from django.urls import reverse
from .forms import NewPersonForm, NewLabForm
from .models import Person,LabGroup
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

def select(request, lab_id):
    lab=get_object_or_404(LabGroup, pk=lab_id)
    togo = Person.objects.filter(presented=False, lab=lab)
    togo_pk = togo.values_list('pk', flat=True)
    max_id = togo.count()
    while True:
        pk = random.choice(togo_pk)
        person = Person.objects.filter(pk=pk).first()
        if person:
            context = {'newperson': person}
            break
    html_modal = render_to_string('modal_content.html', context, request=request)
    return JsonResponse({'html_modal': html_modal, 'person':person.pk})

def save_person_form(request, form, template_name, lab):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            togo = Person.objects.filter(presented=False, lab=lab)
            done = Person.objects.filter(presented=True, lab=lab)
            data['html_person_list'] = render_to_string('partial_person_list.html',
                                            {'potential': togo, 'done': done, 'lab':lab})
            #return render(request, 'meetings.html',  context={'potential': togo, 'done': done, 'lab': lab})
        else:
            data['form_is_valid'] = False

    context = {'form': form, 'lab':lab}
    print("HENLO HEHE")
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    lab = person.lab
    print("person update henlo")
    if request.method == 'POST':
        print("post requset here ")
        form = NewPersonForm(request.POST, instance=person)
        #form.save()
    else:
        print("get request hya")
        form = NewPersonForm(instance=person)
    return save_person_form(request, form, 'partial_person_update.html', lab)

def person_present(request, pk):
    person = get_object_or_404(Person, pk=pk)
    lab = person.lab
    if request.method == 'GET':
        person.presented = True
        person.save()
    togo = Person.objects.filter(presented=False, lab=lab)
    done = Person.objects.filter(presented=True, lab=lab)
    return render(request, "meetings.html", context={'potential': togo, 'done': done, 'lab':lab})

def lab_create(request):
    if request.method == "POST":
        form = NewLabForm(request.POST)
    else:
        form = NewLabForm()
    return save_lab_form(request, form, 'partial_lab_create.html')


def save_lab_form(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            labs = LabGroup.objects.all()
            data['html_lab_list'] = render_to_string('partial_lab_list.html',
                                        {'labs':labs})
            return render(request, 'landing.html', context={'labs':labs})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def person_create(request, lab_id):
    print(lab_id)
    lab = get_object_or_404(LabGroup, pk=lab_id)
    print("ok")
    person = Person(lab=lab)
    if request.method == "POST":
        form = NewPersonForm(request.POST, instance=person)
    else:
        form = NewPersonForm(instance=person)
    return save_person_form(request, form, 'partial_person_create.html', lab)

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    lab = person.lab
    data = dict()
#    if request.method == 'POST':
    person.delete()
    data['form_is_valid'] = True
    togo = Person.objects.filter(presented=False, lab=lab)
    done = Person.objects.filter(presented=True, lab=lab)
    data['html_person_list'] = render_to_string('partial_person_list.html',
                                        {'potential': togo, 'done': done, 'lab': lab})
    return render(request, 'meetings.html',  context={'potential': togo, 'done': done, 'lab':lab})


def meetingmakr(request, pk):
    lab = get_object_or_404(LabGroup, pk=pk)
    template_name="meetings.html"
    togo = Person.objects.filter(presented=False, lab=lab)
    done = Person.objects.filter(presented=True, lab=lab)
    return render(request, template_name, context={'lab':lab, 'potential': togo, 'done': done})

class Landing(TemplateView):
    template_name="landing.html"
    def get(self, request):
        labs = LabGroup.objects.all()
        context = {'labs':labs}
        return render(self.request, self.template_name, context)
