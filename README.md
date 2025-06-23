# GeekMate

GeekMate je aplikacija za praćenje različitih korisnikovih hobija. Omogućuje osnovne CRUD operacije te praćenje napretka u svakom hobiju.

---


## Značajke

- **CRUD** operacije za hobije: dodavanje, uređivanje, brisanje.
- **Audit polja**: automatsko bilježenje datuma kreiranja i posljednje promjene (CEST zona).
- **Bootstrap 5** korisničko sučelje s prilagođenom prozirnom pozadinom i stiliziranim navigacijskim stupcem.
- **Vizualizacija** napretka: Chart.js za klijentske grafikone i Matplotlib za poslužiteljske PNG grafikone.
- **Docker** podrška za jednostavno postavljanje aplikacije.

---

## Tehnologije

- Python 3.10+
- Flask
- PonyORM (SQLite)
- Bootstrap 5
- Chart.js
- Docker

---

## Struktura projekta

```
├── app.py               # Glavna Flask aplikacija
├── requirements.txt     # Python ovisnosti
├── Dockerfile           # Docker upute za izradu
├── hobi.db              # SQLite baza podataka (automatski generirana)
├── static/
│   ├── css/
│   │   └── style.css    # Prilagođeni stilovi (pozadina, navbar, container)
│   └── images/
│       └── bg.jpg       # Pozadinska slika
└── templates/
    ├── base.html        # Osnovni layout (navbar, head)
    ├── index.html       # Popis svih hobija
    ├── dodaj.html       # Forma za dodavanje hobija
    ├── uredi.html       # Forma za uređivanje
    └── vizualizacija.html # Stranica za vizualizaciju napretka
```

---

## Početak rada

### Preduvjeti

- Python 3.10 ili noviji
- Docker 
- Github Desktop

### Kloniranje repozitorija

- kloniraj repozitorij sa ovog linka: https://github.com/ladyeowyn/GeekMate/tree/main

### Upotreba s Dockerom

1. **Izrada Docker slike**:
   ```bash
   docker build -t geekmate .
   ```
2. **Pokretanje Docker kontejnera**:
   ```bash
   docker run -d --name geekmate -p 5000:5000 \
     -v "$(pwd)/hobi.db:/app/hobi.db" \
     -v "$(pwd)/static:/app/static" \
     geekmate
   ```
3. Posjetite [**http://localhost:5000**](http://localhost:5000) u pregledniku.

---

## Korištenje

- **Početna**: pregled svih hobija i njihovog napretka.
- **Dodaj Hobi**: formular za kreiranje novog hobija.
- **Uredi**: ažuriranje podataka o hobiju i ponovni izračun napretka.
- **Vizualizacija**: grafički prikaz % napretka za odabrane ili sve hobije.

---


---

## Buduća poboljšanja (mogućnosti)

- Povijest napretka za linijske grafikone.
- Straničenje i pretraživanje hobija.
- Izvoz podataka u CSV/PDF.

---

## Izvori

Pozadinska slika -> Photo by <a href="https://unsplash.com/@miracleday?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Elena Mozhvilo</a> on <a href="https://unsplash.com/photos/yellow-flower-on-white-paper-CfpCqN9qkrI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

