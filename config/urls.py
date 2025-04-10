from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('/chat/legal/', permanent=False)),
    path('admin/', admin.site.urls),
    path('rag_legal/', include('rag_legal.urls')),
    path('chat/', include('chat.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    try:
        urlpatterns += [
            path("__reload__/", include("django_browser_reload.urls", namespace="django_browser_reload")),
        ]
    except ImportError:
        print("⚠️ django_browser_reload no está instalado. Saltando integración.")
    
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
