FROM python:3-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python ./api.py


# Add your instructions to dockerize the application
# App must run on port 8000
