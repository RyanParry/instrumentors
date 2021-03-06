from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('home/', include('home.urls'))
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
