from rest_framework.authentication import BaseAuthentication
import jwt
from jwt import exceptions
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class JwtAuthentication(BaseAuthentication):

    def authenticate(self, request):
        salt = settings.SECRET_KEY
        token = request.META.get('HTTP_TOKEN')
        try:
            payload = jwt.decode(token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code': 0, 'msg': 'token 超时', 'data': None})
        except jwt.DecodeError:
            raise AuthenticationFailed({'code': 0, 'msg': '错误的 token', 'data': None})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'code': 0, 'msg': '不是 jwt token', 'data': None})
        return payload, token
