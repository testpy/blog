Lettuce and django test client
##############################

:date: 2013-02-01
:tags: functional, lettuce, django test client, selenium
:category: python
:slug: lettuce-and-django-test-client
:author: Dan Claudiu Pop
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:email: danclaudiupop@gmail.com


When running a functional test, you fire up “browser” and do the "same" actions
as a real user (or API client). There are different “browsers” for testing your
applications, some of them are real, like selenium and some of them are less
real, like django test client. Depending on the context, each of them has its
pros and cons.

- django test client is very fast, since you don’t need a browser engine, real
  http listening and so on, but JavaScript and/or Ajax views are not tested
- selenium is a browser-driving library, opens a real browser and tests
  rendered HTML alongside with behavior of Web pages. Write selenium tests for
  Ajax, other JS/server interactions.

A complete test suite should contain both test types.

Functional tests and Django
===========================

Write functional/integration/system (has more names than it needs) tests for
views. Unit testing the view is hard because views have many dependencies
(templates, db, middleware, url routing etc).

You should definitely have django functional tests but chances are you should
have fewer than you have now. See the `software testing pyramid
<https://github.com/kmike/django-webtest>`_ by Alister Scott which provides
solid approach to automated testing and shows the mix of testing a team should
aim for.

**Functional tests:**

- test that the whole integrated system works, catch regressions
- they tend to be slow
- will catch bugs that unit tests will not, but it's harder to debug
- write fewer (more unit tests)


**So what can you test with django-test client ?**

- the correct view is executed for a given url
- simulate post, get, head, put etc. requests
- the returned content has the expected values (you can use beautiful soup,
  lxml or html5lib for parsing the content)

Example
=======

.. sourcecode:: python

    Feature: Register
        In order to get access to app
        A user should be able to register


    Scenario: User registers
        Given I go to the registration page
        When I fill register form with:
            | username | email       | password1 | password2 |
            | danul    | dan@dan.com | test123   | test123   |
        And I submit the data
        Then I should see "Check your email"
        And I should receive an email at "dan@dan.com" with the subject "Activate your djangoproject.com account - you have 7 days!"
        And I activate the account
        Then I should see "Congratulations!"

.. sourcecode:: python

    @step(u'I go to the register page')
    def i_go_to_the_register_page(step):
        response = world.browser.get(reverse('registration_register'))
        assert_equals(response.status_code, 200)
        world.html = BeautifulSoup(response.content)


    @step(u'When I fill register form with:')
    def when_i_fill_in_user_data_with(step):
        for data in step.hashes:
            world.data = data
        assert_equals(len(world.html.select('form')), 1)
        assert_equals(len(world.html.find_all('input', 'required')), 4)


    @step(u'And I submit the data')
    def and_i_submit_the_data(step):
        world.response = world.browser.post(
            reverse('registration_register'),
            world.data,
            follow=True
        )
        assert_equals(
            User.objects.filter(username=world.data['username']).exists(), True
        )
        assert_equals(world.response.status_code, 200)


    @step(u'I should see "(.*)"')
    def i_should_see(step, expected_response):
        html = BeautifulSoup(world.response.content)
        expected_text = html.find('h1').get_text()
        assert_equals(expected_text, expected_response)


    @step(u'And I should receive an email at "([^"]*)" with the subject "([^"]*)"')
    def i_should_receive_email_with_subject(step, address, subject):
        assert_equals(mail.outbox[0].to[0], address)
        assert_equals(mail.outbox[0].subject, subject)


    @step(u'And I activate the account')
    def and_i_activate_the_account(step):
        activation_url = re.findall(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            mail.outbox[0].body
        )
        world.response = world.browser.get(activation_url[0], follow=True)
        assert_equals(world.response.status_code, 200)

What's next ?
=============

Well ... WebTest  :) (http://pyvideo.org/video/699/testing-and-django)

Be a good person and write functional tests. Functional testing is something
that every app needs, no testing strategy is complete without high-level tests
to ensure the entire programming system works together.

