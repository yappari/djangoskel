import settings as _settings


# debugging
DEBUG = True
_toolbar = False



INSTALLED_APPS = _settings.INSTALLED_APPS

if _toolbar:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES = _settings.MIDDLEWARE_CLASSES + ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
