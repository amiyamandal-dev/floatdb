import os

from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
from dotenv import load_dotenv

load_dotenv()


class StringVec(Model):
    __table_name__ = "string_vectors"
    id = columns.Integer(primary_key=True)
    string_val = columns.Text(required=True)
    embedding = columns.List(required=True, value_type=columns.Float)
    hash_of_embedding = columns.Text(required=True)
    created_at = columns.DateTime()


class DB:
    def __init__(self):
        self.cluster = Cluster([os.getenv('CASSANDRA_CLUSTER')], port=os.getenv("CASSANDRA_PORT"))

        self.session = self.cluster.connect(f"{os.getenv('USER_SPACE')}")
        self.session.execute(f"USE {os.getenv('USER_SPACE')}")
        connection.setup([os.getenv('CASSANDRA_CLUSTER')], f"{os.getenv('USER_SPACE')}", protocol_version=3)
        sync_table(StringVec)

    def __call__(self, *args, **kwargs):
        pass
