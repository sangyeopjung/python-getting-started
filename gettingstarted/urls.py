from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

from hello import views, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', views.index, name='views'),
    path('question1', question1.index, name='question1'),
    path('question2', question2.index, name='question2'),
    path('question3', question3.index, name='question3'),
    path('question4', question4.index, name='question4'),
    path('question5', question5.index, name='question5'),
    path('question6', question6.index, name='question6'),
    path('question7', question7.index, name='question7'),
    path('question8', question8.index, name='question8'),
    path('question9', question9.index, name='question9'),
    path('question10', question10.index, name='question10'),
    url(r'^db', views.db, name='db'),
    path('admin/', admin.site.urls),
]
