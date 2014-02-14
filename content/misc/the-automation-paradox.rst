The automation paradox
######################

:date: 2014-02-14
:tags: agile, automation
:category: misc
:slug: automation-paradox
:author: Ramona Suciu
:email: ram.constantinescu@gmail.com
:about_author: Test lead engineer, wannabe aerobics instructor; I like shoes almost as much as testing. Currently working @3PillarGlobal, Cluj-Napoca.
:summary: Or simply put, it seems everyone wants to automate stuff, but there’s never enough time for it

One of the things I enjoy most is to establish the automation framework on a
new project, from simple setup on a local machine, until integration with a CI
server. In my opinion, this is often one of the most challenging parts, and
what follows afterwards, writing and maintaining the tests, is simply the fun
part :)

But what many do not seem to understand is that this is a time consuming
operation, especially when working on products already available on the market,
with legacy features still tested manually. In order for automation to succeed
on a project, my philosophy can be summed up to a few important action items:

- make everyone understand the importance and advantages brought by automation
  testing
- evangelize these advantages as much as you can with managers (so that you
  have their full support) and the clients
- not everyone is suited for automation testing. Some testers do a better job
  at exploratory or performance testing. And this is perfectly ok. Testers
  should be encouraged to specialize in the testing area they like the most, in
  order for them to do their job with passion and enthusiasm (but that’s
  another discussion, for another time :) ).
- you need a tester with a technical background, and very passionate about
  what’s new. Automation testers who keep themselves up to date tend to write
  less brittle tests, by trying to incorporate various tips&tricks into their
  tests.
- with the risk of repeating myself, use (at least in the beginning) just one
  or two automation testers, with experience on this area, until the automation
  framework is in place and fully running. Afterwards, it will be easier to
  increase the automation team, by cultivating such skills to other members of
  the team. As I also said above, writing and maintaining tests is a very fun
  job, once you got it going.

Unfortunately, although everybody is aware of the advantages, it seems that
more often than not, managers and clients prefer manual testing to investing
time and effort into automation. I believe this is because manual testing (for
new features) is faster, the testers doing this job know the product well and
can quickly assert the level of quality for new functionalities, and in such
cases, fast, high-level testing is preferred to long term testing, with a
larger coverage on the product’s features.

I am not saying that manual testing should be eliminated, because that is not
possible. Many times, it is more worth to manually test something, rather than
trying to automate that specific feature. However, what many do not seem to
take into account is the long-term advantages of automation testing. The
confidence that no regressions have been introduced and that the application
behaves well from functional point of view, while you are free to
automate/explore new features, is priceless when you try to make your product
successful.
