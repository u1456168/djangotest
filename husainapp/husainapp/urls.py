from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from hotel import views
from registration.backends.simple.views import RegistrationView
app_name = 'husainapp'

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^hotels/', include('hotel.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),


]
