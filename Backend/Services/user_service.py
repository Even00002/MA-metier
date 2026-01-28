"""
Nom du fichier   : user_service.py
Auteur           : Joel Cunha Faria
Date de création : 28.01.2026
Date de modification : 28.01.2026
"""
from Backend.DB.db_schema import get_session
from Backend.Class.Class_User import User

def set_user_ban(username: str, banned: bool):
    session = get_session()
    user = session.query(User).filter(User.username == username).first()

    if user:
        user.is_banned = banned
        session.commit()

    session.close()
