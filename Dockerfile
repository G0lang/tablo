FROM python:2.7.16-slim-stretch
WORKDIR /usr/src/app
COPY requirements.txt ./
ENV IMG_URL https://s1.rationalcdn.com/vendors/stars-group/images/logos/logo.png
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "/usr/src/app/main.py"]
