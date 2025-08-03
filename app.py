
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "DEIN_NEWS_DATA_API_KEY"

def get_top_news(year: int):
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": API_KEY,
        "country": "de",
        "language": "de",
        "from_date": f"{year}-01-01",
        "to_date": f"{year}-12-31",
        "category": "top",
        "page": 1
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    return [
        {
            "title": article.get("title"),
            "link": article.get("link"),
            "pubDate": article.get("pubDate"),
            "description": article.get("description")
        }
        for article in data.get("results", [])
    ]

@app.route('/api/news', methods=['POST'])
def get_news():
    data = request.get_json()
    birthdate = data.get('birthdate')
    years = int(data.get('years', 0))
    birth_year = int(birthdate.split("-")[0])

    headlines = []
    for i in range(1, years + 1):
        year = birth_year + i
        news = get_top_news(year)
        headlines.append({
            "year": year,
            "news": news
        })

    return jsonify({
        "birthdate": birthdate,
        "years": years,
        "news": headlines
    })

if __name__ == '__main__':
    app.run(debug=True)

