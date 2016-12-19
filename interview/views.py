from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls.base import reverse
from django.views.generic.base import View
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
import time
import decimal

from interview.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    page_title = "Login"

    # Checks if user is already logged in
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('interview:sorting')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect('interview:sorting')

        # Returns an error if authentication failed
        form.add_error(None, "Invalid user name or password")
        return self.form_invalid(form)


# User Logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('interview:login'))


# Check for user's session and redirects it to the log in page if not authenticated
class LoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            url = reverse("interview:login")
            return redirect(url)
        return super().dispatch(request, *args, **kwargs)


class SortingView(LoggedInMixin, View):
    template_name = "sorting.html"
    #Getting via POST the ajax call, reordering it and sleeps for 3 seconds.
    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and request.is_ajax():
            arr = []
            resp = request.POST.get('num1').split(',')
            for i in resp:
                arr.append(decimal.Decimal(i))
            arr.sort()
            time.sleep(3)

        return JsonResponse(arr, safe=False)

    def get(self, request, *args, **kwargs):
        return render(request, "sorting.html")

class LayoutView(View):
    template_name = "Layout.html"

    def get(self, request):
        return TemplateResponse(request, "Layout.html")