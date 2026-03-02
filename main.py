from js import document

def show_players(event=None):
    output_list = document.getElementById("output-list")
    if output_list is None:
        return

    players = [
        "Arevalo, Rhianna Mateo",
        "Atienza, Sebastian Caleb Bustamante",
        "Cubillas, Christian Emmanuel Lin",
        "David, Jolie Cassandra Marquez",
        "De Guzman, Stephanie Gaile",
        "De La Paz, Joaquin Matteo Altura",
        "De Leon, Marcus Theoden Catimpo",
        "De Luna, Andrew James Alipio",
        "Deinla, Brennan Shane Castillo",
        "Elevazo, John Rony Laurilla",
        "Francisco, Amber Ephesiah Manansala",
        "Ganal, Franceska Marie Salvador",
        "Lacerna, Atashya Khariz Coquilla",
        "Lavilla, Ava Samantha Gilo",
        "Luna, Shantia Angelic Ayong",
        "Morishita, John Ken Gudito",
        "Ortega, Megan Jacinth Capili",
        "Pangilinan, Noleen Kelly Berdejo",
        "Salonga, Carmen Beatriz Francisco",
        "Santiaguel, Jasie Grace Dejucos",
        "Solis, Brooke Anika Zamora",
        "Sta. Maria, John Gabriel Sanchez",
        "Tubangi, Lyle Yumi U.",
        "Urrutia, Alexander Lucas Prospero",
        "Valeroso, Eyl Carl Rante",
        "Villanueva, Art Varon"
    ]

    text = ""
    for i, player in enumerate(players):
        text += f"{i+1}.) {player}<br>"

    output_list.innerHTML = text