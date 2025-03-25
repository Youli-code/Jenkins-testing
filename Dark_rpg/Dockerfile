# Stage 1: Builder
FROM python:3.10-slim AS builder

WORKDIR /build

# Copy source files to build stage
COPY dark.py master_script.txt .

# (Optional) Install requirements or do prep here
# RUN pip install -r requirements.txt

# Stage 2: Final Runtime
FROM python:3.10-slim AS final

WORKDIR /app

# Copy only the necessary files from the builder
COPY --from=builder /build /app

# Default command to run the game in auto mode
CMD ["python", "dark.py", "--auto", "--script", "master_script.txt"]

