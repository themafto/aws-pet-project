import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def test_rds(request):
    try:
        response = requests.get(settings.BACKEND_RDS_URL)
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to backendrds: {e}")
        return JsonResponse({'error': str(e)}, status=500)

def test_redis(request):
    try:
        response = requests.get(settings.BACKEND_REDIS_URL)
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to backendredis: {e}")
        return JsonResponse({'error': str(e)}, status=500)
