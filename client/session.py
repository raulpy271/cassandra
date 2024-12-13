
from sys import argv


from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT

def get_nodes():
    return ['node-1', 'node-2', 'node-3']

KEYSPACE = 'store'
nodes = get_nodes()
profile = ExecutionProfile(
    consistency_level=ConsistencyLevel.ONE,
    #consistency_level=ConsistencyLevel.TWO,
    #consistency_level=ConsistencyLevel.ALL,
)
cluster = Cluster(nodes, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
_session = None

def get_session():
    global _session
    if not _session:
        _session = cluster.connect(KEYSPACE)
        print('Conectado ', nodes)
    return _session

