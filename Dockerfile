# Official Python 3.13 Image with UV Installed
FROM python:3.13.2-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.10 /uv /uvx /bin/

# Set the Working Directory
WORKDIR /app

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install System Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    netcat-traditional \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Place executables in environment.
ENV PATH="/app/.venv/bin:$PATH"

# Copy the django project into the container.
COPY . .

# Install dependencies.
RUN uv sync --no-cache

# Copy the `entrypoint.sh` and set permissions.
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the port.
EXPOSE 8000

# Set entrypoint to wait for DB to be ready
ENTRYPOINT [ "/entrypoint.sh" ]