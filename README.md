# Laby z Django: Programowanie internetowe

Projekt Django `Lab0` zbiera wszystkie laby w jednym miejscu.
Strona główna (`/`) pokazuje kafelki, a każdy lab to osobna aplikacja.

Wersja online: https://26npiblauer.pythonanywhere.com/

## Lab 1: Moje hobby (`lab01`)

Mała strona o moich hobby: **IT (programowanie, administrowanie systemami) i oglądanie filmów**.

| Adres | Widok | Szablon |
|---|---|---|
| `/lab01/` | `home` | `lab01/home.html` |
| `/lab01/about/` | `about` | `lab01/about.html` |
| `/lab01/gallery/` | `gallery` | `lab01/gallery.html` |

Wszystkie strony dziedziczą po `lab01/base.html` (nagłówek, menu, stopka).
Dane (nazwa hobby, opis, listy) są przekazywane z widoków w `lab01/views.py`.
Własny CSS z Flexboxem: `lab01/static/lab01/style.css`.

## Jak uruchomić

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py runserver
```

Następnie otwórz http://127.0.0.1:8000/lab01/
