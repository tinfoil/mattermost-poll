FROM python:alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

EXPOSE 5000

RUN mkdir app
WORKDIR app
COPY *.py ./
COPY help.md ./

ENTRYPOINT ["python", "run.py"]
