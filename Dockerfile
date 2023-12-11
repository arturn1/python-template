FROM python:3.8-slim-buster

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

EXPOSE 8000

ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_PORT=8000
ENV PORT=9000
ENV FLASK_ENV=development
ENV USE_CACHE=False
ENV PYTHONDONTWRITEBYCODE=1

CMD ["gunicorn", "-b", ":8000", "wsgi:app"]