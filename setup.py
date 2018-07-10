from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='portinfo',
      version='0.1.0',
      description='Search standard services by its port.',
      long_description=long_description,
      url='http://github.com/nunodio/portinfo',
      author='Nuno Dionisio',
      author_email='nunodio@outlook.com',
      license='MIT',
      packages=['portinfo'],
      entry_points={
        'console_scripts': ['portinfo=portinfo.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
