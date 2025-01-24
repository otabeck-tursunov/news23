from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-details'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('thanks-for-contact/', ThanksContactView.as_view(), name='thanks-for-contact'),
    path('contact-us/', ContactView.as_view(), name='contact-us'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
