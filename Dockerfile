# Use a lightweight Python image
FROM python:3.10-slim as builder

# Set workdir and copy project
WORKDIR /app
COPY . .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# Run the game (in auto mode with script if needed)
CMD ["python", "-m", "Dark_rpg.main", "--auto", "--script", "Dark_rpg/master_script.txt"]
