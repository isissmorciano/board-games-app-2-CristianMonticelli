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