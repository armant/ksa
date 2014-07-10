from django.shortcuts import render, redirect
from models import KSA
from forms import KSAForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from random import sample

#copied from Imagestore
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from imagestore.models import Album, Image
from imagestore.models import image_applabel, image_classname
from imagestore.models import album_applabel, album_classname
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tagging.models import TaggedItem
from tagging.utils import get_tag
from imagestore.utils import load_class
from django.db.models import Q
from imagestore.views import AlbumListView

# Create your views here.
def index(request):
    ksa_list = KSA.objects.all().order_by('ksa_name')
    prez = KSA.objects.get(pk=4)
    image_list = Image.objects.all().order_by('?')[:5]
    album_list = Album.objects.filter(is_public=True).select_related('head')
    return render(request, 'directory/index.html', {'ksa_list': ksa_list, 'prez': prez, 'album_list': album_list, 'image_list': image_list})

def ksa_view(request, pk):
    ksa_list = KSA.objects.all().order_by('ksa_name')
    ksa_instance = KSA.objects.get(pk=pk)
    user = ksa_instance.user
    albums = Album.objects.filter(user=user)
    return render(request, 'directory/instance.html', {'ksa_list': ksa_list, 'ksa_instance': ksa_instance, 'user': user, 'albums': albums})

class KSAUpdate(UpdateView):
    model = KSA
    form_class = KSAForm
    template_name = 'directory/update.html'
    success_url = '/'
    def get_object(self, queryset=None):
        KSA_requested = KSA.objects.get(pk=self.kwargs['pk'])
        if KSA_requested.user == self.request.user:
            return KSA_requested
        else:
            raise Http404

@login_required(login_url='/login/')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def toupdate(request):
    needed_id = request.user.ksa.id
    return HttpResponseRedirect('/directory/update/%s' %needed_id)