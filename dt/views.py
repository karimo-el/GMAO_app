from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import work_request
from .forms import handel_create_dt_form, handel_update_dt_form

# Create your views here.


def handel_work_request(request):

    all_work_request = work_request.objects.all()
    context = {'all_work_request': all_work_request}


    return render(request, 'dt/index.html', context)

def handel_view_work_request(request, id):
    work_request = work_request.objects.get(pk = id)
    return HttpResponseRedirect(reverse("handel_work_request"))


def handel_new_wr(request):
    if request.method == 'POST':
        form = handel_create_dt_form(request.POST)
        if form.is_valid():
            new_number_dt = form.cleaned_data['number_DT']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_equipement = form.cleaned_data['equipement']
            new_installation = form.cleaned_data['installation']
            new_anomalie = form.cleaned_data['anomlie']
            new_service_conserne = form.cleaned_data['service_conserne']

            new_date_creation = form.cleaned_data['date_creation']

            new_wr = work_request(
                number_DT = new_number_dt,
               first_name = new_first_name,
               last_name = new_last_name,
               equipement = new_equipement,
               installation = new_installation,
               anomlie = new_anomalie,
               service_conserne = new_service_conserne,
               Status = 'En cours',

               date_creation = new_date_creation,
            )

            new_wr.save()
            context ={ 'form': handel_create_dt_form(), 'success': True}
            return render(request, 'dt/add_wr.html',context)
    else:
        form = handel_create_dt_form()
        context = {'form':form}
        return render(request, 'dt/add_wr.html', context)    

def handel_edit_wr(request, id):

    if request.method == 'POST':
        work_request_ = work_request.objects.get(pk=id)

        form = handel_update_dt_form(request.POST, instance = work_request_)
        if form.is_valid():
            form.save()
            context = {'form': form, 'success': True}
            return render(request, 'dt/edit_wr.html', context)


    else:
        work_request_ = work_request.objects.get(pk=id)
        
        form = handel_update_dt_form(instance = work_request_)
        context = {'form':form}
        return render(request, "dt/edit_wr.html", context)


def handel_delete_wr(request, id):
    print("on")
    if request.method == 'POST':
        work_request_= work_request.objects.get(pk=id)
        work_request_.delete()
        print("dt supprimer")
    return HttpResponseRedirect(reverse('handel_work_request'))