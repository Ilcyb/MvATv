from setuptools import setup, find_packages

required = []
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='mvatv',
    version='0.0.1',
    description='A Cli Tool that download and watch movies',
    long_description=open('README.md', encoding='utf-8').read(),
    author='ilcyb',
    author_email='hybmail1996@gmail.com',
    url='https://github.com/Ilcyb/MvATv',
    package=find_packages(),
    install_required = requirements,
    entry_points = {
        'console_scripts': [
            'mvatv = mvatv.main:main'
        ]
    },
    license='MIT',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5'
    )
)