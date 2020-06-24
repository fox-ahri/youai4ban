from rest_framework.response import Response
from rest_framework.views import APIView
from manager.extensions.jwt_auth import create_token
from manager.models import User
from manager.serializer import UserSerializer
from django.utils import timezone


class LoginView(APIView):

    def post(self, request):
        number = request.data.get('number')
        password = request.data.get('password')
        user = User.objects.filter(password=password, number=number).first()
        if user:
            user.last_login = timezone.now()
            user.save()
            data = UserSerializer(instance=user, many=False).data
            data['password'] = ''
            token = create_token(data)
            return Response({'code': 200, 'msg': '登陆成功', 'data': {'token': token}})
        return Response({'code': 400, 'msg': '密码错误', 'data': None})
