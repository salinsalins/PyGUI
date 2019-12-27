import tango
from PyQt5 import Qt
from tango import DeviceProxy, EventType

import time


def initpet():
    try:
        initpet10()
    except tango.DevFailed:
        print("pet10 offline")
    
    try:
        initpet02()
    except tango.DevFailed:
        print("pet02 offline")
    
    try:
        initpet04()
    except tango.DevFailed:
        print("pet04 offline")

    try:
        initpet05()
    except tango.DevFailed:
        print("pet05 offline")

    try:
        initpet06()
    except tango.DevFailed:
        print("pet06 offline")

    try:
        initpet07()
    except tango.DevFailed:
        print("pet07 offline")

    try:
        initpet08()
    except tango.DevFailed:
        print("pet08 offline")

    try:
        initpet09()
    except tango.DevFailed:
        print("pet09 offline")


    
    
    return 1

#a=initpet()
def initpet10():
    tango_pet= tango.DeviceProxy("pet10")
    #tango_pet.command_inout("Init")
    #time.sleep(5)
    #tango_pet.command_inout("Reconnect")
    #time.sleep(5)
    tango_pet.poll_attribute("ao00", 500)
    tango_pet.poll_attribute("ao01", 500)
    
    
    return 1


def initpet02():
    tango_pet = tango.DeviceProxy("pet02")
    tango_pet.poll_attribute("ai00", 1000)
    tango_pet.poll_attribute("ai02", 1000)


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
    tango_pet.poll_attribute("ai00", 500)
    tango_pet.poll_attribute("ai01", 500)
    tango_pet.poll_attribute("ai02", 500)
    tango_pet.poll_attribute("ai03", 500)
    tango_pet.poll_attribute("ai04", 1000)
    tango_pet.poll_attribute("ai05", 1000)
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

initpet()