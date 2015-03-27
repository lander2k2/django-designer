from setuptools import setup, find_packages

setup(name='django-designer',
      version='0.1.1',
      description='Django template renderer for designers',
      url='',
      author='Richard Lander',
      author_email='lander2k2@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['django'],
      zip_safe=False)

