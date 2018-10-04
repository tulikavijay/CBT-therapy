# docker build -t "cbt/therapy:1.0"
# docker run -d -p 8080:8000 --name cbt_1 cbt/therapy:1.0
# Access at http://localhost:8080/

FROM python:2.7-stretch

COPY . /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN python manage.py loaddata therapist.json

RUN python manage.py loaddata drawing_challenges.json 

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]