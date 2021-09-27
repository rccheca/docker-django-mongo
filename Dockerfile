FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#CMD tail -f /dev/null
#RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]