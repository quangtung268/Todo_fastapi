from setuptools import setup, find_packages

def get_requirements(path: str):
    return [l.strip() for l in open(path)]

setup(
    name='Todo maker',
    version='1.0.0',
    description='Simple Todo app',
    url='',
    keywords='Todo',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    entry_points={
        'console_scripts': [
            'todo=main:main'
        ],
    },
)