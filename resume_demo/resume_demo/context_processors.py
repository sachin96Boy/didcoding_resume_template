from django.contrib.auth.models import User

def project_context(request):
    context = {
        'me':User.objets.first()
    }
    return context