:title: Running Pelican
:date: 2017-10-21
:category: Meta
:slug: running-pelican
:status: draft

Installing
----------

OSX is pre-installed with a version of the ``six`` module that is too
old for Pelican. The solution (recommended by Pelican themselves, I
think) is to use a ``virtualenv``.

I set up a ``virtualenv`` with this:

.. code:: bash

    sudo pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install pelican markdown  # without sudo!
    deactivate

Need to have the ``virtualenv`` *active* when running Pelican.

If you get an error, try ``python pip install <packages>`` instead.

Building a Site
---------------

After putting a Markdown post in the ``/content`` folder, we can
generate a site with:

.. code:: bash

    pelican content           # build site
    cd output
    python -m pelican.server  # serve locally

Going to `localhost:8000 <http://localhost:8000>`__, we can view the
completed site.

If the content directory is set in the `pelicanconf.py` file, then it can be ommitted from the `pelican` command to build the site. Also, the `-r` flag can be added so that it will watch for any changes to the files in `content` and automatically populate them in the output file.

The modified commands would then be:

.. code:: bash

    pelican -r                # build site and watch for changes
    cd output
    python -m pelican.server  # serve locally
