from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.atados.forms import AuthenticationForm

urlpatterns = patterns(
    '',
    url(r'^$', direct_to_template, {'template': 'atados/atados/home.html'},
        name='home'),

    url(_(r'^sign-in$'), 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
         'template_name': 'atados/atados/sign-in.html'}, name='sign-in'),
)