from django.shortcuts import render

# Dane wspólne dla wszystkich stron (nagłówek i stopka)
HOBBY_NAME = "IT i oglądanie filmów"
AUTHOR = "Bartosz Lauer"


def home(request):
    """Strona główna - przedstawienie hobby."""
    context = {
        "hobby_name": HOBBY_NAME,
        "author": AUTHOR,
        "description": (
            "Najwięcej czasu poza zajęciami spędzam przy komputerze. Nie chodzi o jedną "
            "konkretną rzecz: raz piszę kod, raz stawiam serwer, a raz po prostu sprawdzam, "
            "jak działa coś, o czym przeczytałem rano. Wieczorem odpoczywam przy filmie."
        ),
        # Główne hobby - IT, podzielone na to, czym się zajmuję
        "it_topics": [
            {
                "name": "Programowanie",
                "text": "Głównie Python. Teraz Django, bo chcę rozumieć, co się dzieje "
                        "między wpisaniem adresu a gotową stroną.",
            },
            {
                "name": "Administrowanie systemami",
                "text": "Linux, wirtualizacja, sieć. Lubię, gdy coś działa stabilnie, "
                        "i lubię też dojść do tego, dlaczego przestało.",
            },
            {
                "name": "Nowe rzeczy",
                "text": "Jak coś mnie zaciekawi, instaluję i testuję. Część zostaje na dłużej, "
                        "część ląduje w koszu po wieczorze.",
            },
        ],
        "movies_text": (
            "Mój ulubiony gatunek to horrory. Te klasyczne, jak Halloween z 1978 roku, "
            "i nowe, po których trudno zasnąć."
        ),
    }
    return render(request, "lab01/home.html", context)


def about(request):
    """O mnie - czym zajmuję się w IT i czego używam."""
    context = {
        "hobby_name": HOBBY_NAME,
        "author": AUTHOR,
        "intro": (
            "W IT najbardziej wciąga mnie to, że zawsze jest coś nowego do sprawdzenia. "
            "Piszę kod, stawiam i utrzymuję systemy, "
            "a coraz więcej czasu poświęcam bezpieczeństwu: monitorowaniu i audytom."
        ),
        # Technologie pogrupowane według obszaru
        "skill_groups": [
            {"name": "Programowanie", "items": ["Python", "Django", "HTML", "CSS", "Git"]},
            {"name": "Systemy", "items": ["Linux", "Docker", "Proxmox", "sieci"]},
            {"name": "Bezpieczeństwo", "items": ["Wazuh", "audyty IT", "analiza logów"]},
        ],
        "facts": [
            {"question": "Do czego używam Dockera?",
             "answer": "Żeby szybko postawić usługę, przetestować ją i usunąć bez śmiecenia w systemie."},
            {"question": "Czym jest dla mnie Wazuh?",
             "answer": "Systemem, który zbiera logi z wielu maszyn i pokazuje, gdy dzieje się coś podejrzanego."},
            {"question": "Na czym polegają audyty?",
             "answer": "Na sprawdzeniu, jakie są zasoby, jak działają procesy i gdzie są luki, zanim znajdzie je ktoś inny."},
            {"question": "A po pracy?",
             "answer": "Horrory. Najlepiej takie, po których trudno zasnąć."},
        ],
    }
    return render(request, "lab01/about.html", context)


def gallery(request):
    """Galeria - plakaty ulubionych filmów."""
    movies = [
        {"title": "Halloween", "image": "lab01/posters/halloween.jpg", "year": 1978, "genre": "horror", "rating": 5,
         "note": "Michael Myers i Haddonfield. Klasyk, od którego zaczęły się slashery.",
         "color": "#c8641e"},
        {"title": "Milczenie owiec", "image": "lab01/posters/milczenie.jpg", "year": 1991, "genre": "thriller / horror", "rating": 5,
         "note": "Clarice Starling i Hannibal Lecter. Rozmowy przez szybę robią więcej niż niejedna scena akcji.",
         "color": "#8a6a4a"},
        {"title": "Piła", "image": "lab01/posters/pila.jpg", "year": 2004, "genre": "horror", "rating": 4,
         "note": "Dwóch ludzi przykutych w łazience i gra, z której nie ma dobrego wyjścia.",
         "color": "#9a2a2a"},
        {"title": "Menu", "image": "lab01/posters/menu.jpg", "year": 2022, "genre": "horror / komedia", "rating": 4,
         "note": "Kolacja w ekskluzywnej restauracji na wyspie, która z każdym daniem robi się dziwniejsza.",
         "color": "#5a6b7a"},
        {"title": "Weapons", "image": "lab01/posters/weapons.jpg", "year": 2025, "genre": "horror", "rating": 5,
         "note": "Pewnej nocy prawie cała klasa znika z domów o tej samej godzinie.",
         "color": "#4a5a8a"},
        {"title": "Obsession", "image": "lab01/posters/obsession.jpg", "year": 2026, "genre": "horror", "rating": 5,
         "note": "Zakochanie, które bardzo szybko przestaje być romantyczne.",
         "color": "#8a3a6a"},
    ]
    # Plakaty: Wikipedia (miniatury plakatów kinowych)
    # Gwiazdki liczone w widoku - template tylko je wyświetla
    for movie in movies:
        movie["stars"] = "★" * movie["rating"] + "☆" * (5 - movie["rating"])

    context = {
        "hobby_name": HOBBY_NAME,
        "author": AUTHOR,
        "movies": movies,
    }
    return render(request, "lab01/gallery.html", context)
