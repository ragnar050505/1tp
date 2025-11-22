# Importation des modules nécessaires depuis Flask
from flask import Flask, request, redirect, url_for, render_template

# Création de l'application Flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Définition de la route pour traiter les données du formulaire
@app.route('/submit', methods=['POST'])
def submit():
    # Récupération des données du formulaire
    name = request.form['name']
    email = request.form['email']
    genre = request.form['genre']
    interets = request.form.getlist('interets')  # getlist pour récupérer toutes les cases cochées
    pays = request.form['pays']
    message = request.form['message']

    # Affichage des données dans la console (pour le débogage)
    print(f"Nom: {name}")
    print(f"Email: {email}")
    print(f"Genre: {genre}")
    print(f"Intérêts: {interets}")
    print(f"Pays: {pays}")
    print(f"Message: {message}")

    # Ici, vous pouvez ajouter le traitement des données
    # Par exemple, enregistrer dans une base de données ou envoyer un email

    # Redirection vers la page de remerciement en passant le nom en paramètre
    return redirect(url_for('thank_you', name=name))

# Définition de la route pour la page de remerciement
@app.route('/thank_you')
def thank_you():
    # Récupération du nom depuis les paramètres de l'URL
    name = request.args.get('name', 'Cher utilisateur')

    # Génération de la réponse HTML
    return f"<h1>Merci {name} !</h1><p>Votre message a été envoyé avec succès.</p>"

# Point d'entrée de l'application
if __name__ == '__main__':
    # Démarrage du serveur Flask en mode debug
    app.run(debug=True)