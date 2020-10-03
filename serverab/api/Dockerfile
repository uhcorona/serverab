FROM python:2

COPY *.py ./

RUN pip install flask
RUN pip install Flask-PyMongo

EXPOSE 4000

RUN mkdir -p /elements/procs

CMD ["python", "app.py"]
