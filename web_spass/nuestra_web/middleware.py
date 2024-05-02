# middleware.py
from django.shortcuts import redirect

# def auth_middleware(get_response):
#    def middleware(request):
#        if not request.user.is_authenticated and not request.path.startswith('/register/'):
#            return redirect('register')
#        response = get_response(request)
#        return response
#    return middleware
