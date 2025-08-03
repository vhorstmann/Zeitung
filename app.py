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


from fastapi import FastAPI, Query

app = FastAPI()

API_KEY = "DEIN_NEWS_DATA_API_KEY"

@app.get("/top-news")
def top_news(birthday: str = Query(...), years: int = Query(...)):
    birth_year = int(birthday.split("-")[0])
    news_results = []

    for i in range(1, years + 1):
        year = birth_year + i
        news = get_top_news(year, API_KEY)
        news_results.append({
            "year": year,
            "news": news
        })

    return {"results": news_results}

