Circular foreign key with factory_boy
#####################################

:date: 2014-02-09
:tags: factory_boy, unittest
:category: python
:slug: circular-foreign-key-factory-boy
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: factory_boy


Given the following state:

.. sourcecode:: python

    class Album(models.Model):
        thumb = models.ForeignKey('Image',  related_name='image')

    class Image(models.Model):
        album = models.ForeignKey('Album', null=True, blank=True)


with factory_boy:

.. sourcecode:: python

    class AlbumFactory(factory.DjangoModelFactory):
        FACTORY_FOR = 'app.Album'

        thumb = factory.SubFactory(
            'path.to.factories.ImageFactory'
        )

    class ImageFactory(factory.DjangoModelFactory):
        FACTORY_FOR = 'app.Image'

        album = factory.RelatedFactory(AlbumFactory, 'thumb')
