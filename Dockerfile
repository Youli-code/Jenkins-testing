FROM python:3.10-slim

WORKDIR /app

COPY dark.py master_script.txt . 

CMD ["python", "dark.py", "--auto", "--script", "master_script.txt"]

