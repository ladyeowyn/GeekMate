# Use the official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install build dependencies & clean up to keep image small
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create folder for SQLite & image uploads (ensure write perms)
RUN mkdir -p static/images

# Expose port
EXPOSE 5000

# Use Gunicorn for production-like server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
