# In your app's views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF protection for simplicity in this example
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

        # Do something with email and password variables
        print(f'Email: {email}, Password: {password}')

        return JsonResponse({'message': 'Data received successfully'})
