from pathlib import Path
from loguru import logger
from datetime import datetime
import pandas as pd
import re
from pandas import json_normalize
import json

# Check if data directory exists
datadir = Path("data/raw").resolve()
datadir.exists()

# Create data file path
datafile = datadir / "posts.json"

# Load JSON data into DataFrame
with datafile.open("r", encoding="utf-8") as f:
    df = json_normalize(json.load(f)["posts"], sep="_")

# Display first few rows of the DataFrame
df.head()


# Function to bin time into categories
def bin_time(time):
    if time < datetime(2017, 12, 1):
        return 0
    elif time < datetime(2018, 1, 1):
        return 1
    elif time < datetime(2018, 8, 10):
        return 2
    elif time < datetime(2019, 8, 1):
        return 3
    else:
        return 4


# Function to remove URLs from text
def remove_url(text):
    return re.sub(r"^https?:\/\/.*[\r\n]*", "", text)


# Preprocess DataFrame
df["time"] = df["post_metadata_time"].apply(pd.to_datetime, unit="s")
df["bintime"] = df["time"].apply(lambda x: bin_time(x))
df["text"] = df["text"].apply(lambda x: str(x).replace("\n", " "))
df["text"] = df["text"].apply(lambda x: remove_url(x))
df["text"] = df["text"].apply(lambda x: x.lower())
df["size"] = df["text"].apply(lambda x: len(str(x)))
df = df[df["size"] > 50]
df.reset_index(inplace=True, drop=True)

# Save processed DataFrame to Parquet file
processeddir = Path("data/processed").resolve()
if not processeddir.exists():
    logger.info(f"Creating directory {processeddir}")
    processeddir.mkdir(parents=True)
outputfile = processeddir / Path("posts.parquet")
df.to_parquet(outputfile)

logger.success(f"Preprocessed data saved to {outputfile}")
