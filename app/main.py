from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.repositories import giochi_repo, partite_repo

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

#3. Visualizzare la lista dei giochi
@bp.route('/')
def index():


    lista_giochi = giochi_repo.get_giochi()
    
    return render_template('index.html', lista_giochi = lista_giochi)

#1. Creare nuovi giochi da tavolo
@bp.route("/url_crea_gioco", methods=("GET", "POST"))
def create_gioco():

    if request.method == "POST":
        nome = request.form["nome"]
        numero_giocatori_massimo = request.form["numero_giocatori_massimo"]
        durata_media = request.form["durata_media"]
        categoria = request.form["categoria"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."
        if not categoria:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il canale
            giochi_repo.create_gioco(nome, numero_giocatori_massimo, durata_media, categoria)
            return redirect(url_for("main.index"))
    return render_template('create_gioco.html')


#4. Visualizzare la lista delle partite di un gioco
@bp.route('/partite_gioco/<int:id>')
def partite_gioco(id):
    gioco = giochi_repo.get_gioco_id(id)
    partite = partite_repo.get_partite_id(gioco['id'])
    return render_template('partite_gioco.html',gioco=gioco,partite=partite)

#2. Registrare partite per un gioco esistente
@bp.route('/nuove_partite_gioco/<int:id>', methods=("GET", "POST"))
def nuove_partite_gioco(id):
    if request.method == "POST":
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio_vincitore = request.form["punteggio_vincitore"]
        error = None

        if not vincitore:
            error = "Il vincitore è obbligatorio."
        if not punteggio_vincitore:
            error = "La punteggio_vincitore è obbligatoria."

        if error is not None:
            flash(error)
        else:
            gioco = giochi_repo.get_gioco_id(id)
            partite = partite_repo.get_partite_id(gioco['id'])
            partite_repo.create_partite(id,data,vincitore,punteggio_vincitore)
            return render_template('partite_gioco.html',gioco=gioco,partite=partite)
    return render_template('create_partite.html')
