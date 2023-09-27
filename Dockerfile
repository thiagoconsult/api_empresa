FROM python:3.10

WORKDIR /api_empresa

COPY . /api_empresa


RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["python"]

# CMD ["run.py"]