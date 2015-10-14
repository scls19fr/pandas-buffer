|Build Status|


!!! WORK IN PROGRESS !!! DON'T USE IT FOR NOW

Pandas Buffer
=============

A `Python <https://www.python.org/>`_ `Pandas <http://pandas.pydata.org/>`_ implementation of buffer.

Install
-------

.. code:: bash

    $ pip install pandas-buffer


Ring Buffer
-----------

Description
^^^^^^^^^^^

See `description of a ring buffer (or circular buffer) <https://en.wikipedia.org/wiki/Circular_buffer>`_.

Usage
^^^^^

.. code:: python

    In [1]: from pandas_buffer import RingBuffer

    In [2]: N = 10

Development
-----------

You can help to develop this library.

Issues
~~~~~~

You can submit issues using https://github.com/scls19fr/pandas-buffer/issues

Clone
~~~~~

You can clone repository to try to fix issues yourself using:

::

    $ git clone https://github.com/scls19fr/pandas-buffer.git

Run unit tests
~~~~~~~~~~~~~~

Run all unit tests

::

    $ nosetests -s -v

Run a given test

::

    $ nosetests tests.test_ring:test_ring -s -v

Install development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ python setup.py install

or

::

    $ sudo pip install git+https://github.com/scls19fr/pandas-buffer.git

Collaborating
~~~~~~~~~~~~~

-  Fork repository
-  Create a branch which fix a given issue
-  Submit pull requests


.. |Build Status| image:: https://travis-ci.org/scls19fr/pandas-buffer.svg?branch=master
   :target: https://travis-ci.org/scls19fr/pandas-buffer