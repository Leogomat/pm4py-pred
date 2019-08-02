from os.path import dirname, join

from setuptools import setup

import pm4pypred


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=pm4pypred.__name__,
    version=pm4pypred.__version__,
    description=pm4pypred.__doc__.strip(),
    long_description=read_file('README.md'),
    author=pm4pypred.__author__,
    author_email=pm4pypred.__author_email__,
    py_modules=[pm4pypred.__name__],
    include_package_data=True,
    packages=['pm4pypred', 'pm4pypred.algo', 'pm4pypred.algo.prediction', 'pm4pypred.algo.prediction.versions'],
    url='http://www.pm4py.org',
    license='GPL 3.0',
    install_requires=[
        "pm4py",
        "keras",
        "tensorflow",
        "joblib",
        "lime"
    ],
    project_urls={
        'Documentation': 'http://pm4py.pads.rwth-aachen.de/documentation/',
        'Source': 'https://github.com/pm4py/pm4py-source',
        'Tracker': 'https://github.com/pm4py/pm4py-source/issues',
    }
)
