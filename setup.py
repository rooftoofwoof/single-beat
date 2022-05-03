from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='single-beat',
    version='0.5.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='ensures only one instance of your process across your servers',
    url='https://github.com/ybrs/single-beat',
    license='MIT',
    packages=['singlebeat'],
    zip_safe=True,
    install_requires=[
        'tornado >= 6.0,<7.0',
        'redis >= 2.9.1',
        'aioredis >= 1.3.1,<2.0'
        'Click>=7.0'
    ],
    test_require=[
        'psutil>=5.2.2'
    ],
    entry_points={
        'console_scripts': [
            'single-beat = singlebeat.beat:run_process',
            'single-beat-cli = singlebeat.cli:main',
        ],
    }
)
