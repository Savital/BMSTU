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
    int sock_desc;
    struct sockaddr_in server_sockaddr;

    if ((sock_desc = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        handle_error("client error socket()");
    }

    memset((char *) &server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

    if (connect(sock_desc, (struct sockaddr*)&server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        handle_error("client error connect()");
        close(sock_desc);
    }

    close(sock_desc);
    
    return 0;
}