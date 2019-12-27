import tango
from PyQt5 import Qt
from tango import DeviceProxy, EventType
from tango.constants import ALL_EVENTS



def initpet():
    initpet10()
    
    
    return 1

#a=initpet()
def initpet10():
    tango_pet1= tango.DeviceProxy("pet10")
    tango_pet.poll_attribute("ao00", 500)
    tango_pet.poll_attribute("ao01", 500)
    
    
    return 1


def initpet04():
    tango_pet = tango.DeviceProxy("pet04")
    tango_pet.poll_attribute("ai00", 1000)
    tango_pet.poll_attribute("ao00", 1000)
    tango_pet.poll_attribute("ao01", 1000)

    
    
    return 1

def initpet05():
    tango_pet = tango.DeviceProxy("pet05")
    tango_pet.poll_attribute("di00", 1000)
    tango_pet.poll_attribute("di01", 1000)
    tango_pet.poll_attribute("di02", 1000)
    tango_pet.poll_attribute("di03", 1000)
    tango_pet.poll_attribute("di04", 1000)
    tango_pet.poll_attribute("di05", 1000)
    tango_pet.poll_attribute("do00", 1000)
    tango_pet.poll_attribute("do01", 1000)
    tango_pet.poll_attribute("do02", 1000)
    tango_pet.poll_attribute("do03", 1000)
    tango_pet.poll_attribute("do04", 1000)
    tango_pet.poll_attribute("do05", 1000)
    
    
    return 1

def initpet06():
    tango_pet = tango.DeviceProxy("pet06")
    tango_pet.poll_attribute("di00", 1000)
    tango_pet.poll_attribute("di01", 1000)
    tango_pet.poll_attribute("di02", 1000)
    tango_pet.poll_attribute("di03", 1000)
    tango_pet.poll_attribute("di04", 1000)
    tango_pet.poll_attribute("di05", 1000)
    tango_pet.poll_attribute("do00", 1000)
    tango_pet.poll_attribute("do01", 1000)
    tango_pet.poll_attribute("do02", 1000)
    tango_pet.poll_attribute("do03", 1000)
    tango_pet.poll_attribute("do04", 1000)
    tango_pet.poll_attribute("do05", 1000)
    
    
    return 1

def initpet07():
    tango_pet = tango.DeviceProxy("pet07")
    tango_pet.poll_attribute("ai00", 200)
    tango_pet.poll_attribute("ai01", 200)
    tango_pet.poll_attribute("ai02", 200)
    tango_pet.poll_attribute("ai03", 200)
    tango_pet.poll_attribute("ai04", 200)
    tango_pet.poll_attribute("ai05", 200)
    tango_pet.poll_attribute("ao00", 1000)
    tango_pet.poll_attribute("ao01", 1000)
    
    
    return 1

def initpet08():
    tango_pet = tango.DeviceProxy("pet06")
    tango_pet.poll_attribute("di00", 1000)
    tango_pet.poll_attribute("di01", 1000)
    tango_pet.poll_attribute("di02", 1000)
    tango_pet.poll_attribute("di03", 1000)
    #tango_pet.poll_attribute("di04", 1000)
    #tango_pet.poll_attribute("di05", 1000)
    tango_pet.poll_attribute("do00", 1000)
    tango_pet.poll_attribute("do01", 1000)
    tango_pet.poll_attribute("do02", 1000)
    tango_pet.poll_attribute("do03", 1000)
    tango_pet.poll_attribute("do04", 1000)
    #tango_pet.poll_attribute("do05", 1000)
    
    
    return 1

def initpet09():
    tango_pet = tango.DeviceProxy("pet09")
    tango_pet.poll_attribute("ai00", 1000)
    tango_pet.poll_attribute("ao00", 1000)

    
    
    return 1
