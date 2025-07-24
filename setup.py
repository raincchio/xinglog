from setuptools import setup, find_packages

setup(
    name='log_writer_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'os',  # os is part of the Python standard library, so it's just an example
    ],
    description='A package for logging model training information',
    author='raincchio',
    author_email='raincchio@gmail.com',
    url='https://github.com/raincchio/xinglog',  # Replace with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
