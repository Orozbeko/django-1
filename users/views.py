from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares

class RegistrationView(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = "users/register.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data['experience']
        if age < 1:
            self.object.experience = 'Junior'
        elif age >= 2 and age <= 3:
            self.object.experience = 'Junior'
        elif age >= 3 and age <= 5:
            self.object.experience = 'Middle'
        else:
            self.object.experience = 'Senior'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience'] = getattr(self.request, 'experience', 'Опыт работы не определен')
        return context