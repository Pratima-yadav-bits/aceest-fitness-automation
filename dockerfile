# Use lightweight Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies including gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port (optional but good practice)
EXPOSE 5000

# Run Flask app with Gunicorn in production
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]