Beginners guide to functionally test an API in Django
#####################################################

:date: 2014-03-06
:tags: django, functional, api
:category: python
:slug: guide-to-functionally-test-an-api-in-django
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary:


Bootstrapping
-------------

To set up our django development environment, we'll start by creating a
virtual environment. Execute the following commands in the terminal:

.. sourcecode:: python

    $ virtualenv temp
    $ source bin/activate


I've created a repo with a dummy app which exposes an api that contains a list
of musicians with albums, to serve as our testing ground. I used django rest
framework, dig into their `documentation
<http://www.django-rest-framework.org/>`_ if you want to build API's for your
application. `Clone the repository
<https://github.com/danclaudiupop/beginners-guide-to-functionally-test-an-api-in-django>`_
and then run `pip install -r requirements.txt` to install all dependencies.
With all of the dependencies set up, we're ready to move on and start the local
web server. You should be able to type `fab runserver` and browse to
http://127.0.0.1:8000/. You should see a list a musicians.

Laying the testing ground
-------------------------

Django test client is a good approach when it comes to these types of tests.
Let's create a simple test:


.. sourcecode:: python

    from django.test import TestCase
    from django.test.client import Client
    from django.core.urlresolvers import reverse


    class EndpointsTestCase(TestCase):

        def test_musician_with_albums_list_endpoint(self):
            url = reverse('musician-list')
            client = Client()
            response = client.get(url)
            print response.content

As we can see, no data is exposed when going to `/musicians/`. Let's create
a musician with some albums in `setUp`:

.. sourcecode:: python

    from django.test import TestCase
    from django.test.client import Client
    from django.core.urlresolvers import reverse


    class EndpointsTestCase(TestCase):

        def setUp(self):
            test_musician = Musician.objects.create(
                first_name='Foo',
                last=name='Bar',
                instrument='guitar'
            )
            album1 = Album.objects.create(
                musician=test_musician,
                name='Album1',
                release_date='2011-01-01',
                num_stars=5
            )
            album2 = Album.objects.create(
                musician=test_musician,
                name='Album2',
                release_date='2012-02-02',
                num_stars=4
            )

        def test_musician_with_albums_list_endpoint(self):
            url = reverse('musician-list')
            client = Client()
            response = client.get(url)
            print response.content


Now we have some data displayed in api. We can start to make some assertions.
But when we fetch the response body, it returns a string. We decode the json
document using `json.loads`. Create a helper function fetch_url which will
return a dictionary. We should now be able to loop through the results. The
code should look like this:

.. sourcecode:: python

    def fetch_url(url):
        client = Client()
        response = client.get(url)
        return json.loads(response.content)

    ...

    def test_musician_with_albums_list_endpoint(self):
        url = reverse('musician-list')
        response = client.fetch_url(url)
        self.assertEqual(len(response[0]['albums']), 3)


Factories
---------

Before we move on, let's take a look at the models. We will need to create
programmatically objects in database for testing when querying the endpoints.
You can use `factory_boy <https://factoryboy.readthedocs.org/en/latest/>`_
library (fixtures replacement), or any other library for that matter, but we'll
stick with a more raw approach, yet powerful enough to cover our needs. Back to
models relationships, everything looks straightforward, we can see the album
model has a field called musician, which is a foreign key to the musician
model. Let's create factory.py and map the models relationship into a factory
design:


.. sourcecode:: python

    from albumreview.models import Musician, Album


    class MusicianFactory(object):
        def __init__(self):
            self.counter = 0

        def __call__(self, first_name=None, last_name=None, instrument=None):
            if first_name is None:
                first_name = 'Foo%s' % self.counter
            if last_name is None:
                last_name = 'Bar%s' % self.counter
            if instrument is None:
                instrument = 'Blowfish%s' % self.counter

            musician = Musician.objects.create(
                first_name=first_name,
                last_name=last_name,
                instrument=instrument
            )
            self.counter +=1
            return musician


    class AlbumFactory(object):
        def __init__(self):
            self.counter = 0

        def __call__(self, musician, name=None, release_date=None, num_stars=None):
            if name is None:
                name = 'Album%s' % self.counter
            if release_date is None:
                release_date = '2014-03-03'
            if num_stars is None:
                num_stars = 5

            album = Album.objects.create(
                musician=musician,
                name=name,
                release_date=release_date,
                num_stars=num_stars
            )
            self.counter += 1
            return album


When creating records in db for testing, we can write in `setUp` something as:

.. sourcecode:: python

    def setUp(self):
        musician = MusicianFactory()
        album = AlbumFactory()
        for x in range(3):
            album(musician=musician())

This approach will bring us a few benefits, such as:

- creating objects with default data
- creating sequence of objects
- focus on tests not on creating records in db

At any time, you can override the default data with data specific to your
testing context:

.. sourcecode:: python

    musician = MusicianFactory()
    musician = musician(first_name='x', last_name='y')

After completing this tutorial, we have a good foundation to go and start
testing an API from a functional point of view.
