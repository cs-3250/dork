import networkx as nx
from networkx.utils import open_file
import yaml

__all__ = ['read_yaml', 'write_yaml']

def write_yaml(G_to_be_yaml, path_for_yaml_output, **kwds):
    try:
        import maze.yaml
    except ImportError:
        raise ImportError("write_yaml() requires PyYAML: http://pyyaml.org/")

def read_yaml(path):
    try:
        import maze.yml
    except ImportError:
        raise ImportError("read_yaml() requires PyYAML: http://pyyaml.org/")

    G = yaml.load(path, Loader=yaml.FullLoader)
    return G

def setup_module(module):
    from nose import SkipTest
    try:
        import maze.yml
    except:
        raise SkipTest("PyYAML not available")

def teardown_module(module):
    import os
    os.unlink('maze.yaml')