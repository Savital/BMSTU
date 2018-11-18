#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#define addr_ip "127.0.0.1"
#define socket_port 444444
#define message_length 5000

void handle_error(char* error) 
{
    fprintf(stderr, "%s\n", error);
    exit(-1);
}

int main(void)
{
    int sock_desc;
    struct sockaddr_in server_sockaddr, client_sockaddr;
    unsigned char message[message_length];
    int cslen = sizeof(client_sockaddr);
    size_t size;

    if ((sock_desc = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
    {
        handle_error("error socket");
    }

    memset((char *) &server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(sock_desc, &server_sockaddr, sizeof(server_sockaddr)) == -1)
    {
        handle_error("error bind()");
        close(sock_desc);
    }

    
    while (1)
    {
        if ((size = recvfrom(sock_desc, message, message_length, 0, (struct sockaddr*)&client_sockaddr, (socklen_t*)&cslen)) == -1)
        {
            handle_error("error recvfrom()");
            close(sock_desc);
        }

        printf("Message: %s\n", message);

        break;
    }

    close(sock_desc);

    return 0;
}