#docker created from https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application

# FROM python:3.9

# # ENV VIRTUAL_ENV=env
# # RUN python3 -m venv $VIRTUAL_ENV
# # ENV PATH=”$VIRTUAL_ENV/bin:$PATH”

# COPY requirements.txt requirements.txt
# RUN pip3 install --upgrade pip && pip install -r requirements.txt
# RUN python3 -m nltk.downloader stopwords

# COPY . projcryptocurrently
# WORKDIR /projcryptocurrently

# EXPOSE 8020

# ENTRYPOINT ["python", "projcryptocurrently/manage.py"]
# CMD ["runserver", "0.0.0.0:8020"]

FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/cryptocurrently

RUN mkdir -p /opt/cryptocurrently/projcryptocurrently
COPY requirements.txt start-server.sh /opt/cryptocurrently/

COPY ./nltk_data /usr/local/nltk_data

COPY projcryptocurrently /opt/cryptocurrently/projcryptocurrently/
WORKDIR /opt/cryptocurrently
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/cryptocurrently
RUN chmod +x start-server.sh

EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/cryptocurrently/start-server.sh"]