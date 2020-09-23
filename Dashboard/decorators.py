from django.contrib.auth.models import Permission
from django.shortcuts import redirect
from django.contrib import messages

def admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.has_perm("StudentManager.view_admin"):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'You do not have the necessary permission to perform this operation!'
                                    'Please contact the site administrator')
            return redirect("login")
    return wrapper_func


def managerecords(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.has_perm("StudentManager.view_schooladmin") or request.user.has_perm("StudentManager.view_admin"):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'You do not have the necessary permission to perform this operation!'
                                    'Please contact the site administrator')
            return redirect("login")
    return wrapper_func

def management(view_func):
    def wrapper_func(request, *args, **kwargs):
        if (request.user.has_perm("StudentManager.view_account") or request.user.has_perm("StudentManager.view_schooladmin")
            or request.user.has_perm("StudentManager.view_admin")):
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return wrapper_func


def pastoral(view_func):
    def wrapper_func(request, *args, **kwargs):
        if (request.user.has_perm("StudentManager.view_pastoral") or request.user.has_perm("StudentManager.view_schooladmin")
            or request.user.has_perm("StudentManager.view_admin")):
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return wrapper_func