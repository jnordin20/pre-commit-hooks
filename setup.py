from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks',
    description='Hooks for pre-commits',
    url='https://github.com/jnordin20/pre-commit-hooks',
    version='1.0.0',

    author='Johan Nordin',
    author_email='jnordin@fyusion.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'check_commit_msg_pattern = pre_commit_hooks.check_commit_msg_pattern:main',
        ],
    },
)
