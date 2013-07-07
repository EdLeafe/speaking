#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012 Rackspace

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import sys

import pyrax
import login
cf = pyrax.cloudfiles

answer = input("This will create 1000 containers, each CDN-enabled with a single small file in it. It will take roughly 10 minutes to run. Do you want to proceed? [y/N]")
if not answer.lower().startswith("y"):
    sys.exit()

prefix = "thous"
start = 0
count = 1000
obj_name = "testobj"
obj_data = "x" * 222

import time
stm = time.time()

for n in range(start, count):
    if not n % 10:
        print(n)
    cont_name = '%s%s' % (prefix, n)
    cont = cf.create_container(cont_name)
    cont.make_public(ttl=86400)
    obj = cf.store_object(cont, obj_name, obj_data)

elapsed = time.time() - stm
print("It took %6.2f seconds to create %s containers" % (elapsed, count))
