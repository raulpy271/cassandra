
from cassandra.cluster import Cluster

cluster = Cluster(['node-1', 'node-2', 'node-3'])
session = cluster.connect()

print(session.execute("SELECT release_version FROM system.local").one())
