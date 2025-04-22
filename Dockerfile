FROM python:3.10-slim
WORKDIR /app

# Install build deps (pycairo, etc.)  
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential libcairo2-dev pkg-config python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements and strip hashes  
COPY requirements.txt .  
RUN sed -E '/--hash=/d' requirements.txt > req-nohash.txt

# Install without cache  
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r req-nohash.txt

# Copy app code and run  
COPY . .  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver"]
