import os
import json
import time
import click
import requests
from flask import Flask, request, Response

app = Flask(__name__)
cache = {}
origin_url = "" 
CACHE_FILE = "cache.json"
ttl = 60



def load_cache():
    global cache
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)
    else:
        cache = {}

def save_cache():
    with open(CACHE_FILE,"w") as f:
        json.dump(cache, f)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--port',required=True, type=int, help='Port to run proxy on.')
@click.option('--origin', required=True, help='Origin URL to forward requests.')

def start(port, origin):
    global origin_url
    origin_url = origin
    load_cache()

    @app.route('/<path:path>',methods=['GET'])
    def proxy(path):
        full_url = f"{origin_url}/{path}"
        entry = cache.get(full_url)

        if entry:
            age = time.time() - entry["timestamp"]
            if age <= ttl:
                print(f"[CACHE HIT]{full_url}")
                content = entry["content"]
                headers = entry["headers"]
                resp = Response(content, status=200)
                for key,value in headers.items():
                    resp.headers[key] = value
                resp.headers["X-Cache"] = "HIT"
                return resp
            else:
                print(f"[CACHE EXPIRED]{full_url}")
        
        print(f"[CACHE MISS]{full_url}")
        r = requests.get(full_url)
        content = r.content
        headers = dict(r.headers)


        cache[full_url] = {
            "timestamp":time.time(),
            "content":content.decode('utf-8'),
            "headers":headers
            }
        save_cache()

        resp = Response(content, status=r.status_code)
        for key, value in headers.items():
            resp.headers[key] = value
        resp.headers["X-Cache"] = "Miss"
        return resp
    app.run(port=port)


@cli.command()
def clear_cache():
    global cache
    cache = {}
    save_cache()
    print("CACHE CLEARED")

if __name__ =="__main__":
    cli()