import requests
from bs4 import BeautifulSoup

urls = [
    ("https://subwaysurf.fandom.com/wiki/Hoverboard", "Board.md"),
    ("https://subwaysurf.fandom.com/wiki/Characters", "Character.md"),
]

session = requests.Session()
for url, file_name in urls:
    completed_names = set()
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("- [x]"):
                    completed_names.add(line[5:].strip())
    except FileNotFoundError:
        pass

    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", {"class": "article-table"})
    if table is not None:
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")
        new_names = []
        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 2:
                name = cols[2].text.strip()
                if name not in completed_names:
                    new_names.append(name)

        with open(file_name, "a") as f:
            for name in new_names:
                f.write(f"- [ ] {name}\n")
    else:
        print("Unable to find table on page.")
