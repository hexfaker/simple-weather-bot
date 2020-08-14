#
# Create image with poetry
#
FROM python:3.8-slim-buster AS poetry
ENV \
    DEBIAN_ENVIRONMENT=noninteractive \
    LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=0

RUN pip install 'poetry>=1<=1.1'

#
# Infer requirements
#
FROM poetry AS requirements
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN  poetry export -f requirements.txt -o requirements.txt

#
# Create wheel
#
FROM poetry as build
WORKDIR /app
COPY poetry.lock pyproject.toml README.md LICENSE /app/
COPY simple_weather_bot/ /app/simple_weather_bot
RUN poetry build

#
# Final image
#
FROM python:3.8-slim-buster
ENV \
    DEBIAN_ENVIRONMENT=noninteractive \
    LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=0
WORKDIR /app
COPY --from=requirements /app/requirements.txt /app
RUN pip install -r requirements.txt
COPY --from=build /app/dist/*.whl ./
RUN pip install *.whl

ENTRYPOINT ["python", "-m", "simple_weather_bot"]
