from django.shortcuts import render

# New code

import logging
from rest_framework.views import APIView
from rest_framework.response import Response

# สร้าง logger สำหรับ activity
logger = logging.getLogger('activity')

class UserActionView(APIView):
    def post(self, request):
        user = request.data.get('user', 'anonymous')
        action = request.data.get('action', 'unknown action')

        extra = {
            'username': user,
        }

        logger.info(action, extra=extra)

        return Response({"message": "Action logged successfully"})
