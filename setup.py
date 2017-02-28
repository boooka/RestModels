try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='RestModels',
    version='1.0.0',
    author='SergeyDuka',
    author_email='sergey.duka@gmail.com',
    url='https://github.com/boooka/RestModels',
    description='Access to all django models throught tastypie api',
    download_url='https://github.com/boooka/RestModels/archive/master.zip',
    license='MIT',

    packages=['restmodels'],
    install_requires=['django', 'django-tastypie'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)