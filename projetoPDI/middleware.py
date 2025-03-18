from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from channels.db import database_sync_to_async

User = get_user_model()  # 🔥 Garante que usa o teu `loja.User`

class WebSocketAuthMiddleware:
    """
    Middleware para autenticar utilizadores em WebSockets usando cookies de sessão.
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        session_id = None
        cookies = dict(scope.get("headers", []))

        # Extrai o `sessionid` dos cookies da WebSocket request
        for key, value in cookies.items():
            if key == b'cookie':
                cookies_dict = dict(item.split("=") for item in value.decode().split("; "))
                session_id = cookies_dict.get("sessionid", None)

        if session_id:
            scope["user"] = await get_user_from_session(session_id)
        else:
            scope["user"] = None

        return await self.inner(scope, receive, send)

@database_sync_to_async
def get_user_from_session(session_id):
    """ Obtém o utilizador autenticado através da sessão """
    try:
        session = Session.objects.get(session_key=session_id)
        session_data = session.get_decoded()
        user_id = session_data.get("_auth_user_id")
        return User.objects.get(id=user_id)  # 🔥 Usa `loja.User`
    except (Session.DoesNotExist, User.DoesNotExist, KeyError):
        return None
