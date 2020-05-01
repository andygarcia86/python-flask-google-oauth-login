# build
FROM python:3.7.4-slim AS build

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y \
    python3-dev

WORKDIR /

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

RUN pip3 install --user -r requirements.txt

# Remove the requirements.txt file
RUN rm -R requirements.txt

COPY /app /app

ENTRYPOINT [ "python" ]

CMD [ "/app/app.py" ]