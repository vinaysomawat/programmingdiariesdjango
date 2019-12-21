from . import views
from django.urls import path

from django.conf import settings
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListall.as_view(), name='home'),
    path('web-development/', views.PostListwebdev.as_view(), name='web-development'),
    path('data-structure/', views.PostListds.as_view(), name='data-structure'),
    path('android-development/', views.PostListandroid.as_view(), name='android-development'),
    path('c-programming/', views.PostListprograms.as_view(), name='c-programming'),
    path('aboutus/', views.Aboutus.as_view(), name='aboutus'),
    path('privacypolicy/', views.Privacypolicy.as_view(), name='privacypolicy'),
    path('contactus/', views.Contactus.as_view(), name='contactus'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('aboutus/', views.aboutus, name='aboutus'),
    # path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    # path('contactus/', views.contactus, name='contactus'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
