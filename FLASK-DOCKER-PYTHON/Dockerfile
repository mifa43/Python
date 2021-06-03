FROM python:3.8.5-alpine

WORKDIR /app

ADD . /app 

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

# docker build -t python-test .  - tacka oznacava mesto gde se nalazi dockerfile
# docker run -it --name python-container -p 3200:3200 python-test : -it znaci pokreni u konzoli