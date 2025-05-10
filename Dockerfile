FROM python:3.13-slim
COPY --from=sikalabs/dogsay:v0.1.0 /usr/local/bin/dogsay /usr/local/bin/dogsay
RUN pip install --no-cache-dir --upgrade pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . .
CMD ["pipenv", "run", "python", "main.py"]
