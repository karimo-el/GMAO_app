from django.shortcuts import render
form .models import work_request

# Create your views here.


def handel_work_request(request):
    
    all_work_request = work_request.objects.all()
    context = {'all_work_request': all_work_request}


    return render(request, 'dt/index.html', context)
