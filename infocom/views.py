from urllib.parse import urlencode

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AuthorizeView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        redirect_uri = request.GET.get('redirect_uri', None)
        username = request.POST['username']
        password = request.POST['password']
        query_string = urlencode({'code': 'code'})
        url = '{}?{}'.format(redirect_uri, query_string)
        return HttpResponseRedirect(url)


def access_token(request):
    return JsonResponse({"access_token": "access token"})


def employee(request):
    return JsonResponse({"pin": "1234567890"})
