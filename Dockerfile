FROM python:3.11-slim

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y \
    gcc \
    portaudio19-dev \
    ffmpeg

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask 
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
