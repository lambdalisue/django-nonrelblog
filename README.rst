Introduction
========================
`Google App Engine <http://code.google.com/intl/ja/appengine/>`_ doesn't support SQL but GQL.
That's why when you want to create `Django <https://www.djangoproject.com/>`_ app on Google App Engine, you have to rewrite models
for Google App Engine. Even if it is really simple application.

`Django-nonrel <http://www.allbuttonspressed.com/projects/django-nonrel>`_ is a branch version of
Django which support NoSQL database system. Using this branch, you can create an model used
NoSQL database system with nearly same format of SQL database system.

In this article, I'll show you how to use Django-nonrel on Google App Engine.


Demo
========
`Nonrelblog <http://nonrelblog.appspot.com/>`_ is a demo application of using Django-nonrel on Google App Engine.
It is a simple blogging system. Permission feature of the demo application is currently commented out.


Required packages
==================================
The packages below is required to run Demo application.

-   `Django-nonrel <http://www.allbuttonspressed.com/projects/django-nonrel>`_
-   `djangoappengine <http://www.allbuttonspressed.com/projects/djangoappengine>`_

    .. WARNING::
        Nonrelblog doesn't use official version of djangoappengine. The official version
        of djangoappengine doesn't allow to put python source files on ``ROOT/src/<project_name>``
        directory which I often use. Forked version of it is on https://bitbucket.org/lambdalisue/djangoappengine

-   `django-dbindexer <http://www.allonspressed.com/projects/django-dbindexer>`_
-   `django-autoload <http://www.allbuttonspressed.com/projects/django-autoload>`_
-   `djangotoolbox <http://www.allbuttonspressed.com/projects/djangotoolbox>`_
-   `django-qwert <http://github.com/lambdalisue/django-qwert/>`_


How to install Demo app
==============================================
First you have to install Google App Engine SDK for Python on your computer.
Follow the instruction of `official Google App Engine <http://code.google.com/intl/ja/appengine/downloads.html>`_ page.

Second open Terminal and execute commands below on your working directory.

Commands::

    git clone git://github.com/lambdalisue/django-nonrelblog.git
    cd django-nonrelblog
    ./utils/leadoff.sh install
    ./src/nonrelblog/manage.py syncdb
    ./src/nonrelblog/manage.py runserver

Finally, you can see simpleblog application on http://localhost:8080/

