import requests
from pathlib import Path
from loguru import logger
import re


# Function to download a file from a URL to a specified path
def download(url, datafile: Path):
    datadir = datafile.parent
    if not datadir.exists():
        logger.info(f"Creating directory {datadir}")
        datadir.mkdir(parents=True)

    if not datafile.exists():
        logger.info(f"Downloading {url} to {datafile}")
        response = requests.get(url)
        with datafile.open("wb") as f:
            f.write(response.content)
    else:
        logger.info(f"File {datafile} already exists, skipping download")


# Main dataset URL and local path
url = "https://raw.githubusercontent.com/jkingsman/JSON-QAnon/main/posts.json"
datadir = Path("data/raw")
datafile = datadir / Path("posts.json")

# Download the main dataset
download(url, datafile)

# Download Tanach books
books = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "1%20Samuel",
    "2%20Samuel",
    "1%20Kings",
    "2%20Kings",
    "Isaiah",
    "Jeremiah",
    "Ezekiel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
]

# Install the books
for book in books:
    url = f"https://www.tanach.us/Server.txt?{book}*&content=Accents"
    filename = re.sub(r"%20", "_", book)
    datafile = datadir / "tanach" / Path(f"{filename}.txt")
    download(url, datafile)
