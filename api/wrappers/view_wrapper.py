from rest_framework.views import APIView
from rest_framework.response import Response

class ViewWrapper(APIView):
    view_factorie = None

    def dispatch(self, request, *args, **kwargs):
        if not self.view_factorie:
            return Response({ 'error': 'View factorie not set' }, status=500)
        
        view_instance = self.view_factorie.create()
        request_method = request.method.lower()

        handler = getattr(view_instance, request_method, None)
        if not handler:
            return Response({"error": f"Method {request.method} not allowed"}, status=405)
        
        body, status = handler(request, *args, **kwargs)

        return Response(body, status=status)


