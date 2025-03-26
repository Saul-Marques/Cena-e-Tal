from django.contrib.auth.models import AnonymousUser
from loja.models import User  # usa diretamente o teu User
from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings
from asgiref.sync import sync_to_async


@sync_to_async
def get_user_from_custom_session(session_key):
    session = SessionStore(session_key=session_key)
    uid = session.get('user_id')  # <- usa tua chave customizada
    if uid is None:
        return AnonymousUser()
    try:
        return User.objects.get(pk=uid)
    except User.DoesNotExist:
        return AnonymousUser()


class WebSocketSessionUserMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        session_key = None

        if b"cookie" in headers:
            cookies = headers[b"cookie"].decode().split(";")
            for cookie in cookies:
                if cookie.strip().startswith(settings.SESSION_COOKIE_NAME + "="):
                    session_key = cookie.strip().split("=")[1]
                    break

        scope["user"] = await get_user_from_custom_session(session_key) if session_key else AnonymousUser()
        return await self.inner(scope, receive, send)
