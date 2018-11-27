
from installer import check_license

def main():
    if check_license() == 1:
        print("The license is trusted.")
    elif check_license() == 0:
        print("The license isn't trusted.")
    elif check_license() == -1:
        print("The platform isn't supported.")
    else:
        print("Error: %d\n", check_license())

main()