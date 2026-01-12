
# Flask und notwendige Module importieren
from flask import Flask, render_template, request

# Flask-App initialisieren
# __name__ sagt Flask, wo es nach Templates und Static-Files suchen soll
app = Flask(__name__)

# ============================================================
# ROUTE 1: Homepage / Landing Page
# ============================================================
@app.route('/')
def index():
    """
    Zeigt die Startseite an.
    Hier sollen User sehen, worum es geht und können sich anmelden.
    
    URL: http://localhost:5000/
    Method: GET (nur Seite anzeigen)
    """
    return render_template('index.html')


# ============================================================
# ROUTE 2: Anmeldeformular
# ============================================================
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Zeigt das Anmeldeformular an (GET) oder verarbeitet die Anmeldung (POST).
    
    GET:  Formular anzeigen
    POST: Formulardaten empfangen und verarbeiten
    
    URL: http://localhost:5000/signup
    """
    
    # Wenn Formular abgeschickt wurde (POST-Request)
    if request.method == 'POST':
        # Formulardaten aus dem Request holen
        user_name = request.form.get('user_name')
        email = request.form.get('email')              # Email-Adresse des Users
        
        # ======= HIER KOMMT SPÄTER DIE DB-LOGIK =======
        # TODO: User in die Datenbank eintragen
        # TODO: Bestätigungs-Email verschicken
        # TODO: Token für Email-Bestätigung generieren
        # ===============================================
        
        # Erstmal nur: Success-Page anzeigen
        return render_template('success.html',user_name=user_name, email=email)
    
    # Wenn nur die Seite aufgerufen wird (GET-Request)
    return render_template('signup.html')


# ============================================================
# ROUTE 3: Abmeldung (für Links in Emails)
# ============================================================
@app.route('/unsubscribe/<int:user_id>')
def unsubscribe(user_id):
    """
    Meldet einen User ab.
    Diese Route wird über einen Link in den verschickten Emails aufgerufen.
    
    URL: http://localhost:5000/unsubscribe/123
    user_id wird aus der URL extrahiert (z.B. 123)
    
    Parameter:
        user_id (int): Die ID des Users aus der Datenbank
    """
    
    # ======= HIER KOMMT SPÄTER DIE DB-LOGIK =======
    # TODO: User mit dieser ID in der DB als "gelöscht" markieren
    # TODO: deleted_at Timestamp setzen
    # ===============================================
    
    # Bestätigungsseite anzeigen
    return render_template('unsubscribe.html', user_id=user_id)


# ============================================================
# ROUTE 4: Email-Bestätigung
# ============================================================
@app.route('/confirm/<token>')
def confirm_email(token):
    """
    Bestätigt die Email-Adresse eines neuen Users.
    Der Token wird in der Bestätigungs-Email mitgeschickt.
    
    URL: http://localhost:5000/confirm/abc123xyz456
    token ist ein einzigartiger String zur Verifizierung
    
    Parameter:
        token (str): Eindeutiger Bestätigungstoken
    """
    
    # ======= HIER KOMMT SPÄTER DIE DB-LOGIK =======
    # TODO: Token in der DB suchen und validieren
    # TODO: User als "bestätigt" markieren
    # TODO: Ablaufdatum des Tokens prüfen
    # ===============================================
    
    # Bestätigungsseite anzeigen
    return render_template('confirm.html')

@app.route('/api/categories')
def get_categories():
    """
    Gibt alle verfügbaren Kategorien zurück (als JSON).
    
    URL: http://localhost:5000/api/categories
    """
    # Dummy-Kategorien
    categories = [
        "Motivation",
        "Philosophy", 
        "Wisdom",
        "Work",
        "Self-Development",
        "Resilience"
    ]
    
    return {"categories": categories}

# ============================================================
# FLASK-APP STARTEN
# ============================================================
if __name__ == '__main__':
    """
    Startet den Flask-Development-Server.
    
    debug=True bedeutet:
    - Änderungen am Code werden automatisch neu geladen
    - Ausführliche Fehlermeldungen im Browser
    - NICHT für Production verwenden!
    
    Server läuft auf: http://localhost:5000
    """
    app.run(debug=True)