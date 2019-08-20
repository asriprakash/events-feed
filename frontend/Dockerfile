FROM python:3.7
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
ENV GREETING 'Welcome to Events Feed'
RUN pip install gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app