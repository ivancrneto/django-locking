import django
if django.VERSION >= (1, 6):
    from django.conf.urls import patterns
else:
    from django.conf.urls.defaults import patterns

urlpatterns = patterns('locking.views',
    # verwijst naar een ajax-view voor het lockingmechanisme
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', 'lock'),
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', 'unlock'),
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$', 'is_locked'),
    (r'variables\.js$', 'js_variables', {}, 'locking_variables'),
    )

urlpatterns += patterns('',
    (r'jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': 'locking'}),
    )
