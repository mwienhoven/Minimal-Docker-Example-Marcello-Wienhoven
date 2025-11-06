# Makefile for data ingestion, preprocessing, model training, and serving
.PHONY: ingest preprocess serve model all cluster train serve # Define targets

# Ingest data
ingest:
	docker build -t ingest -f ./ingest/ingest.Dockerfile ./ingest
	docker run --rm -v "$$(pwd | sed 's|/c|C:|')/data:/app/data" ingest

# Preprocess data
preprocess:
	docker build -t preprocess -f ./preprocess/preprocess.Dockerfile ./preprocess
	docker run --rm -v "$$(pwd | sed 's|/c|C:|')/data:/app/data" preprocess

# Train model
model:
	docker build -t serve -f ./model/serve.Dockerfile ./model
	docker run --rm -v "$$(pwd | sed 's|/c|C:|')/data:/app/data" -v "$$(pwd | sed 's|/c|C:|')/img:/app/img" serve

# Complete pipeline
all: ingest preprocess model