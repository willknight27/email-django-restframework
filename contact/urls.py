from django.urls import path
from contact.views import contact_email


urlpatterns = [
    path('email/', contact_email, name='send_email')
]
