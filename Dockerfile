#FROM python:3.9-alpine3.13
FROM python:3.9
#LABEL maintainer="sergioev@gmail.com"

# it tells python that you don't want to buffer the output 
# it will printed directly from the console 
# it prevents delays 
#ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Install Python packages
RUN pip install --upgrade pip && \
  pip install -r /tmp/requirements.txt

COPY ./app /app
WORKDIR /app
EXPOSE 8000

# Install dependencies
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  postgresql-client && \
  rm -rf /var/lib/apt/lists/*




# to run any python command from the virtual environment we created 
#ENV PATH="/py/bin:$PATH"

#USER django-user



