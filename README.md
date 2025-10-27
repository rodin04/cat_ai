Cat AI 😸

Webcam reacts like a cat – erkennt Handgesten und Gesichtsausdrücke und zeigt passende Katzenbilder. Optional werden Sounds abgespielt.

Funktionen

Handgestenerkennung

Beide Hände oben 🙌 → feiernde Katze

Eine winkende Hand ✋ → winkende Katze

Hände vorm Gesicht 😿 → traurige Katze

Gesichtsausdruckserkennung

Lächeln 😸 → glückliche Katze

Echtzeit

Live-Video von deiner Webcam mit Anzeige der aktuellen Katze

Sound (optional)

Spielt passende Sounds ab, wenn Lautsprecher verfügbar

Installation

Repository klonen:

git clone https://github.com/DEIN-BENUTZERNAME/cat_ai.git
cd cat_ai


Abhängigkeiten installieren:

pip install -r requirements.txt

Verwendung

Schnellstart:

python main.py


Steuerung:

q → Anwendung schließen

💡 Hinweis: Du kannst eigene Bilder oder Sounds in imgs/ und sounds/ hinzufügen. Die Erkennung wird automatisch angepasst.

Projektstruktur
cat_ai/
├── main.py          # Hauptskript
├── imgs/            # Katzenbilder
├── sounds/          # Sounds für Gesten
├── requirements.txt # Python-Abhängigkeiten
└── README.md        # Diese Datei

Anforderungen

Python 3.12+

OpenCV

MediaPipe

NumPy

Pillow

Pygame

Lizenz

MIT License – siehe LICENSE
