import requests

def get_top_news(year: int, api_key: str):
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": api_key,
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
