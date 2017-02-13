from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='limit',
      version='0.2.2',
      description='Decorator that limits the calling rate of a function',
      long_description=long_description,
      url='http://github.com/enricobacis/limit',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['limit'],
      keywords='rate ratelimit ratelimiter limit limiting api function'
)
