FROM python:3.8
ARG DIR=/code

WORKDIR $DIR
# WORKDIR /code

RUN apt update

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]


# uWSGI will listen on this port
EXPOSE 8050

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi
# Start uWSGI
CMD [ "uwsgi", "--ini", "uwsgi.ini"]