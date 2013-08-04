from setuptools import setup, find_packages

setup(
    name='python-angellist',
    version="0.1",
    license="MIT",

    install_requires = [
        "urllib","urllib2","json"
    ],

    description='Light wrapper around AngelList API',
    long_description=open('README.md').read(),

    author='Sandeep Bhaskar',
    author_email='sandeep.bhaskar19@gmail.com',

    url='https://github.com/sandeepbhaskar/python-angellist',
    download_url='https://github.com/sandeepbhaskar/python-angellist/downloads',

    include_package_data=True,

    packages=['angellist'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)