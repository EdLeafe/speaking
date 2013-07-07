#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pyrax
pyrax.keyring_auth()

svcs = {"CS": pyrax.cloudservers.servers,
        "CSK": pyrax.cloudservers.keypairs,
        "CNW": pyrax.cloud_networks,
        "CLB": pyrax.cloud_loadbalancers,
        "CDB": pyrax.cloud_databases,
        "DNS": pyrax.cloud_dns,
        }

with open("pycondemo.json") as ff:
    clean = json.load(ff)

for svc_abbr in clean:
    svc = svcs.get(svc_abbr)
    for id_ in clean[svc_abbr][::-1]:
        try:
            svc.delete(id_)
            print "Service %s has deleted ID %s" % (svc_abbr, id_)
        except Exception as e:
            print "SVC", svc_abbr, "ID", id_
            print "ERR", e
            print
        clean[svc_abbr].remove(id_)
with open("pycondemo.json", "w") as ff:
    json.dump(clean, ff)
