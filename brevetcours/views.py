from django.shortcuts import render


def error_404(request, allowed_hosts=True):
    data = {'message': '404 - Page not found'}
    return render(request, 'error.html', data)

def error_500(request, allowed_hosts=True):
    data = {'message': '500 Internal Server Error'}
    return render(request, 'error.html', data)