from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    """Only admins can access"""
    def check(user):
        return user.groups.filter(name='Admin').exists() or user.is_superuser
    return user_passes_test(check)(view_func)

def user_required(view_func):
    """Only normal users (not admin)"""
    def check(user):
        return user.groups.filter(name='User').exists()
    return user_passes_test(check)(view_func)
