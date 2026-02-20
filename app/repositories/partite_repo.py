from app.db import get_db



def get_partite_id(id):
    db = get_db()
    query = '''
            SELECT *
            FROM partite 
            WHERE gioco_id=?'''
    print("--------------------------------------------------------")
    print(query)
    partite = db.execute(query,(id,)).fetchall()

    return [dict(partita) for partita in partite]

def create_partite(gioco_id, data, vincitore, punteggio_vincitore) -> None:
    db = get_db()
    query = '''
            INSERT INTO partite (gioco_id,data, vincitore, punteggio_vincitore)
            VALUES (?,?,?,?)'''
    cursor = db.execute(query, (gioco_id,data, vincitore, punteggio_vincitore,))
    db.commit()
    return cursor.lastrowid

def delete_partita(partita_id):
    """Elimina un partite."""
    db = get_db()
    db.execute('DELETE FROM partite WHERE id = ?', (partita_id,))
    db.commit()