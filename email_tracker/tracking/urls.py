from django.urls import path, include
from django.views.generic import TemplateView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('vote/', track_click, name='track_click'),
    path('clicks/', clicks_list, name='clicks_list'),
    path('logout/', logout_view, name='logout'),
    path('send-email/', send_emails_view, name='send_email'),
    path('upload-csv/', upload_csv_view, name='upload_csv'),
    # path('upload-recipients/', upload_recipients_view, name='upload_recipients'),
    path('email-sent-success/', TemplateView.as_view(template_name='email_sent_success.html'), name='email_sent_success'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)