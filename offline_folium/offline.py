import pkg_resources
from branca.element import Figure, Element, CssLink
from jinja2 import Template
import os
from .paths import dest_path

class Link(Element):
    """An abstract class for embedding a link in the HTML."""

    def get_code(self):
        """Opens the link and returns the response's content."""
        if self.code is None:
            with open(self.url, "r") as f:
                contents = f.read()
            self.code = contents
        return self.code

    def to_dict(self, depth=-1, **kwargs):
        """Returns a dict representation of the object."""
        out = super(Link, self).to_dict(depth=-1, **kwargs)
        out["url"] = self.url
        return out


class JavascriptLink(Link):
    """Create a JavascriptLink object based on a url.

    Parameters
    ----------
    url : str
        The url to be linked
    download : bool, default False
        Whether the target document shall be loaded right now.

    """

    _template = Template("<script>{{this.get_code()}}</script>")

    def __init__(self, url, download=False):
        super(JavascriptLink, self).__init__()
        self._name = "JavascriptLink"
        self.url = url
        self.code = None


class CssLink(Link):
    """Create a CssLink object based on a url.

    Parameters
    ----------
    url : str
        The url to be linked
    download : bool, default False
        Whether the target document shall be loaded right now.

    """

    _template = Template("<style>{{this.get_code()}}</style>")

    def __init__(self, url, download=False):
        super(CssLink, self).__init__()
        self._name = "CssLink"
        self.url = url
        self.code = None


import folium

folium.folium._default_js = [
    (name, os.path.join(dest_path, os.path.basename(url)))
    for (name, url) in folium.folium._default_js
]
folium.folium._default_css = [
    (name, os.path.join(dest_path, os.path.basename(url)))
    for (name, url) in folium.folium._default_css
]
folium.Map.default_js = folium.folium._default_js
folium.Map.default_css = folium.folium._default_css

# Use local resources for MarkerCluster
folium.plugins.marker_cluster.MarkerCluster.default_css = [
    (name, os.path.join(dest_path, os.path.basename(url)))
    for (name, url) in folium.plugins.marker_cluster.MarkerCluster.default_css
]

folium.plugins.marker_cluster.MarkerCluster.default_js = [
    (name, os.path.join(dest_path, os.path.basename(url)))
    for (name, url) in folium.plugins.marker_cluster.MarkerCluster.default_js
]

folium.elements.JavascriptLink = JavascriptLink
folium.elements.CssLink = CssLink


import folium.plugins

plugins = [folium.plugins.BeautifyIcon]

for plugin in plugins:
   plugin.default_js = [
       (name, os.path.join(dest_path, os.path.basename(url)))
       for (name, url) in plugin.default_js
   ]
   plugin.default_css = [
       (name, os.path.join(dest_path, os.path.basename(url)))
       for (name, url) in plugin.default_css
   ]
