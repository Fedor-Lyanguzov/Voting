"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sms_voting.views import *

urlpatterns = [
    path('2weh4EFLACKvneYZLb3n/', admin.site.urls),
    path('', PollListView.as_view(), name='poll-list'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll-update'),
    path('VLkK3JkuqLJNgeUpQWyu/', sms_endpoint, name='sms-endpoint'),
]
