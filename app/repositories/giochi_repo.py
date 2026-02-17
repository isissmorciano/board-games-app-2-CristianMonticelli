from app.db import get_db

def get_giochi():
    db = get_db()
    query = '''
            SELECT *
            FROM giochi 
            ORDER BY id'''
       
        
    giochi = db.execute(query).fetchall()
    return [dict(gioco) for gioco in giochi]

def create_gioco(nome, numero_giocatori_massimo, durata_media, categoria) -> None:
    db = get_db()
    query = '''
            INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria)
            VALUES (?,?,?,?,?)'''
    cursor = db.execute(query, (nome, numero_giocatori_massimo, durata_media, categoria,))
    db.commit()
    return cursor.lastrowid

def get_gioco_id(id):
    db = get_db()
    query = '''
            SELECT *
            FROM giochi 
            WHERE id=?'''
    print("--------------------------------------------------------")
    print(query)
        
    gioco = db.execute(query,(id,)).fetchone()
    if gioco:
        return dict(gioco)
    return None