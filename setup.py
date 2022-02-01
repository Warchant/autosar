from setuptools import setup
import os

thispath = os.path.dirname(__file__)


def readme():
    with open(os.path.join(thispath, 'README.rst')) as f:
        return f.read()


setup(
    name='autosar',
    version='0.4.0',
    description='autosar python module',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Markup :: XML',
    ],
    url='http://github.com/warchant/autosar',
    author='Conny Gustafsson',
    author_email='congus8@gmail.com',
    license='MIT',
    install_requires=[],
    packages=[
        'autosar',
        'autosar.parser',
        'autosar.writer',
        'autosar.util'
    ],
    zip_safe=False,
    test_suite='tests.my_test_suite',
    python_requires='>=3.7',
)
