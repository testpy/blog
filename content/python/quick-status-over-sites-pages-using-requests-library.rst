Quick status over sites pages using requests library
####################################################

:date: 2014-03-24
:tags: requests, functional, yaml, bs4
:category: python
:slug: quick-status-codes-with-requests
:author: Bianca Pirte
:email: biancapirte@gmail.com
:about_author: Test engineer
:summary:


Prerequisites
-------------

.. sourcecode:: python

    $ pip install PyYAML
    $ pip install requests
    $ pip install BeautifulSoup4


Let's start with a yaml config where we store data we will use in this script:

.. sourcecode:: python

    ---
    url: http://explorerproducer.lunchbox.pbs.org/home/
    title: Home | explorerproducer.lunchbox.pbs.org | PBS
    status_code: 200
    ---

    url: http://explorerproducer.lunchbox.pbs.org/video/
    status_code: 200
    title: Video | explorerproducer.lunchbox.pbs.org | PBS
    mandatory_text: "some text existent in this page you can verify"
    ---

    url: http://explorerproducer.lunchbox.pbs.org/page_does_not_exist/
    status_code: 404
    title: wrong title page
    mandatory_text: "All it takes is one bad page. Click one of the good pages below to return to our content."
    ---

    url: http://explorerproducer.lunchbox.pbs.org/celerity/
    title: Celerity | explorerproducer.lunchbox.pbs.org | PBS
    status_code: 200


...feel free to add/remove any fields you consider important to receive quick
status. (this are my first checkpoints)


1. response.status_code (Succes, Error, Forward and redirection ..)
-------------------------------------------------------------------

When testing/automating a web app one of the first things you do is typeing the
url in a browser or perform a get("url") using any open source tool for testing
web app.  What is the first response the server sends for your request? Why
don't we use this basic information - the status codes, as a first checkpoint?
(status_code from requests API offers us the integer code of responded HTTP
Status, e.g. 404 or 200.) First, let's  create the response object based on
each page url stored in the yaml and than we use `status_code` that will return
an integer code of responded HTTP status, e.g. 404 or 200.

.. sourcecode:: python

    my_response = requests.get(page_info['url'])
    print my_response.status_code

As you can see the output is an integer code of responded HTTP Status. You can
now play with it, add different error messages for server errors or redirects
and so on.

We can validate against data from yaml config, or just log information in the
txt file and than review. (you decide which is more valuable for you)

Ok, now we have first status server responses with but let's try gather some
more information.


2. Verify page content
----------------------

Verify title is the one you expected or verify some text is displayed in the
page content (of course this will not guarantee the display is proper, this
type of testing is covered by other tools). For pulling data out of HTML
response content we will use `Beautiful Soup
<http://www.crummy.com/software/BeautifulSoup/>`_.

First we create the method for extracting the title

.. sourcecode:: python

    def get_page_title(html):
        soup = BeautifulSoup(html)
        return soup.title.string

and now use the method to validate the title is the one we expected.

.. sourcecode:: python

    my_response = requests.get(page_info['url'])
    # now we need the html content -> my_response.content
    print get_page_title(my_response.content)

Again, feel free to display what information you need and how you need it.
Maybe there is some text that if not displayed the test should stop. Maybe you
want to log the text that was verified and received successful...


3. Time statistics
------------------

How about some statistics about the amount of time elapsed between sending the
request and the arrival of the response?

Many servers will accept a connection and then hold it until it is ready to
process. This backlog of requests can slow down the response time. If logging
this statistics for each build of your web app you can easily see if new
features have impact over the performance of your time to load page by
comparing the results in time.

The amount of time elapsed between sending the request and the arrival of the
response as a timedelta is not the same with the time to load a page, it is
only a part of it, the one related to server processing the requests. If
elapsed time is more than a few hundred milliseconds, you may have investigate
if you have some bottlenecks on your server.

Let's gather some time statistics too in order to have comparison metrics too:


.. sourcecode:: python

    import requests
    import yaml
    from bs4 import BeautifulSoup


    def get_page_title(html):
        soup = BeautifulSoup(html)
        return soup.title.string

    def get_page_status():
        site_page_url_list = yaml.load_all(open('config.yml','r'))
        input_list = []
        for e in site_page_url_list:
            input_list.append(e)

        fp = open('site_pages_status.txt', 'a')
        for page_info in input_list:
            my_response = requests.get(page_info['url'])
            fp.write(
                "\nGET %s \n Status code %s \n Done in %s" % (page_info['url'],
                my_response.status_code, my_response.elapsed)
            )
            print "\nGET %s \n Status code %s \n Done in %s" % (
                page_info['url'], my_response.status_code, my_response.elapsed
            )

            if not (page_info['title'] == get_page_title(my_response.content)):
                print "Fail - check page title for - %s" % (page_info['url'])
                fp.write("Fail - check page title for - %s" % (page_info['url']))

            if not (my_response.status_code == page_info['status_code']):
                print "Error - check page %s" % (page_info['url'])
                fp.write("Error - check page %s" % (page_info['url']))
        fp.close()

    def main():
        get_page_status()

    if __name__ == '__main__':
        main()

Remember this is the output I considered contains important data necessary for
my web app. You can configure the py  script / yaml different in order to
obtain valuable data for your web app. We only used three from many others
methods requests library offers. Take a look at `requests
<http://docs.python-requests.org/en/latest/api/>`_ api and play with it in
order to add new, more complex or simple test scenarios.
