gone
=========

gone is `screen-message <https://darcs.nomeata.de/screen-message/>`_
plus a screen locker. The basic idea is that I wanted to
leave a message on my (locked) screen, like "be back soon".

Another "feature" of gone is its *non*-integration with PAM. ``gone`` needs a
password-hash as its first parameter, and will not check against any other
system db. This is to encourage different password for different purposes.

Screenshots
------------

Here they are:

composing; the last (slightly grey) part, without the bottom bar, is the locked
screen.

.. image:: http://i.imgur.com/lQHeS0u.gif

A tipical message you could leave

.. image:: https://i.imgur.com/3LBUjmk.png

Credits
---------

This is basically a dirty mix of `screen-message
<https://darcs.nomeata.de/screen-message/>`_ and `pyxtrlock
<https://github.com/leonnnn/pyxtrlock>`_.

License
---------

GPLv3
