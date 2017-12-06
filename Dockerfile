FROM python:2.7.14
COPY /app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["chop_demo.py"]
