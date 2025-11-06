# Start from a lightweight Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY model.py serve.py /app/

# Install required Python packages from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create the data directory (optional, since script will create it anyway)
RUN mkdir -p /app/img /app/data

# Set environment variable to avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Command to run the script
CMD ["python", "serve.py"]
