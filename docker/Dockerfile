# Start with the official Python 3.10 image as base
FROM python:3.10 AS python-base

# Set working directory and copy pyproject.toml
WORKDIR /autofl
COPY pyproject.toml .

# Install poetry in a single layer and configure it
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-ansi --without dev

# Copy the remaining application code
COPY . .

# Set environment variables
ENV PYTHONPATH=/autofl/src
ENV HYDRA_FULL_ERROR=1

# Define a health check command
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl --fail http://localhost:8000 || exit 1

# Set the default command to start the app
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "api.main:app", "--bind", "0.0.0.0:8000", "--timeout", "100000"]
