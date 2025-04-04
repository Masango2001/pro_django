# users/decorators.py
from django.http import HttpResponseForbidden

def role_required(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Vous n'avez pas l'autorisation d'accéder à cette page.")
        return _wrapped_view
    return decorator



