# tablo

Image to Dice Pattern convertor

[Original idea](https://youtu.be/yDU-0cN43eQ)


1. build image 
```
docker build -t tablo .
```

2. run 
```
docker run tablo
```

pass image url to container 
```
docker run -e IMG_URL=< image url > tablo
```

# TODO

- [ ] port to python3
- [ ] make it functional!
- [ ] show the result image with dices
- [ ] fix the problem of dice number 7 it should be transparent background in png
- [ ] optimize dockerfile make it multi stage and use smaler base image like alpine
