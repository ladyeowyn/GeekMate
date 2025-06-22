from flask import Flask, render_template, request, redirect, url_for, abort
from pony.orm import Database, Required, PrimaryKey, Optional, db_session, select
from datetime import datetime
from zoneinfo import ZoneInfo
from flask import send_file
import json


app = Flask(__name__)


db = Database()

class Hobi(db.Entity):
    id = PrimaryKey(int, auto=True)
    ime = Required(str)
    ciljano_vrijeme_napretka = Required(int, default=0)
    ostvareno_vrijeme_napretka = Required(int, default=0)
    postotak_napretka = Required(int, default=0)
    opis = Optional(str)
    datum_kreiranja = Required(datetime, default=lambda: datetime.now(ZoneInfo('Europe/Paris')))
    datum_promjene = Required(datetime, default=lambda: datetime.now(ZoneInfo('Europe/Paris')))


db.bind(provider='sqlite', filename='hobi.db', create_db=True)
db.generate_mapping(create_tables=True)

@app.route('/')
def index():
    with db_session:
        hobiji = select(h for h in Hobi)[:]
    return render_template('index.html', hobiji=hobiji)

@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj_hobi():
    if request.method == 'POST':
        ime = request.form.get('ime')
        cilj = request.form.get('ciljano_vrijeme_napretka', type=int) or 0
        ostvareno = request.form.get('ostvareno_vrijeme_napretka', type=int) or 0
        opis = request.form.get('opis')
        postotak = int(ostvareno / cilj * 100) if cilj > 0 else 0

        with db_session:
            Hobi(
                ime=ime,
                ciljano_vrijeme_napretka=cilj,
                ostvareno_vrijeme_napretka=ostvareno,
                postotak_napretka=postotak,
                opis=opis
            )
        return redirect(url_for('index'))
    return render_template('dodaj.html')

@app.route('/uredi/<int:id>', methods=['GET', 'POST'])
def uredi_hobi(id):
    with db_session:
        h = Hobi.get(id=id)
        if not h:
            abort(404)
        if request.method == 'POST':
            h.ime = request.form.get('ime')
            h.ciljano_vrijeme_napretka = request.form.get('ciljano_vrijeme_napretka', type=int) or 0
            h.ostvareno_vrijeme_napretka = request.form.get('ostvareno_vrijeme_napretka', type=int) or 0
            h.opis = request.form.get('opis')
            
            h.postotak_napretka = int(h.ostvareno_vrijeme_napretka / h.ciljano_vrijeme_napretka * 100) if h.ciljano_vrijeme_napretka > 0 else 0
            
            h.datum_promjene = datetime.now(ZoneInfo('Europe/Paris'))
            return redirect(url_for('index'))
    return render_template('uredi.html', hobi=h)

@app.route('/brisi/<int:id>', methods=['POST'])
def brisi_hobi(id):
    with db_session:
        h = Hobi.get(id=id)
        if not h:
            abort(404)
        h.delete()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


@app.route('/vizualizacija', methods=['GET', 'POST'])
def vizualizacija():
    with db_session:
        hobiji = select(h for h in Hobi)[:]
        labels = [h.ime for h in hobiji]
        values = [h.postotak_napretka for h in hobiji]

    selected = request.form.get('hobi_id', type=int)
    if selected:
        with db_session:
            h = Hobi.get(id=selected)
        labels = [h.ime]
        values = [h.postotak_napretka]

    
    return render_template(
        'vizualizacija.html',
        hobiji=hobiji,
        selected=selected,
        labels=labels,
        values=values
    )

