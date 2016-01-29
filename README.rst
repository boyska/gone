gone
=========

gone is `screen-message <https://darcs.nomeata.de/screen-message/>`_
plus a screen locker. The basic idea is that I wanted to
leave a message on my (locked) screen, like "be back soon".

Another "feature" of gone is its *non*-integration with PAM. ``gone`` needs a
password-hash as its first parameter, and will not check against any other
system db. This is to encourage different password for different purposes.

Howto
--------

First of all, you should choose your password:

.. code:: bash
  
   gone password-gen 'P4ssw0rd!'

The output, will be something like ``$6$rounds=678695$6oMtfzrgJtpCCxD6$uqopLEv9pqjt7KXj4kQou3K5yO7XblAPD1q3u2EZfnfv4sdOlX414GNzB4DAv4LEshu0aMwmtxg7biyK5.adN/``

Our script locker will therefore be

.. code:: bash
  
   gone lock '$6$rounds=678695$6oMtfzrgJtpCCxD6$uqopLEv9pqjt7KXj4kQou3K5yO7XblAPD1q3u2EZfnfv4sdOlX414GNzB4DAv4LEshu0aMwmtxg7biyK5.adN/'

When you run this command, the script **WON'T** be locked until you press ``Ctrl+D``. Until that moment, you can type, or exit with ``Ctrl+Q``.

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
