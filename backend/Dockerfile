# Backend Dockerfile for development
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy all backend files and folders
COPY pyproject.toml uv.lock ./
COPY run.py ./
COPY app ./app
COPY processed_data ./processed_data

# Install dependencies using uv
RUN uv sync --dev

# Expose port
EXPOSE 8000

# Run the development server
CMD ["uv", "run", "dev"]
