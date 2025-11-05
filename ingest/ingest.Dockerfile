# Start from a lightweight Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY ingest.py .

# Install required Python packages
RUN pip install --no-cache-dir requests loguru

# Create the data directory (optional, since script will create it anyway)
RUN mkdir -p data/raw data/raw/tanach

# Set environment variable to avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Command to run the script
CMD ["python", "ingest.py"]
