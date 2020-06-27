from rest_framework.response import Response
from rest_framework.views import APIView
from index.serializer import UserInfoSerializer, OneUserInfoSerializer
from manager.models import UserInfo


class IndexView(APIView):
    def get(self, request, id=None):
        if id:
            ui = UserInfo.objects.filter(pk=id).first()
            if ui:
                data = OneUserInfoSerializer(instance=ui, many=False).data
                return Response({'code': 200, 'msg': '查询成功', 'data': data})
            return Response({'code': 500, 'msg': '查询失败', 'data': None})
        uis = UserInfo.objects.all()
        if uis:
            data = UserInfoSerializer(instance=uis, many=True).data
            return Response({'code': 200, 'msg': '查询成功', 'data': data})
        return Response({'code': 500, 'msg': '查询失败', 'data': None})
