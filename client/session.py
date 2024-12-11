
from sys import argv

from cassandra.cluster import Cluster

def get_nodes():
    return ['node-1', 'node-2', 'node-3']

KEYSPACE = 'store'
nodes = get_nodes()
cluster = Cluster(nodes)
_session = None

def get_session():
    global _session
    if not _session:
        _session = cluster.connect(KEYSPACE)
        print('Conectado ', nodes)
    return _session

