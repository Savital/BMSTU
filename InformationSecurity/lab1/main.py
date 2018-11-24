
from installer import check_license

def main():
    if check_license():
        print("The license is trusted.")
    else:
        print("The license isn't trusted.")

main()