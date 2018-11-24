from sys import platform
from subprocess import check_output
import hashlib
import os

def get_sum():
    output = check_output("dmedicode | grep -i uuid", shell=True).decode()
    #hard_uuid = output.split(":")[1][1:-1]
    #serial_num = check_output("dmidecode -s system-serial-number", shell=True).decode()
    #check_str = hard_uuid + " " + serial_num
    #return "39AB53E4-FCF1-4AD5-9BF6-E205DF017B15\n" #hashlib.sha256(check_str.encode('utf-8')).hexdigest()


def check_sum():
    real_key = get_license_key()
    #if (real_key == get_sum()):
    #    return True
    #else:
    get_sum()
    return False

def set_license_key(checksum):
    with open("license.key", "r") as license_file:
        license_file.write((checksum))

def get_license_key():
    with open("license.key", "r") as license_file:
        return license_file.readline()

def check_license():
    print(get_sum())
    print(get_license_key())
    return check_sum()
