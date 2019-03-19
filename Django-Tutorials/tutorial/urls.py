from django.conf.urls import url, include
from django.contrib import admin
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', views.home, name='home'),
    url(r'^reading/', include('reading.urls', namespace='reading')),
    url(r'^writing/', include('writing.urls', namespace='writing')),
    url(r'^listening/', include('listening.urls', namespace='listening')),
    url(r'^paper/', include('questionpaper.urls', namespace='paper')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^student/', include('student.urls', namespace='student')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
