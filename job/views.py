from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job
from .form import ApplyForm
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    
    paginator = Paginator(job_list , 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs' :page_obj}
    
    return render(request,'job/job_list.html',context)


def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method=='POST':
        pass
    else:
        form = ApplyForm()

    context = {'job':job_detail, 'form':form}
    return render(request,'job/job_detail.html',context)
 