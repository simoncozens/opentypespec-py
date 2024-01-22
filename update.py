from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re

script_tags_url = "https://learn.microsoft.com/en-gb/typography/opentype/spec/scripttags"
lang_tags_url = "https://learn.microsoft.com/en-gb/typography/opentype/spec/languagetags"

r = requests.get(script_tags_url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find("table")
SCRIPT_TAGS = {}
for row in table.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) == 3:
        name, tag, description = columns
        m = re.search("'([A-Za-z0-9\s]{4})'", tag.text.strip())
        if m:
            tag = m.group(1)
        else:
            tag = tag.text.strip()
        tag = tag.replace("\xa0", " ") # Yi!
        SCRIPT_TAGS[tag] = {"name": name.text.strip()}

r = requests.get(lang_tags_url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find("table")
LANGUAGE_TAGS = {}
for row in table.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) == 3:
        name, tag, iso639 = columns
        iso639 = re.sub(r"See.*", "", iso639.text.strip()).split(", ") # Mon
        if not iso639[0]:
            iso639 = []
        m = re.search("'([A-Za-z0-9\s]{4})'", tag.text.strip())
        if m:
            tag = m.group(1)
        else:
            tag = tag.text.strip()
        LANGUAGE_TAGS[tag] = {
            "name": name.text.strip(),
            "iso639": iso639
        }

with open("opentypespec/tags/scripts.py", "w") as fh:
    fh.write("SCRIPT_TAGS = ")
    pprint(SCRIPT_TAGS, fh)

with open("opentypespec/tags/languages.py", "w") as fh:
    fh.write("LANGUAGE_TAGS = ")
    pprint(LANGUAGE_TAGS, fh)