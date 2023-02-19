from googletrans import Translator
from bs4 import BeautifulSoup

# Load the HTML file and parse it with BeautifulSoup
with open('index.html', 'r', encoding='utf-8') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# Create a translator object
translator = Translator()

# Find all title and snap tags and translate their contents to Hindi
for tag in soup.find_all(['title','a', 'span', 'h1', 'h2', 'h3', 'h4', 'p', 'strong']):
    original_text = tag.string
    if original_text:
        translated_text = translator.translate(
            original_text, src='en', dest='hi').text
        tag.string.replace_with(translated_text)

# Save the translated HTML to a new file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
