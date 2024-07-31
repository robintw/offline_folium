import pickle
from pathlib import Path
import folium.plugins
from .paths import dest_path

dump_plugins_path = Path(dest_path) / "plugins.download"


def handle_plugin_name(plugins_name: list[str] | None):
    if plugins_name is None:
        return []

    plugins = []
    all_valid_plugins = folium.plugins.__all__
    for name in plugins_name:
        if name not in all_valid_plugins:
            raise ValueError(f'"{name}" is not a valid folium plugin.')
        plugins.append(eval(f"folium.plugins.{name}"))
    dump_plugins_list(plugins)

    return plugins


def dump_plugins_list(plugins) -> None:
    """Serializing for storage"""
    with open(dump_plugins_path, "wb") as f:
        pickle.dump(plugins, f)
    print(f"\nDump downloaded plugins list to {dump_plugins_path}")


def get_local_plugins():
    if not dump_plugins_path.exists():
        return []

    with open(dump_plugins_path, "rb") as f:
        plugins = pickle.load(f)
    return plugins
