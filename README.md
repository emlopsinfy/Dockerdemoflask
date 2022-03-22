this is the code for my medium article
https://medium.com/@aknsmb/running-a-flask-app-in-a-docker-containers-with-vs-code-docker-extension-6e6a2460fcd7

docker build . -t dockerdemoflask:latest

docker run -p 5000:5000 dockerdemoflask:latest

The flask app will not be running on docker build, only while you do docker run, it will host the app.