from django.contrib.sessions.backends.db import SessionStore
from .models import User

def get_session_id(user_id):
    # Retrieve the user object
    user = User.objects.get(id=user_id)

    # Get the session key associated with the user
    session_key = user.session_key

    # If the session key is None, retrieve it from the session store
    if not session_key:
        session = SessionStore()
        session.create()
        session_key = session.session_key

        # Associate the session key with the user
        user.session_key = session_key
        user.save()

    return session_key
