# Stage 1: Build dependencies
FROM python:3.13-slim AS builder

# Install system dependencies needed for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libffi-dev \
    libssl-dev \
    libmariadb-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies into a temporary directory
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.13-slim

WORKDIR /app

# Install runtime dependencies + dos2unix for script compatibility
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmariadb-dev \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy app code and wait-for-it script
COPY . .

# Convert line endings and ensure script is executable
RUN dos2unix /app/wait-for-it.sh /app/start.sh && chmod +x /app/wait-for-it.sh /app/start.sh

EXPOSE 8085

CMD ["./wait-for-it.sh", "db:3306", "--", "./start.sh"]
