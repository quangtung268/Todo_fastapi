from setuptools import setup, find_packages

setup(
    name='Todo maker',
    version='1.0.0',
    description='Simple Todo app',
    url='',
    keywords='Todo',
    python_requires='>=3.10',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=main:main'
        ],
    },
)