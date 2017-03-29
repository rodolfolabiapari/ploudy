import socket
import sys
import function

HOST = ""  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

ROBOT_SENSORS = "M"
ROBOT_N_SENSORS = "S"


# Address Family : AF_INET (this is IP version 4 or IPv4)
# Type : SOCK_STREAM (this means connection oriented TCP protocol)

print "[INFO] Starting the Ploudy"
ploudy_server = function.start_server(HOST, PORT)

while 1:

    print "[INFO] Waiting a new client..."

    # wait to accept a connection - blocking call
    # addr0 is the IP and and addr1 is the ports
    client_connection, client_addr = ploudy_server.accept()
    print "[INFO] Connected with " + client_addr[0] + " : " + str(client_addr[1])

    robot = client_connection.recv(1024)

    if robot == ROBOT_SENSORS:

        print "[INFO] <led_esq> <led_dir>  <acel_x> <acel_y> <acel_z>  <giro_x> <giro_y> <giro_z>"

        # now keep talking with the client
        while 1:

            # now keep talking with the client
            package = client_connection.recv(1024)
            print "Received: \"", package, "\""

            # Verify the parameters
            led_esq, led_dir, acel_x, acel_y, acel_z, giro_x, giro_y, giro_z = function.verify_parameters(package)

            # Process
            motor_esq, motor_dir = function.calcule_new_action(led_esq, led_dir, acel_x, acel_y, acel_z, giro_x, giro_y, giro_z)


            # Respond
            reply = "Received: \"", package, "\""
            if "exit" in package or\
                            "finnish" in package:
                break

            client_connection.sendall(reply)

        client_connection.close()

        if "exit" in package:
            break

ploudy_server.close()