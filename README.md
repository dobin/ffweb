# FFWeb

A web gui for FFW (Fuzzing For Worms) fuzzing framework.


## Install

```
sudo pip install django djangorestframework whitenoise
```

## Run in production

```
export DJANGO_SECRET_KEY='<key>'
export DJANGO_DEBUG="" # enables prod
```


## Screenshots 

Sorry, may contain 0-days, therefore badly obfuscated most of the text. 

Overview of fuzzed projects: 

![Overview](https://raw.githubusercontent.com/dobin/ffweb/master/docs/ffweb-overview.png)

Details of all crashes of an project, unique'd:

![Project](https://raw.githubusercontent.com/dobin/ffweb/master/docs/ffweb-project.png)


Details of a crash: 

![Details](https://raw.githubusercontent.com/dobin/ffweb/master/docs/ffweb-details.png)
