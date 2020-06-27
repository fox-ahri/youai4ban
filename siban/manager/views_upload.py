import os
from rest_framework.response import Response
from rest_framework.views import APIView
from manager.extensions.auth import JwtAuthentication
import uuid
import oss2


class UploadView(APIView):
    authentication_classes = [JwtAuthentication, ]

    def post(self, request):
        img = request.FILES.get('file')
        e = os.path.splitext(img.name)[1]
        file_name = str(uuid.uuid4()) + e
        auth = oss2.Auth('<AK>', '<SK>')
        bucket = oss2.Bucket(auth, '<地域名>', '<Bucket Name>')
        result = bucket.put_object(file_name, img.read())
        s = '<域名>' + file_name
        return Response({'code': 200, 'msg': '上传成功', 'data': {'url': s}})
