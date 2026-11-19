import requests
from bs4 import BeautifulSoup

url = "https://shidler.hawaii.edu/itm/people"
response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
print(type(soup))
lines = soup.prettify().splitlines()
for line in lines[:10]:
    print(line)

cards = soup.find_all("article", class_="node-faculty")
print("\nNumber of people cards:", len(cards))
print("\nFirst card HTML:")
print(cards[0].prettify())

print("\nNames and emails:")
names = []
for card in cards:
    name = card.find("h2").get_text(strip=True)
    email_section = card.find("div", class_="field-email")

    if email_section is not None:
        email = email_section.find("div", class_="field-item").get_text(strip=True)
    else:
        email = "Not listed"

    print(name, "-", email)

    # A person may appear in more than one section of the page.
    if name not in names:
        names.append(name)

print("Number of unique people:", len(names))
