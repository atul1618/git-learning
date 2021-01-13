from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic  import TemplateView
# Create your views here.

class Home(TemplateView):

	def get(self,request,*args,**kwargs):
		return HttpResponse("Welcome user")