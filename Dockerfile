# ---------- Builder Stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and tests
COPY app.py .
COPY test_app.py .

# Run automated tests
RUN pytest

# ---------- Runtime Stage ----------
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy only runtime dependencies from builder
COPY --from=builder /usr/local /usr/local

# Copy only application code (no tests)
COPY app.py .

# Run as non-root user
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]