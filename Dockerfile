FROM python:3
ENV PYTHONUNBUFFERED=1
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY req.txt ./
RUN pip install -r req.txt
EXPOSE 8000
CMD exec gunicorn event_registration.wsgi:application --bind 0.0.0.0:8000 --workers 3
