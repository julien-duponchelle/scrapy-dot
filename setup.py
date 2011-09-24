from distutils.core import setup

setup(name='ScrapyDot',
      version='0.1',
      license='Apache License, Version 2.0',
      description='Export a graph of link between crawled items in dot file format.',
      author='Julien Duponchelle',
      author_email='julien@duponchelle.info',
      url='http://github.com/noplay/scrapy-dot',
      keywords="scrapy dot graphviz",
      py_modules=['scrapydot'],
      platforms = ['Any'],
      install_requires = ['scrapy'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)

