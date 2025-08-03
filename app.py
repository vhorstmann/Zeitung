from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Erlaubt Cross-Origin-Anfragen vom Frontend

@app.route('/api/news', methods=['POST'])
def get_news():
    data = request.get_json()
    birthdate = data.get('birthdate')
    years = int(data.get('years', 0))

    # Simulierte Antwort mit Platzhalter-Schlagzeilen und Bildern
    headlines = [
        {
            "year": 2025 - i,
            "headline": f"Beispiel-Schlagzeile für {2025 - i}",
            "image": f"https://via.placeholder.com/150?text={2025 - i}"
        }
        for i in range(years)
    ]

    return jsonify({
        "birthdate": birthdate,
        "years": years,
        "news": headlines
    })

if __name__ == '__main__':
    app.run(debug=True)

