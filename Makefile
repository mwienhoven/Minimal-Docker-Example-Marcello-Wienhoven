.PHONY: ingest preprocess train serve

# Ingest data
ingest:
	docker build -t ingest -f ./ingest/ingest.Dockerfile ./ingest
	docker run --rm -v "$(PWD)/data:/app/data" ingest


