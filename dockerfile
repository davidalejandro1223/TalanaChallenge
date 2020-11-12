FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/TalanaChallenge/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /opt/TalanaChallenge/TalanaChallenge

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]