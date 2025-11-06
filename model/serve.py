from model import TextClustering
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
from loguru import logger

datadir = Path("data/processed")
if not datadir.exists():
    logger.info(f"Creating directory {datadir}")
    datadir.mkdir(parents=True)
datafile = datadir / Path("posts.parquet")
df = pd.read_parquet(datafile)
df.head()

clustering = TextClustering()


k = 100
X = clustering(df["text"], k=k, batch=True, method="PCA")
X.shape

labels = clustering.get_labels(df)


plt.figure(figsize=(10, 10))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels)

imgdir = Path("../img")
if not imgdir.exists():
    print(f"Creating directory {imgdir}")
    imgdir.mkdir(parents=True)

imgfile = imgdir / Path("clustering.png")
plt.savefig(imgfile)
