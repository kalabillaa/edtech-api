from django.http import JsonResponse

def signup(request):
    return JsonResponse({'message': 'Signup API working'})

def login(request):
    return JsonResponse({'message': 'Login API working'})
