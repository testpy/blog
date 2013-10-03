Using tail to explore logs
##########################

:date: 2013-10-03 12:30
:tags: unix
:category: misc
:slug: using-tail-to-explore-logs
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: Using tail to explore logs


When I am testing, I always keep an eye on the logs because they are a valuable
resource for finding problems on the system. They can act as an early warning
system. The ``tail`` commnand alongside with ``view`` or ``vim`` are great ways
to explore big log entries.

There is a slightly difference between the ``tail -f`` and ``tailf`` commands.
With ``tail -f`` you can basically do multitail like this:

.. sourcecode:: python

    >> tail -f web_app.log import.log

while ``tailf`` does not allow you to do multitail.

Ofcourse when there is too much noise you can pipe the output.

.. sourcecode:: python

    >> tail -f web_app.log import.log | grep ERROR
