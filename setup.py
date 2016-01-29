from distutils.core import setup


authors = (
    'boyska <piuttosto@logorroici.org>, '
)

desc = (
    'screen-message + X screen locker'
)


classifiers = [
    'Environment :: X11 Applications',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: '
    'GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2',
    'Topic :: Desktop Environment :: Screen Savers'
]

setup(name='gone',
      version='0.1',
      author=authors,
      author_email='piuttosto@logorroici.org',
      requires=['pygtk', 'pyxdg'],
      packages=['pyxtrlock'],
      py_modules=['xlock'],
      scripts=['gone'],
      license='GPLv3+',
      description=desc,
      long_description=open('README.rst').read(),
      classifiers=classifiers
      )
