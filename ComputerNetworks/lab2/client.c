#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define ip_addr "127.0.0.1"
#define message_len 256
#define socket_port 21566

int main(void)
{
    struct sockaddr_in server_sockaddr;
    int sock_desc;
    char *message = "hellow server";
    char buf[message_len];

    if ((sock_desc = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("Error socket()\n");
        exit(1);
    }

    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    if (connect(sock_desc, (struct sockaddr *)&server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        perror("Error connect()\n");
        exit(1);
    }

    //printf("Please, enter a message: \n");
    //fgets(buf, message_len, stdin);
    if (send(sock_desc, message, sizeof(message), 0) < 0)
    {
        perror("Error send()\n");
        exit(1);
    }

    if (recv(sock_desc, buf, sizeof(message), 0) < 0)
    {
        perror("Error recv()\n");
        exit(1);
    }

    printf("Server returned message: %s\n", buf);

    close(sock_desc);
    
    return 0;
}