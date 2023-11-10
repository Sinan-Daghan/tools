import requests, webbrowser, sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: python img_scraper.py <url>")
    sys.exit(1)

url = sys.argv[1]
print(f"The url passed is: {url}")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    img_elements = soup.find_all('img')

    if len(img_elements) == 0:
        print("No img elements found")
    elif len(img_elements) == 1:
        print("1 img element found")
    elif len(img_elements) < 11:
        print(f"{len(img_elements)} img elements found")
    else:
        print(f"{len(img_elements)} img elements found do you want to continue? (y/n)")
        response = input()
        if response.lower() != "y":
            print("Exiting...")
            sys.exit(1)

    for img in img_elements:
        src = img.get('src')
        print(f"Image Source: {src}")
        webbrowser.open(src)

else:
    print(f"HTTP error response status code : {response.status_code}")