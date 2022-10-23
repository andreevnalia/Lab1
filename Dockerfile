FROM python:3.10.6-slim
ENV FLASK_APP=__init__.py
COPY requirements.txt /opt/Lab1/
RUN python3 -m pip install -r /opt/Lab1/requirements.txt
COPY ./ /opt/Lab1/
WORKDIR /opt/Lab1/api_project/
CMD flask run --host 0.0.0.0 -p 5000