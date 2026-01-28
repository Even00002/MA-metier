"""
Nom du fichier : seed_users.py
Auteur : Joel Cunha Faria
Date de création : 20.01.2026
Date de modification : 28.01.2026
"""

from sqlalchemy import insert, select
from db_schema import engine
from Backend.Class.Class_User import User
from datetime import date, datetime

def add_users(username: str, password: str, email: str, birthdate: date, role: str, is_banned: bool, is_muted: bool):
    with engine.begin() as conn:
        exists = conn.execute(
            select(User.id).where(User.username == username)
        ).fetchone()
        if exists:
            print(f"Déjà présent: {username}")
            return

        conn.execute(
            insert(User).values(username=username, password=password, email=email, birthdate=birthdate, role=role, is_banned=is_banned, is_muted=is_muted)
        )
        print(f"Ajouté: {username}")

if __name__ == "__main__":
    # ---- ADMINS ----
    birthdate = datetime.strptime("01-02-2009", "%d-%m-%Y").date()
    add_users("py18uam", "Pa$$w0rd", "py18uam@eduvaud.ch", birthdate, "admin", False, False)

    birthdate = datetime.strptime("13-06-2010", "%d-%m-%Y").date()
    add_users("pv60kfh", "Pa$$w0rd", "pv60kfh@eduvaud.ch", birthdate, "admin", False, False)

    birthdate = datetime.strptime("16-02-2006", "%d-%m-%Y").date()
    add_users("pm11mjh", "Pa$$w0rd", "pm11mjh@eduvaud.ch", birthdate, "admin", False, False)

    birthdate = datetime.strptime("23-12-2008", "%d-%m-%Y").date()
    add_users("pd51emw", "Pa$$w0rd", "pd51emw@eduvaud.ch", birthdate, "admin", False, False)

    # ---- MEMBRES ----
    membres = [
        ("pz22abc", "04-05-2007"),
        ("pt33def", "20-08-2008"),
        ("px44ghi", "11-11-2009"),
        ("py55jkl", "30-03-2006"),
        ("pv66mno", "22-09-2007"),
        ("pm77pqr", "05-12-2008"),
        ("pz88stu", "17-07-2009"),
        ("py99vwx", "01-01-2008"),
        ("pv10yza", "12-02-2007"),
        ("pm21bcd", "23-03-2006"),
        ("pz32efg", "04-04-2009"),
        ("pt43hij", "15-05-2008"),
        ("px54klm", "26-06-2007"),
        ("py65nop", "07-07-2006"),
        ("pv76qrs", "18-08-2009"),
        ("pm87tuv", "29-09-2008"),
        ("pz98wxy", "10-10-2007"),
        ("pt09zab", "21-11-2006"),
        ("px10cde", "02-12-2009"),
        ("py11fgh", "13-01-2008"),
        ("pv12ijk", "24-02-2007"),
        ("pm13lmn", "05-03-2006"),
        ("pz14opq", "16-04-2009"),
        ("pt15rst", "27-05-2008"),
        ("px16uvw", "08-06-2007"),
        ("py17xyz", "19-07-2006"),
        ("pv18abc", "30-08-2009"),
        ("pm19def", "10-09-2008"),
        ("pz20ghi", "21-10-2007"),
        ("pt21jkl", "02-11-2006"),
        ("px22mno", "13-12-2009"),
        ("py23pqr", "24-01-2008"),
        ("pv24stu", "05-02-2007"),
        ("pm25vwx", "16-03-2006"),
        ("pz26yza", "27-04-2009"),
        ("pt27bcd", "08-05-2008"),
        ("px28efg", "19-06-2007"),
        ("py29hij", "30-07-2006"),
        ("pv30klm", "11-08-2009"),
        ("pm31nop", "22-09-2008"),
        ("pz32qrs", "03-10-2007"),
        ("pt33tuv", "14-11-2006"),
        ("px34wxy", "25-12-2009"),
        ("py35zab", "06-01-2008"),
        ("pv36cde", "17-02-2007"),
        ("pm37fgh", "28-03-2006"),
    ]

    for u in membres:
        birthdate = datetime.strptime(u[1], "%d-%m-%Y").date()
        add_users(u[0], "Pa$$w0rd", f"{u[0]}@eduvaud.ch", birthdate, "membre", False, False)