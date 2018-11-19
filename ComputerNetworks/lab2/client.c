#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define ip_addr "127.0.0.1"
#define message_len 256
#define socket_port 333331

void handle_error(char* error) 
{
    fprintf(stderr, "%s\n", error);
    exit(-1);
}

int main(void)
{
    int sock_desc;
    struct sockaddr_in server_sockaddr;
    char message[message_len];
    char buf[message_len];

    if ((sock_desc = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
    {
        handle_error("error socket");
    }

    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    if (connect(sock_desc, (struct sockaddr *)&server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        close(sock_desc);
        handle_error("Error connect()\n");
    }

    printf("Please, enter a message: \n");
    fgets(message, message_len, stdin);

    while (1)
    {
        if (send(sock_desc, message, message_len, 0) < 0)
        {
            close(sock_desc);
            handle_error("Error send()\n");
        }

        if (recv(sock_desc, buf, message_len, 0) < 0)
        {
            close(sock_desc);
            handle_error("Error recv()\n");
        }

        if (buf[0] == '$')
            break;
    }
    

    printf("Server returned message: %s\n", buf);

    close(sock_desc);
    
    return 0;
}