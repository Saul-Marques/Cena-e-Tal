# loja/middleware.py
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db import close_old_connections
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(session_key):
    try:
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if user_id is None:
            return AnonymousUser()
        User = get_user_model()
        return User.objects.get(id=user_id)
    except Exception:
        return AnonymousUser()

class CustomAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()

        # Extract cookie headers
        cookies = {}
        for header in scope['headers']:
            if header[0] == b'cookie':
                raw_cookie = header[1].decode()
                for pair in raw_cookie.split(';'):
                    key, _, value = pair.strip().partition('=')
                    cookies[key] = value

        session_key = cookies.get('sessionid', None)
        scope['user'] = await get_user(session_key)

        return await super().__call__(scope, receive, send)
