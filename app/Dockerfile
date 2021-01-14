FROM python:3.4-alpine
ADD . /code
WORKDIR /code
EXPOSE 80
RUN pip install flask datetime pymongo[srv]
CMD ["python", "app.py"]

