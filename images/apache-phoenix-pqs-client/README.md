Docker image for [Apache Phoenix Query Server](https://phoenix.apache.org/server.html) client application 

##### Tested versions:
 - 4.14.3RC1

##### Requires:
 - HBase >= 1.4.10
 - Phoenix PQS

##### once container is launched, open python3 CLI and enter:
```
from typing import List, Dict
import phoenixdb
import json

def get_ids() -> List[Dict]:
    database_url = 'http://localhost:8765/'
    conn = phoenixdb.connect(database_url, autocommit=True)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, firstname VARCHAR) SALT_BUCKETS=4")
    cursor.execute("UPSERT INTO USERS VALUES (?, ?)", (1, 'Artem'))
    cursor.execute("UPSERT INTO USERS VALUES (?, ?)", (2, 'Josiah'))
    cursor.execute("UPSERT INTO USERS VALUES (?, ?)", (3, 'Mac'))
    cursor.execute("UPSERT INTO USERS VALUES (?, ?)", (4, 'Ron'))
    cursor.execute('SELECT * FROM USERS')
    results = [{id: firstname} for (id, firstname) in cursor]
    cursor.close()
    conn.close()
    return results

if __name__ == '__main__':
    json.dumps({'Users:': get_ids()})
```
