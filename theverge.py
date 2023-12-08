import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.theverge.com/"
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")
        articles = soup.find_all("h2", class_="font-polysans text-20 font-bold leading-100 tracking-1 md:text-24")

        with open("index.html", "w", encoding="utf-8") as file:
            file.write("<!DOCTYPE html>\n<html>\n<head>\n")
            file.write("<title>The Verge Articles</title>\n")
            file.write("<style>body {font-family: Arial, sans-serif;}</style>\n")
            file.write("</head>\n<body>\n")
            file.write("<h1>The Verge Articles</h1>\n<ul>\n")

            for article in articles:
                title = article.text.strip()
                link = article.find("a")["href"]
                file.write(f"<li><a href='{link}'>{title}</a></li>\n")

        print("HTML file generated: index.html")
    else:
        print(f"Failed to fetch content from {url}")

if __name__ == "__main__":
    main()
