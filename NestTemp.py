#! /usr/bin/env python
import nest
import clientkeys

access_token_cache_file = 'nest.json'
napi = nest.Nest(client_id=clientkeys.client_id, client_secret=clientkeys.client_secret, access_token_cache_file=access_token_cache_file)

for structure in napi.structures:
    print ('Structure %s' % structure.name)
    print ('    Away                           : %s' % structure.away)
    print ('    Postal Code                    : %s' % structure.postal_code)
    print ('    Country                        : %s' % structure.country_code)
    print ('    num_thermostats                : %s' % structure.num_thermostats)
    print ('    Devices:')

    for device in structure.thermostats:
        print ('        Device: %s' % device.name)
        print ('        Where : %s' % device.where)
        print ('            Temp       : %0.1f' % device.temperature)
        print ('            Mode       : %s' % device.mode)
        print ('            Fan        : %s' % device.fan)
        print ('            Humidity   : %0.1f%%' % device.humidity)
        print ('            Target     : %0.1fC' % device.target)
        print ('            HVAC_STATE : %s' % device.hvac_state )
        print ('            Mode       : %s' % device.mode )

