from django.conf.urls import patterns, url

urlpatterns = patterns('ReadingNotes.views',
    url(r'^$', 'index'),
)
