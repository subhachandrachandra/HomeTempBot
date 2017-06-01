#! /usr/bin/env python
import nest
import clientkeys

access_token_cache_file = 'nest.json'
napi = nest.Nest(client_id=clientkeys.client_id, client_secret=clientkeys.client_secret, access_token_cache_file=access_token_cache_file)

for structure in napi.structures:
    for device in structure.thermostats:
        print "%s,%s,%s,%s,%s,%0.1f,%0.1f%%,%0.1f,%s,%s,%s,%s" % ( 
            structure.name,
            structure.country_code,
            structure.postal_code,
            device.name,
            device.where,
            device.temperature,
            device.humidity,
            device.target,
            device.mode,
            device.fan,
            device.hvac_state,
            structure.away )
