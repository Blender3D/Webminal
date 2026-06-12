FROM python:2.7

WORKDIR /var/www/webminal

# Install Python 2 dependencies
RUN pip install \
    flask==0.12.5 \
    Flask-SQLAlchemy==2.3.2 \
    Flask-Mail==0.9.1 \
    Flask-FlatPages==0.7.1 \
    Flask-Bcrypt==0.7.1 \
    Flask-WTF==0.14.3 \
    WTForms==2.2.1 \
    gunicorn==19.10.0 \
    gevent==1.4.0 \
    greenlet==0.4.17 \
    stripe==2.48.0 \
    rq==1.0 \
    redis==2.10.6 \
    requests==2.22.0 \
    Pygments==2.5.2 \
    email_validator==1.0.5 \
    SQLAlchemy==1.3.24

COPY . .

EXPOSE 1973

CMD ["gunicorn", "-k", "gevent", "--max-requests", "10", "--log-level", "debug", "--timeout", "600", "--threads", "2", "--workers", "2", "-b", "0.0.0.0:1973", "server:app"]
