import os
import time
from neo4j import GraphDatabase, basic_auth
from functools import partial
import urllib.request as request
import urllib.error as req_error
import dependency_network_loader.watcher as watcher


def _create_graph(tx, data):
    print(data)
    tx.run("MERGE (caller:Function {name: $caller_name, class: $caller_class, module: $caller_module}) " +
           "MERGE (callee:Function {name: $callee_name, class: $callee_class, module: $callee_module}) " +
           "MERGE (caller)-[:CALLS]->(callee)",
           caller_name=data['caller']['name'],
           caller_class=data['caller']['class'],
           caller_module=data['caller']['module'],
           callee_name=data['callee']['name'],
           callee_class=data['callee']['class'],
           callee_module=data['callee']['module'])


def _is_neo_up(url):
    try:
        request.urlopen(url).read()
    except (req_error.HTTPError, req_error.URLError) as e:
        return False

    return True


def _gather(x, output):
    output.append(x)


def start(main):
    callstack = []
    watcher.start(main, partial(_gather, output=callstack))

    neo_url = os.getenv('NEO4J_URL')
    bolt_url = os.getenv('NEO4J_BOLT_URL')
    auth = basic_auth(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASSWORD'))

    print(callstack)
    neo_is_down = True
    while(neo_is_down):
        neo_is_down = not _is_neo_up(neo_url)
        print(neo_is_down)
        time.sleep(1)

    with GraphDatabase.driver(bolt_url, auth=auth) as driver:
        with driver.session() as session:
            for f in callstack:
                session.write_transaction(_create_graph, f)
