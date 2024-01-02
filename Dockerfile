FROM python:3.10.13-alpine3.19

RUN apk add --no-cache gcc libc-dev

RUN mkdir -p /handsdown
RUN mkdir -p /app
WORKDIR /handsdown

ADD ./handsdown ./handsdown
ADD ./LICENSE ./LICENSE
ADD ./pyproject.toml ./pyproject.toml
ADD ./setup.cfg ./setup.cfg
ADD ./README.md ./README.md

RUN adduser \
    --disabled-password \
    --home /home/app \
    handsdown

USER handsdown

ENV PATH "$PATH:/app/.local/bin"
RUN python -m pip install -U pip
RUN python -m pip install --no-cache-dir .

WORKDIR /app

ENV PYTHON_VER "3"

ENTRYPOINT ["handsdown"]
