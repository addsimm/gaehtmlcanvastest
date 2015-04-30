# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response

def index(request):
   template_values = {}
   template_values.update({'page_name': 'Landing Page'
                           })

   return render_to_response('index.html', template_values)