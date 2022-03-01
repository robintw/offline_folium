from setuptools import setup, find_packages

setup(
    name='offline_folium',
    version='0.1',
    url='https://github.com/mypackage.git',
    author='Robin Wilson',
    author_email='robin@rtwilson.com',
    description='Description of my package',
    packages=find_packages('src'),    
    install_requires=['folium'],
)