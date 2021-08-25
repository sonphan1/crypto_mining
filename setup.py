from setuptools import setup

setup(
    name='crypto_mining',
    version='0.0.1',
    packages=['python'],
    install_requires=[
        'comtypes',
        'pywin32',
        'pywinauto',
        'six',
        'importlib; python_version >= "3.8"'
    ],
)