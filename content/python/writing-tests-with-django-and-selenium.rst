Writing tests with django and selenium
######################################

:date: 2013-04-25
:tags: functional, django, selenium
:category: python
:slug: writing-tests-with-django-and-selenium
:author: Ramona Suciu
:about_author: Test lead engineer, wannabe aerobics instructor; i like shoes almost as much as testing.
:email: ram.constantinescu@gmail.com


Getting our Selenium tests to run faster can be complicated at times, because
there are a number of factors to be taken into consideration. Debugging these
tests is time consuming and the end result is almost always the same one - a
large part of the tests needs to be refactored.

Luckily, for projects implemented with Django, we have the possibility to
explore a wide range of testing solutions, backed up by an active internet
community. Instead of always trying to use Selenium as a standalone solution,
we could analyze the possibility of having those tests integrated in our Django
project, and hence, be able to run with a simple command, all tests. By all
tests, I mean unit tests and functional tests.

For a practical example, please have a look at this `github
<https://github.com/ramonasuciu/django_selenium_tests>`_ repo. This is just an
example of how Selenium tests can be integrated with Django, with the use of
LiveServerTestCase class. Make sure to run pip install -r requirements.txt in a
virtualenv and you’re good to go.

The application used for testing is `django-registration
<https://bitbucket.org/ubernostrum/django-registration/>`_, which provides
enough support for developing functional tests. We inserted a js library
(password_strength_plugin.js) to better illustrate the need of Selenium
(JS/CSS/HTML focused) automated tests.

The advantages of this approach are numerous - you are able to test the
build as well, not only the deploy. Tests are faster, and, if you decide to
write your tests using a page object pattern method, then debugging will become
easier, as you’ll be able to faster track failures and their causes.
