Functional tests with django-webtest
####################################

:date: 2013-04-25
:tags: functional, django-webtest
:category: python
:slug: functional-tests-with-django-webtest
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: Why you should use django-webtest instead of django test client ?

I’ve been watching both presentations that Carl Meyer held at Pycon 2012/13 and
I highly recommend them if you want a deep dive into writing tests with django.
They outline some very good principles for writing effective and maintainable
tests. They also highlight a suite of test utilities and frameworks which help
you in writing better tests. Among the others, Webtest caught my attention via
`django-webtest <https://github.com/kmike/django-webtest>`_ for writing
integration/functional tests.


.. sourcecode:: python

    def testLoginProcess(self):
        login = self.app.get(reverse('auth_login'))
        login.form['username'] = 'danu'
        login.form['password'] = 'test123'
        response = login.form.submit('Log in').follow()
        assert_equals('200 OK', response.status)
        assert_contains(response, 'Welcome danu :]', count=1, status_code=200)

    def testLoginWithInvalidCredentials(self):
        login = self.app.get(reverse('auth_login'))
        login.form['username'] = 'foo'
        login.form['password'] = 'bar'
        response = login.form.submit('Log in')
        assert_contains(
            response,
            'Please enter a correct username and password. '
            'Note that both fields are case-sensitive.',
            count=1,
            status_code=200
        )

**Why you should choose django-webtest instead of django client ?**  Well,
first of all, it can better capture the user experience mainly because you can
submit forms and follow links. You are not only testing the views but also the
template html. Secondly, it will allow you to write more simple and readable
tests, an important fact when it comes to integration or functional tests.

It interacts with django via the WSGI interface so ajax, js will not be tested.
For that purpose you normally use selenium.

I’ve set up a project on `github
<https://github.com/danclaudiupop/django-lab-tests>`_ to illustrate some
automated tests with django-webtest. It uses nose test suite runner since i
don’t want to to import all my tests into tests/__init__.py and for rest of the
goodness that nose offers.
