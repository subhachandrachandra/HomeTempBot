#!/usr/local/bin/python3
import nest
import nest.clientkeys
import time

access_token_cache_file = '/root/nest.json'
napi = nest.Nest(client_id=nest.clientkeys.client_id, 
                 client_secret=nest.clientkeys.client_secret, 
                 access_token_cache_file=access_token_cache_file)

for structure in napi.structures:
    for device in structure.thermostats:
        print ( "%d,%s,%s,%s,%s,%s,%0.1f,%0.1f%%,%0.1f,%s,%s,%s,%s" % ( 
                int(time.time()),
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
                structure.away ) )
