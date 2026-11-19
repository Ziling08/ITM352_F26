import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

bank = ""
print("Bank | Term/Type | Interest Rate (%) | Points (%) | APR (%)")

for row in rows:
    cells = row.find_all("td")

    if len(cells) == 0:
        continue

    if len(cells) == 5:
        bank = cells[0].find("b").get_text(strip=True)
        cells = cells[1:]

    values = []
    for cell in cells:
        value = cell.get_text(strip=True)
        if value == "":
            value = "N/A"
        values.append(value)

    print(bank, "|", values[0], "|", values[1], "|", values[2], "|", values[3])