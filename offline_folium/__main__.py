from urllib.request import urlopen
import os
import sys

import folium
import folium.plugins
from .paths import dest_path
from .plugin import handle_plugin_name

def download_all_files(plugins_name=None):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for _, js_url in folium.folium._default_js:
        download_url(js_url)
    for _, js_url in folium.folium._default_css:
        download_url(js_url)
    for plugin in handle_plugin_name(plugins_name):
        for _, js_url in plugin.default_css:
            download_url(js_url)
        for _, js_url in plugin.default_js:
            download_url(js_url)


def download_url(url):
    output_path = os.path.join(dest_path, os.path.basename(url))
    print(f"Downloading {output_path}")
    contents = urlopen(url).read().decode("utf8")
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(contents)

if __name__ == "__main__":
    print(f"Downloading files to {dest_path}")
    if len(sys.argv) > 1:
        download_all_files(sys.argv[1:])
    else:
        download_all_files()
