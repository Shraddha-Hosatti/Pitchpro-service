FROM python:3.12

RUN mkdir app

ADD src/pitchpro /app/pitchpro
ADD vector_store /app/vector_store
ADD assets /app/assets

COPY src/main.py /app
COPY requirements.txt /app

WORKDIR /app
EXPOSE 8080

RUN python -m pip install -r /app/requirements.txt

ENTRYPOINT ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]
