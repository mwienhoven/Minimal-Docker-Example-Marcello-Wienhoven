.PHONY: ingest preprocess train serve

# Ingest data
ingest:
	docker build -t ingest -f ./ingest/ingest.Dockerfile ./ingest
	docker run --rm -v "$$(pwd | sed 's|/c|C:|')/data:/app/data" ingest

preprocess:
	docker build -t preprocess -f ./preprocess/preprocess.Dockerfile ./preprocess
	docker run --rm -v "$$(pwd | sed 's|/c|C:|')/data:/app/data" preprocess