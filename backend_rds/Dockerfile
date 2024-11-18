FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
#test2
COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]