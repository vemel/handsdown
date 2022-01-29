FROM python:3.10.2-alpine3.15

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

ENV PYTHON_VER "3"

ENTRYPOINT ["handsdown"]
