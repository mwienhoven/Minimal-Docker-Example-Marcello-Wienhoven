from model import TextClustering
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
from loguru import logger


# Load the processed data
datadir = Path("data/processed")
if not datadir.exists():
    logger.info(f"Creating directory {datadir}")
    datadir.mkdir(parents=True)

# Read the data
datafile = datadir / Path("posts.parquet")
df = pd.read_parquet(datafile)
logger.info(f"Data shape: {df.shape}")

# Initialize the clustering model
clustering = TextClustering()

# Perform clustering
k = 100  # Number of clusters
X = clustering(df["text"], k=k, batch=True, method="PCA")
logger.info(f"Clustering completed with {k} clusters. Resulting shape: {X.shape}")

# Get cluster labels
labels = clustering.get_labels(df)

# Visualize the clusters
plt.figure(figsize=(10, 10))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels)

# Save the plot
imgdir = Path("./img")
if not imgdir.exists():
    print(f"Creating directory {imgdir}")
    imgdir.mkdir(parents=True)

imgfile = imgdir / Path("clustering.png")
plt.savefig(imgfile)
logger.info(f"Clustering plot saved to {imgfile}")
