FROM python:3.7-slim

WORKDIR /home/neo

RUN pip install --upgrade pip
RUN pip install neo4j-driver

COPY src/ .

#CMD ["python", "./main_wrapper.py"]
CMD ["sh"]
