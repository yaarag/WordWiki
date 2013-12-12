from django.conf.urls import patterns, include, url
import pages.views

urlpatterns = patterns('',
    url(r'^$', pages.views.home, name='home'),
    url(r'^word$', pages.views.list, name='list'),
    url(r'^word/(?P<word_name>[a-zA-Z]+)$', pages.views.details, name='details'),
    url(r'^word/(?P<word_name>[a-zA-Z]+)/edit$', pages.views.edit, name='edit'),
    url(r'^update_view$', pages.views.update_view, name='update_view'),
    url(r'^add_word$', pages.views.add_word, name='add_word'),
)
