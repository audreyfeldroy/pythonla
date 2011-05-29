============
Contributing
============

Setup
=====

Fork on github
--------------

Before you do anything else, login/signup on Github.com and fork pythonla from https://github.com/LAPython/pythonla.

Clone your package locally
--------------------------

If you have git-scm installed, you now clone your git repo using the following command-line argument where <my-github-name> is your account name on github::

    git clone git@github.com/<my-github-name>/pythonla.git

As you work, pull upstream changes into your fork regularly
===========================================================

Nothing is worse than putting in a day of hard work into a pull request, only to have it rejected because it has diverged too far from master. 

To pull in upstream changes and merge them::

    git remote add pythonla git://github.com/LAPython/pythonla.git
    git fetch pythonla
    git merge pythonla/master

Submitting your work
====================

Commit and push to your repo::

    git add <filenames-that-you-changed>
    git commit -m "Message describing what you changed."
    git push

Then submit a pull request.  If it's a major code change, have Michael review your pull request and merge it into master.
