from typing import override, Union

from django.contrib.auth.views import LoginView
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from core.http import HTTPResponseHXRedirect
from user.forms import ProfileCreateForm, UserCreateForm
from user.models import Profile, User


class CustomLoginView(LoginView):
    """
    Custom LoginView that redirects authenticated users to the root URL.
    """
    template_name = 'pages/login/index.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    @override
    def form_valid(self, form) -> HttpResponse:
        """
        Handle successful HTMX login with special redirect
        """
        super().form_valid(form)

        # For HTMX requests, use custom redirect that
        # adds the `HX-Redirect` header to the response.
        if self.request.headers.get('HX-Request'):
            return HTTPResponseHXRedirect(self.get_success_url())

        # For normal requests, use the default redirect.
        return HttpResponseRedirect(self.get_success_url())


# class SignupView(View):
#     """
#     View for user signup.
#     """
#     @override
#     def get(self, request: HttpRequest) -> HttpResponse:
#         """
#         Renders the signup page.
#         """
#         user_form = UserCreateForm()
#         profile_form = ProfileCreateForm()
#         return render(
#             request,
#             'user/signup.html',
#             {'user_form': user_form, 'profile_form': profile_form}
#         )

#     @override
#     def post(self, request: HttpRequest) -> Union[
#         HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect
#     ]:
#         """
#         Handles user signup form submission.
#         """
#         user_form = UserCreateForm(request.POST)
#         profile_form = ProfileCreateForm(request.POST)

#         # Check if both forms are valid.
#         if user_form.is_valid() and profile_form.is_valid():

#             # Create the user from the form field(s).
#             email = user_form.cleaned_data['email']
#             password = user_form.cleaned_data['password1']
#             user = User.objects.create_user(
#                 email=email, password=password
#             )

#             # Create the profile linked to the user.
#             profile: Profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             return redirect('login')

#         # Re-render the signup page with errors if invalid.
#         return render(
#             request,
#             'user/signup.html',
#             {'user_form': user_form, 'profile_form': profile_form}
#         )
