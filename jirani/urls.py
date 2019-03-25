from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^blog',views.blog, name='blog'),
    url(r'^health',views.health, name='health'),
    url(r'^authorities',views.security, name='authorities'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
    url(r'^my-profile/',views.my_profile, name='my-profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^search/',views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
