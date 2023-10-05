FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/app

ENV DB_HOST=localhost
ENV DB_USER=root
ENV DB_PASSWORD=mauFJcuf5dhRMQrjj
ENV DB_NAME=forsit

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
