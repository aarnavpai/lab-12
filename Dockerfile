FROM python:3.13-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "python3", "-m", "uvicorn", "main:app" ]
