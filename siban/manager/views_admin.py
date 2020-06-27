from rest_framework.response import Response
from rest_framework.views import APIView
from manager.extensions.auth import JwtAuthentication
from manager.extensions.jwt_auth import create_token
from manager.models import User, UserInfo
from manager.serializer import UserInfoSerializer, UserSerializer


class AdminView(APIView):
    authentication_classes = [JwtAuthentication, ]

    def get(self, request):
        u = User.objects.filter(pk=request.user['id']).first()
        if u:
            ui = UserInfo.objects.filter(user=u).first()
            if ui:
                data = UserInfoSerializer(instance=ui, many=False).data
                return Response({'code': 200, 'msg': '查询成功', 'data': data})
            else:
                new = UserInfo(user=u)
                new.save()
                data = UserInfoSerializer(instance=new, many=False).data
                return Response({'code': 200, 'msg': '查询成功', 'data': data})
        return Response({'code': 500, 'msg': '服务器错误', 'data': None})

    def post(self, request):
        ui = UserInfo.objects.filter(pk=request.data.get('id')).first()
        if ui:
            ui.name = request.data.get('name')
            ui.update_time = request.data.get('name')
            ui.name = request.data.get('name')
            ui.sex = request.data.get('sex')
            ui.age = request.data.get('age')
            ui.birthday = request.data.get('birthday')
            ui.image = request.data.get('image')
            ui.introduce = request.data.get('introduce')
            ui.info = request.data.get('info')
            ui.email = request.data.get('email')
            ui.phone = request.data.get('phone')
            ui.qq = request.data.get('qq')
            ui.save()
            data = UserInfoSerializer(instance=ui, many=False).data
            return Response({'code': 200, 'msg': '更新成功', 'data': data})
        return Response({'code': 500, 'msg': '服务器错误', 'data': None})

    def put(self, request):
        user = User.objects.filter(pk=request.data.get('id')).first()
        if user:
            user.username = request.data.get('username')
            user.password = request.data.get('password')
            user.avatar = request.data.get('avatar')
            user.save()
            data = UserSerializer(instance=user, many=False).data
            data['password'] = ''
            token = create_token(data)
            return Response({'code': 200, 'msg': '更新成功', 'data': {'token': token}})
        return Response({'code': 500, 'msg': '服务器错误', 'data': None})
