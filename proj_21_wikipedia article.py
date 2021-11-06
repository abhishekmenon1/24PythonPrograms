# The program searches Wikipedia and fetches a random article. Then it asks the user if he wants to read that article
# or not. If the answer is yes, the material is shown; otherwise, another random report is presented.

# Code learnt from: www.codesnail.com

import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    random_page = requests.get("https://en.wikipedia.org/wiki/Special:Random")  # Getting a random page from wikipedia
    soup = BeautifulSoup(random_page.content, "html.parser")              # Parsing out the information of that webpage
    title = soup.find(class_="firstHeading").text                               # gets the title of the page

    print(f"\n{title}")

    # asking the user whether they want to read the page
    user = input("Do you want to read about this topic?(Yes/No) :\n")
    user.lower()

    if user == "yes":
        url = "https://en.wikipedia.org/wiki/%s" % title    # opening webpage
        webbrowser.open(url)

    elif user == "no":
        print("hmm..how about this one?")   # looping for another title
        continue

    else:
        print("Enter either a YES or a NO.")
        continue
