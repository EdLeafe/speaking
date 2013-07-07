#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyrax
pyrax.keyring_auth()
#pyrax.set_credential_file("path/to/creds/file")

cs = pyrax.cloudservers


ubu1204 = "5cebb13a-f783-4f8c-8058-c4182c724ccd"
flavor512 = 2
x = locals()

def cb(obj):
    print("Callback, obj =", obj, obj.id)
    print("status =", obj.status)
    print("networks:", obj.networks)


for ii in range(3):

    import pdb
    pdb.set_trace()

    nm = "wayne%s" % ii
    server = cs.servers.create(nm, ubu1204, flavor512, metadata={"purpose": "ww test"})
    print(nm, server.adminPass)
    pyrax.utils.wait_until(server, "status", ["ERROR", "ACTIVE"], attempts=0, interval=10, callback=cb)



