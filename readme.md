# Motivation

We are currently migrating our projects from [django](http://www.djangoproject.com) to [flask](http://flask.pocoo.org).
Since we also intend to use flask for entirely new projects, it made sense to save on initial setup time.
So we created a project skeleton which includes some of the things (libs and configuration) that we pick for most projects.

# Components

## General

here is a list of assembled components

* flask decorators for (cache_page, login_required)
* gae specific monkeypatch for werkzeug debugger [http://dev.pocoo.org/projects/werkzeug/wiki/UsingDebuggerWithAppEngine](http://dev.pocoo.org/projects/werkzeug/wiki/UsingDebuggerWithAppEngine)
* a simple user model
* google appengine specific development/production environment switch
* google appengine appstats configured
* google appengine memcache caching backend configured
* favicon.ico stub to avoid unneeded error logs
* deck module with 26 char uuid generator
* deck module with JsonProperty for the datastore
* lib directory for external dependencies prepended to syspath

## Libraries

### Python

* Flask
* Jinja
* werkzeug
* gaeUtils from deck [http://github.com/blossom/gae-utils](http://github.com/deck/gae-utils)
* gaePath [http://github.com/nikgraf/gae-path](http://github.com/nikgraf/gae-path)

# Dependencies

## General

* Python 2.5
* Google AppEngine SDK [http://code.google.com/appengine/downloads.html](http://code.google.com/appengine/downloads.html)

## Testing

* lxml [http://pypi.python.org/pypi/lxml](http://pypi.python.org/pypi/lxml)
* nose [http://pypi.python.org/pypi/nose](http://pypi.python.org/pypi/nose)
* NoseGAE [http://pypi.python.org/pypi/NoseGAE](http://pypi.python.org/pypi/NoseGAE)
* selenium 2+ [http://pypi.python.org/pypi/selenium](http://pypi.python.org/pypi/selenium)

# Setup

clone repository

    git clone https://github.com/blossom/flask-gae-skeleton.git <project_name>

change to directory of <project_name>

    cd <project_name>

fetch all the submodules via

    git submodule update --init

set your own appengine application id in app.yaml

change the 'secret_key' in settings.py by generating a new one

add replace remote

    git remote rm origin
    git remote add origin <new_remote like git@github.com:your_name/project_name.git>
    git commit -am "initial setup"
    git push origin master

# Update from Skeleton

Add the remote and merge in all changes and removes the old stuff again.

    git remote add skeleton https://github.com/blossom/flask-gae-skeleton.git
    git pull skeleton
    git checkout -b skeleton remotes/skeleton/master
    git rebase <your_development_branch like master>
    git checkout <your_development_branch like master>
    git merge --no-ff skeleton
    git branch -D skeleton
    git remote rm skeleton
    git submodule update

# Usage

## Run Application

Go to path "gae" and run

    dev_appserver.py .

## Run Test Enviroment

Go to path "gae" and run

    nosetests-2.5 --with-gae tests/

## Run Remote Console

Go to path "gae" and run

    python2.5 appengine_console.py <app-id>

# TODO

things we still need to extract and clean up from other projects

* add tests for decorators
* set port for testing via configuration in settings or test_settings
* kill subprocess dev_appserver for selenium tests also in windows (see python2.6 implementation how to kill a process)
* add coverage
* add fixture (http://farmdev.com/projects/fixture/using-fixture-with-appengine.html)
