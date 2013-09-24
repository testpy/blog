Getting up and running
----------------------

Pull down the repo and build the virtualenv.

    $ git clone
    $ mkvirtualenv testpy
    $ workon testpy
    $ pip install -r requirements.txt


Writing and testing
-------------------

Build the HTML and run dev server.

    $ make html
    $ make devserver


Publishing
----------

Commit content and images as required, push to master. Then...

    $ make publish
    $ make github

All good in the hood.
