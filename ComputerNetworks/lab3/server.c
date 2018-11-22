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
    int sock_desc, accept_desc;
    struct sockaddr_in server_sockaddr, client_sockaddr;
    int cslen = sizeof(client_sockaddr);
    //size_t size;

    if ((sock_desc = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        handle_error("server error socket");
    }

    memset((char *) &server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(sock_desc, &server_sockaddr, sizeof(server_sockaddr)) == -1)
    {
        handle_error("server error bind()");
        close(sock_desc);
    }

    printf("server binded()\n");

    if (listen(sock_desc, 13) != 0)
    {
        handle_error("server error listen()");
        close(sock_desc);
    }

    printf("server listen()\n");

    cslen = sizeof(client_sockaddr);
    if ((accept_desc = accept(sock_desc, (struct sockaddr*)&client_sockaddr, (socklen_t*)&cslen)) < 0)
    {
        handle_error("server error accept()");
        close(sock_desc);
    }

    printf("server accept()\n");
    

    close(sock_desc);
    close(accept_desc);

    return 0;
}