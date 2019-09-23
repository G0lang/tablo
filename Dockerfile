FROM python:2.7.16-slim-stretch
WORKDIR /usr/src/app
COPY requirements.txt ./
# defualt IMG_URL 
ENV IMG_URL https://totallygaming.com/sites/default/files/the_stars_group_1.jpg
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "/usr/src/app/main.py"]
