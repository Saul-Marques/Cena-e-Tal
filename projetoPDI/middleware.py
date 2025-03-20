from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class WebSocketAuthMiddleware:
    """Middleware to authenticate WebSocket users using session cookies."""

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope.get("headers", []))
        cookies = {}

        if b"cookie" in headers:
            cookie_header = headers[b"cookie"].decode()
            cookies = dict(item.split("=", 1) for item in cookie_header.split("; ") if "=" in item)

        session_id = cookies.get("sessionid")

        if session_id:
            user = await get_user_from_session(session_id)
            scope["user"] = user if user else AnonymousUser()

            print(f"✅ WebSocket Authenticated User: {user}")  
        else:
            scope["user"] = AnonymousUser()
            print("❌ WebSocket Authentication Failed: No session found")

        return await self.inner(scope, receive, send)

@database_sync_to_async
def get_user_from_session(session_id):
    """ Get the authenticated user from the session ID """
    try:
        session = Session.objects.get(session_key=session_id)
        session_data = session.get_decoded()
        user_id = session_data.get("_auth_user_id")
        return User.objects.get(id=user_id)
    except (Session.DoesNotExist, User.DoesNotExist, KeyError):
        return None
