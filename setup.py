from setuptools import setup, find_packages

setup(
    name='offline_folium',
    version='0.1',
    url='https://github.com/debrief/offline_folium',
    author='Robin Wilson',
    author_email='robin@rtwilson.com',
    description='Allows using folium with no internet connection',
    packages=find_packages('.'),    
    install_requires=['folium'],
)