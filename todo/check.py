
# the sole purpose of this warning is to prevent people who have
# django-autocomplete-light installed but not configured to start the app
@register()
def dal_check(app_configs, **kwargs):
    errors = []
    return errors
