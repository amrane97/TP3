from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


import requests
from PyQt5.QtWidgets import QMessageBox

class Main():
    def query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


from shodan import Shodan

@app.get("/ip/{ip}")
async def get_ip(ip: str, key: Optional[str] = None):
    if key is None:
        return {"Error": "Please provide a valid API key"}
    else:
        try:
            api = Shodan(key)
            res = api.host(ip)
            return {
                "IP": res["ip_str"],
                "Organization": res["org"],
                "Country": res["country_name"],
            }
        except Exception as e:
            return {"Error": str(e)}