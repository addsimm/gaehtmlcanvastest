# Create your views here.


from __future__ import print_function

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.core.validators import validate_email

from google.appengine.api import users
from google.appengine.api import mail  # --enable_

from gaehtmlcanvasapp.models import *


def index(request):
    template_values = {}
    template_values.update({'page_name': 'Landing Page'
                            })

    return render_to_response('base.html', template_values)