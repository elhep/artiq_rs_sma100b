Welcome to Rohde & Schwarz SMA100B NDSP 
=======================================

PRECONDITIONS
-------------

Install sipyco module and R&D VISA::

    $ apt-get update
    $ apt-get install -y wget
    $ wget https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1dc02___rs_v/rsvisa_5.12.9_amd64.deb -O /tmp/rsvisa_5.12.9_amd64.deb
    $ dpkg -i /tmp/rsvisa_5.12.9_amd64.deb || apt-get install -f -y
    $ rm /tmp/rsvisa_5.12.9_amd64.deb && apt-get clean && rm -rf /var/lib/apt/lists/*

SMA100B controller usage example
--------------------------------

First, run the SMA100B controller::

    $ aqctl_artiq_rs_sma100b -d device

.. note::
    Device is RsSmab device. More in `RsSmab docs <https://rssmab.readthedocs.io/en/latest/getting_started.html>`_


Then, send commands to it via the ``sipyco_rpctool`` utility::

    $ sipyco_rpctool 127.0.0.1 3278 call set_frequency 1e5
    $ sipyco_rpctool 127.0.0.1 3278 call set_rf_on 1
    $ sipyco_rpctool 127.0.0.1 3278 call set_power 15

API
---

.. automodule:: artiq_rs_sma100b.driver
    :members:


ARTIQ Controller
----------------

.. argparse::
   :ref: artiq_rs_sma100b.aqctl_artiq_rs_sma100b.get_argparser
   :prog: aqctl_artiq_rs_sma100b

