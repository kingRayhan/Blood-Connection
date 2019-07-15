from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('home.html',views.home, name='home'),
    path('about.html',views.about, name='about'),
    path('blog.html',views.blog, name='blog'),
    path('contact.html',views.contact, name='contact'),
    path('blood.html', views.blood, name='blood'),
    path('sign.html', views.sign, name='sign'),

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()