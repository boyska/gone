gone
=========

gone is `screen-message <https://darcs.nomeata.de/screen-message/>`_
plus a screen locker. The basic idea is that I wanted to
leave a message on my (locked) screen, like "be back soon".

Another "feature" of gone is its *non*-integration with PAM. ``gone`` needs a
password-hash as its first parameter, and will not check against any other
system db. This is to encourage different password for different purposes.

License
---------

GPLv3