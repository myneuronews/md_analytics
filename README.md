# Social-media analytic tool



[![Build Status](https://travis-ci.org/mdyzma/md_analytics.svg?branch=master)](https://travis-ci.org/mdyzma/md_analytics)
[![Documentation Status](https://readthedocs.org/projects/md-analytics/badge/?version=latest)](http://md-analytics.readthedocs.io/en/latest/?badge=latest)


A Flask based app, which inspects social media accounts, displaying statistics, semantic analysis and friends/followers network graphs. followers of the followers of account authorized via Twitter. Can be deployed to Heroku.

## Usage

1. Visit [web site](https://md-analytics.herokuapp.com)



2. Sign in with one/all of social-mediar account/s
3. Browse lists, statistics and graphs of the dashboard:



Data are also accssible in JSON format:





## Deploying to Heroku

To deploy your copy of application simply click:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

(you will need Twitter app and SECRET CREDENTIALS provided by Twitter in order to make it work)

You can also quickly deploy using git. Make sure you have [HerokuCLI][HerokuCLI] installed.

```sh
$ git clone https://github.com/mdyzma/md_analytics.git
$ cd md_analytics
$ heroku create
$ git push heroku master
$ heroku open
```


## Running Locally

It can be also run locally. Make sure you have [Python][Python] and [HerokuCLI][HerokuCLI].

```sh
$ git clone https://gitlab.com/mdyzma/md_analytics.git
$ cd md_analytics
$ pip install --no-cache-dir -r requirements.txt

$ heroku local
```

Your app should now be running on [http://127.0.0.1:5000](http://localhost:5000/).














<!-- Links -->
[Python]:    http://install.python-guide.org
[HerokuCLI]: https://toolbelt.heroku.com

<!-- Images -->

[start]:     static/img/screen-start.png
[followers]: static/img/screen-followers.png
[followers_json]: static/img/screen-followers-json.png