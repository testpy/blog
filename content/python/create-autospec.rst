Autospeccing your mocks
#######################

:date: 2014-02-03
:tags: mock, unittest
:category: python
:slug: auto-speccing
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: create a mock object using another object as a spec


Auto-speccing can be done through the `autospec` argument to patch, or the
`create_autospec` function. Auto-speccing creates mock objects that have the
same attributes and methods as the objects they are replacing, and any
functions and methods (including constructors) have the same call signature as
the real object.

Given that, if your mock is used in illegal ways, for e.g a mock method is
called with incorrect number of arguments, an exception will be thrown.  When
refactoring is happening and your tests still serve as living documentation,
tests that are using mocks without autospeccing flag will continue to pass.


.. sourcecode:: python

    from mock import create_autospec
    import unittest

    def foo(a, b):
        pass

    class FooTestCase(unittest.TestCase):

        def test_foo_spec(self):
            mock = create_autospec(foo)
            mock(1, 2)
            mock.assert_called_with(1, 2)
            mock.return_value = 10
            self.assertEqual(mock(1, 2), 10)
            self.assertRaises(TypeError, mock, 'only_one_arg')

    if __name__ == '__main__':
        unittest.main()
