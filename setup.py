from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='offline_folium',
    version='0.1',
    url='https://github.com/debrief/offline_folium',
    author='Robin Wilson',
    author_email='robin@rtwilson.com',
    description='Allows using folium with no internet connection',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('.'),
    include_package_data=True,
    package_data={
        'offline_folium': ['local/*'],
    },
    install_requires=[
        'folium',
        'requests',
    ],
)