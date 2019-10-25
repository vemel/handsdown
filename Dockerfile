FROM python:3.7.5-alpine3.10

RUN apk add --no-cache gcc libc-dev

RUN mkdir /handsdown
WORKDIR /handsdown

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD ./handsdown ./handsdown
ADD ./setup.py ./setup.py
ADD ./README.md ./README.md
RUN python setup.py install

RUN adduser \
    --disabled-password \
    --home /app \
    handsdown

USER handsdown
WORKDIR /app

ENTRYPOINT ["handsdown"]
