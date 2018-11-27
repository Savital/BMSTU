from sys import platform
from subprocess import check_output
import hashlib

def get_sum():
    if platform == "linux2":
        hard_uuid = check_output("dmidecode -s system-uuid", shell=True).decode()
        serial_num = check_output("dmidecode -s system-serial-number", shell=True).decode()
    elif platform == "win32":
        hard_uuid = check_output("wmic csproduct get UUID", shell=True).decode()
        serial_num = check_output("wmic csproduct get IdentifyingNumber", shell=True).decode()
    else:
        return ""
    check_str = hard_uuid + " " + serial_num
    return hashlib.sha256(check_str.encode('utf-8')).hexdigest()

def check_sum():
    real_key = get_license_key()
    sum = get_sum()

    if (sum == ""):
        return -1
    if (real_key == sum):
        return 1
    return 0

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
