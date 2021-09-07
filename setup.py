from setuptools import setup, find_packages

setup(
    name='fpl-engine',
    version='0.0.1',
    description='Package to pull fantasy football data and run your account',
    url='https://github.com/HendoGit/FantasyFootyBot.git',
    author='Alex Henderson',
    license='Apache',
    packages=find_packages(),
    install_requires=['requests', 'sqlalchemy', 'psycopg2', 'pandas']
)