FROM python:3.8.4-buster
COPY . /app
WORKDIR /app
RUN chmod 777 /app 
RUN apt -qq update
RUN apt -qq install -y bash
RUN pip install -r requirements.txt
CMD ["bash","start.sh"]