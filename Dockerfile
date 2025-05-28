# It will get python 3.9 slim buster image.
FROM python:3.9-slim-buster

# updating apt package manager and installing awscli for deployment.
RUN apt update -y && apt install awscli -y
WORKDIR /app

# copying all the code inside the /app folder.
COPY . /app
RUN pip install -r requirements.txt

# using python'3' because it is a linux command.
CMD ["python3", "app.py"]

