from setuptools import find_packages, setup

setup(name="exception-decouple",
      version="1.0",
      description="A decorator that allows you to decouple exception handling",
      author="Aleksandr Gavrilov",
      author_email='sanya-991@mail.ru',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="MIT",
      url="http://github.com/cfytrok/exception-decouple",
      readme="README.md",
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
      )
