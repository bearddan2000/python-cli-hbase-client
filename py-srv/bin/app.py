import happybase, logging

TABLE_NAME = 'test_table'

logging.basicConfig(level=logging.INFO)

def _get_table(connection):
    return connection.table(TABLE_NAME)

def scan(connection):
    table = _get_table(connection)
    for key, data in table.scan():
        print(f'key: {key}, value: {data}')

def get(connection, identifier):
    table = _get_table(connection)
    row = table.row(identifier)
    print(row[b'cf:col1'])

def put(connection, identifier):
    table = _get_table(connection)
    table.put(identifier, {b'cf:col1': b'value1',
                        b'cf:col2': b'value2'})

def create_table(connection):
    if TABLE_NAME not in connection.tables():
        connection.create_table(TABLE_NAME, {'cf': dict()})

def main():
    connection = happybase.Connection('hbase-docker',9090)
    create_table(connection)
    put(connection, b'row-id')
    get(connection, b'row-id')
    scan(connection)

if __name__ == "__main__":
    main()