# query_search/views.py
import requests
from django.http import JsonResponse

def query_search_view(request):
    query = request.GET.get('query')
    if query:
        response = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{query}')
        if response.status_code == 200:
            return JsonResponse(response.json())
    return JsonResponse({'error': 'No results found'}, status=404)
