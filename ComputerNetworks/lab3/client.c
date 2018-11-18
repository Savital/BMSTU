#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#include "file_transfer.h"

void handle_error(char* error) 
{
    fprintf(stderr, "%s\n", error);
    exit(-1);
}

int main(void)
{
    int sock_desc, sending_sock;
    struct sockaddr_in server_sockaddr, client_sockaddr;

    if ((sock_desc = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
    {
        handle_error("error socket");
    }

    memset((char *) &server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(server_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

    memset((char *) &client_sockaddr, 0, sizeof(client_sockaddr));
    client_sockaddr.sin_family = AF_INET;
    client_sockaddr.sin_port = htons(client_port);
    client_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(sock_desc, (const struct sockaddr*) &client_sockaddr, sizeof(client_sockaddr)) < 0)
    {
        handle_error("error bind()");
        close(sock_desc);
    }

    if (sendto(sock_desc, client_message, strlen(client_message), 0, (const struct sockaddr*) &server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        handle_error("error sendto()");
        close(sock_desc);
    }

    close(sock_desc);
    

    return 0;
}