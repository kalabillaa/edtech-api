from django.http import JsonResponse

def create_assignment(request):
    return JsonResponse({'message': 'Create Assignment working'})

def submit_assignment(request):
    return JsonResponse({'message': 'Submit Assignment working'})

def view_submissions(request):
    return JsonResponse({'message': 'View Submissions working'})
