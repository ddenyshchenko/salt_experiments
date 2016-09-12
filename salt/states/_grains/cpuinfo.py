#!/usr/bin/env python

import salt
import salt.log
import salt.utils
import salt.modules.cmdmod

def cpuinfo():
    f = open('/proc/cpuinfo', 'r')
    cpu = {
        'processors': 0,
        'threads_per_core': 0
    }

    cpu_id = None
    cpu_ids = { '0': None }
    for line in f.readlines():
        try:
            key, value = line.split(':', 2)
            if key.strip() == 'processor':
                proc = value.strip()
                cpu['processors'] += 1
            elif key.strip() == 'physical id':
                cpu_id = value.strip()
                cpu_ids[cpu_id] = None
            elif key.strip() == 'cpu MHz':
                cpu['speed'] = value.strip()
                cpu['speed_unit'] = 'MHz'
            elif key.strip() == 'core id':
                core_id = value.strip()
                if cpu_id == '0' and core_id == '0':
                    cpu['threads_per_core'] += 1
        except:
            pass

    f.close()

    cpu['sockets'] = len(cpu_ids)
    if cpu['threads_per_core'] > 0:
        cpu['cores_per_socket'] = cpu['processors'] / cpu['sockets'] / cpu['threads_per_core']
    else:
        cpu['threads_per_core'] = 1
        cpu['cores_per_socket'] = 1

    data = {}
    data['cpu'] = cpu
    return data

if __name__ == "__main__":
    print(cpuinfo()['cpu'])
