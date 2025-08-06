FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y portaudio19-dev ffmpeg

# Set workdir
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Optional: expose port if needed, for example
# EXPOSE 8080

# Start your app
CMD ["python", "app.py"]
