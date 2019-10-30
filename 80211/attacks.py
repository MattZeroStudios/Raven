
# This class holds the functions to carry out attacks against a particular entity within the 80211 802.11 spectrum


class AttackTarget:
    def __init__(self, target):
        self.target = target

    # this will multiplex the disrupt attack to use multiple addresses
    def disrupt(self, multibool, *interfaces):
        pass

# This is a global class for attacking anything in the local area, used for hail marry attacks and can spawn
# AttackTarget objects to attack targets while still being globally controlled as a attack.


class LocalAttack:
    def __init__(self):
        pass

