FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt || true

CMD ["python", "-m", "Dark_rpg.main", "--auto", "--script", "Dark_rpg/master_script.txt"]
