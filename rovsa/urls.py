from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rovsa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'webpage.views.home', name='home'),
    url(r'^servicioUno/', 'webpage.views.servicioUno', name='servicioUno'),
    url(r'^servicioDos/', 'webpage.views.servicioDos', name='servicioDos'),
    url(r'^servicioTres/', 'webpage.views.servicioTres', name='servicioTres'),
    url(r'^clientes/', 'webpage.views.clientes', name='clientes'),
    url(r'^aboutUs/', 'webpage.views.aboutUs', name='aboutUs'),
    url(r'^contacto/', 'webpage.views.contacto', name='contacto'),
    url(r'^gracias/', 'webpage.views.gracias', name='gracias'),


)
