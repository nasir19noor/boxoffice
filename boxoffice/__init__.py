import requests
from bs4 import BeautifulSoup

def extract():
    try:
        response = requests.get("https://www.imdb.com/chart/boxoffice/")
    except Exception:
        return None

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        movies = soup.select("td.titleColumn")
        income = soup.select("td.ratingColumn")
        weeks = soup.select("td.weeksColumn")
        result = []
        for i in range(0,10):
            movies_title = movies[i].get_text().split(",")[0].strip()
            weekend = income[i*2].get_text().split(",")[0].strip()
            gross = income[i*2+1].get_text().split(",")[0].strip()
            weeks_long = weeks[i].get_text()
            data = {"movie": movies_title,
                    "weekend": weekend,
                    "gross": gross,
                    "weeks": weeks_long
                }
            result.append(data)
        i = 0
        for movie in result:
            i+=1
            print(f"{i}. {movie['movie']} - {movie['weekend']} - {movie['gross']} - {movie['weeks']}")
    else:
        return None

