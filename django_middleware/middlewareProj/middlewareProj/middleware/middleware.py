from typing import Any
from django.http import HttpResponseForbidden
from home.models import Store


ALLOWED_IPS = ["123.45.67.89",'987.65.34.22']
class IPBlockingMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
        
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
        
    def __call__(self,request):
        ip = self.get_client_ip(request)
        print(ip)
        if ip in ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: IP not allowed")
        
        return self.get_response(request)
    
    
    
class CheckBMPHeaderMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        headers = request.headers
        
        if "bmp" not in headers:
            return HttpResponseForbidden("Missing: header *bmp*")
        else:
            print(headers.get('bmp'))
            if not Store.objects.filter(bmp_id=str(headers.get('bmp'))).exists():
                return HttpResponseForbidden("Wrong: *bmp*")
        
        return self.get_response(request)