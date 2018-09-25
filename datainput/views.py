from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
	db_data_list = DataInput.objects.all().order_by('-time_stamp')[4:14]
	paginator = Paginator(db_data_list, 11)

	page = request.GET.get('page')
	try:
		db_data = paginator.page(page)
	except PageNotAnInteger:
		db_data = paginator.page(1)
	except EmptyPage:
		db_data = paginator.page(paginator.num_pages)

	context = {
		"data": db_data
	}
	return render(request, 'home.html', context)	

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
    	db_data = DataInput.objects.all().order_by("-time_stamp")
    	paginate_by = 10
    	context = {
    		"data": db_data
    	}
    	return context	

def test(request):
	i = 0
	while i < len(i):
		i += 1
	data = i
	print(data)
	return HttpResponse(data)    	