import requests
from send_email import send_email

topic = "ukraine"
api_key = "421fc6fbe4d74593bbaf5dca3929cf22"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=421fc6fbe4d74593bbaf5dca3929cf22&" \
      "language=en"

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()
print(content)

# Loop through the articles. Set limits to 20.
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Todays news " \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

# Set the language option. Send the articles to email
body = body.encode("utf-8")
send_email(message=body)
