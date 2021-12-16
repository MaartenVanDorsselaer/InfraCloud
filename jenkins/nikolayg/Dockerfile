FROM python:3.6.0
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/home/spa/
WORKDIR /home/spa
EXPOSE 5081
CMD python3 main.py