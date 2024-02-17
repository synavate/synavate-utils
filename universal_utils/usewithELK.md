from ecs_logging import StdlibFormatter

def connect_to_es():
    # Create the client instance
    client = Elasticsearch(
        cloud_id=CLOUD_ID,
        basic_auth=("elastic", ELASTIC_PASSWORD)
    )

    # Successful response!
    return client

def index_doc(docSchema)
doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print(resp['result'])