10 pragmatic guidelines to maximize test usefulness
###################################################

:date: 2013-11-05
:tags: django, talks
:category: python
:slug: 10-pragmatic-guidelines-to-maximize-test-usefulness
:author: Dan Claudiu Pop
:email: danclaudiupop@gmail.com
:about_author: Test engineer, currently working @3PillarGlobal, interested in most aspects of software testing.
:summary: Testing Django Projects at Scale / Pycon CA 2013



.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/91-LiEb3sPE" frameborder="0" allowfullscreen></iframe>


ABSTRACT
========

**WHAT MAKES GOOD TESTS?**

- Tests should be as simple as possible.
- Tests should run as quickly as possible.
- Tests should avoid coupling with other tests.
- Tests should communicate intent.

**CANONICAL FORM OF A TEST**

- Setup pre-conditions.
- Perform operation under test.
- Make assertions.
- Benefits of following canonical form.

**TESTING TOOLS**

- Factories (instead of fixtures).
- Coverage.py
- django-nose + multiprocess

**GUIDELINES**

- Tests should be as simple as possible.
- Each test method tests one thing, and one thing only.
- Only set up the minimum needed pre-conditions for your test.
- Create your pre-conditions explicitly - don't use shared helper methods outside your module.
- Name your TestCase methods to indicate what they actually test.
- Use factories, not fixtures.
- Use django.tests.TestCase instead of unittest2.TestCase
- Create mixins, not shared TestCases.
- Segment your tests.
- Don't use setupClass() or tearDownClass()
