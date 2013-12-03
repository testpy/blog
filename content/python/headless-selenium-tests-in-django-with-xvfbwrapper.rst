Headless selenium tests in django with xvfbwrapper
##################################################

:date: 2013-11-29
:tags: functional, django, headless, xvfb, selenium
:category: python
:slug: headless-selenium-tests-in-django-with-xvfbwrapper
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: headless tests in django with xvfb


Install dependencies:

- ``sudo apt-get install xvfb``

- ``pip install xvfbwrapper``

This code uses selenium and xvfbwrapper to run tests with Firefox inside a
headless display.

.. sourcecode:: python

    from django.test import LiveServerTestCase
    from selenium.webdriver.firefox.webdriver import WebDriver
    from xvfbwrapper import Xvfb

    class SeleniumTestCase(LiveServerTestCase):

        @classmethod
        def setUpClass(cls):
            cls.xvfb = Xvfb(width=1280, height=720)
            cls.xvfb.start()
            cls.wd = WebDriver()
            super(SeleniumTestCase, cls).setUpClass()

        @classmethod
        def tearDownClass(cls):
            cls.wd.quit()
            super(SeleniumTestCase, cls).tearDownClass()
            cls.xvfb.stop()
