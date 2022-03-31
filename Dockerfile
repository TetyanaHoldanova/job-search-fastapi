FROM python:3.7

EXPOSE 80

COPY . /app


RUN pip install -r /app/app/requirements.txt

WORKDIR /app
RUN ls

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]