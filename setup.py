from distutils.core import setup

required = []

setup(
    name='mvatv',
    version='0.0.1',
    description='A Cli Tool that download and watch movies',
    long_description=open('README.md').read(),
    author='ilcyb',
    author_email='hybmail1996@gmail.com',
    url='https://github.com/Ilcyb/MvATv',
    package=[],
    install_required = required,
    license='MIT',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5'
    )
)