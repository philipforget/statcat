statcat!
========

statcat is a simple Django app that makes tracking and displaying timestamped
stats simple. It is open source, so you can install it on your own system, and
will likely be a free hosted app for people at the hobby scale.


Goals
-----

The goal of statcat is to provide a REST and streaming api for collecting and
emitting arbitrary streams of data. This could take the form of temperature
tracking for various brewing processes, light levels in a plant growing setup,
or really any data that needs to be monitored over a period of time.

The front end for statcat should provide useful visual representation of the
data as well as providing triggers through the use of web hooks. For example,
make a POST request to a url when my fermentation chamber reaches a certain
temperature. Useful graphs should be as real time as possible to provide
adequate feedback for tuning temperature and motion controllers.


API
---

Schema forthcoming.
