import socket
import sys

def start_server(HOST, PORT):
    try:
        # create an AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print "[INFO] Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1]
        sys.exit()

    print "[INFO] Socket created"

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print "[INFO] Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1]
        sys.exit()

    print "[INFO] Socket bind complete"

    # Start listening on socket for ten clients
    s.listen(10)
    print "[INFO] Socket now listening"

    return s


# <led_esq> <led_dir>  <acel_x> <acel_y> <acel_z>  <giro_x> <giro_y> <giro_z>"
def verify_parameters (package):

    list_package = package.split()

    if len(list_package) == 8:
        led_esq = float(list_package[0])
        led_dir = float(list_package[1])

        acel_x = float(list_package[2])
        acel_y = float(list_package[3])
        acel_z = float(list_package[4])

        giro_x = float(list_package[5])
        giro_y = float(list_package[6])
        giro_z = float(list_package[7])

    else:
        sys.exit(8)

    return led_esq, led_dir,  acel_x, acel_y, acel_z,  giro_x, giro_y, giro_z


def calcule_new_action(led_esq, led_dir, acel_x, acel_y, acel_z, giro_x, giro_y, giro_z):


    return motor_esq, motor_dir



