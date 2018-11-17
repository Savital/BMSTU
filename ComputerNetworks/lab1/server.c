#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define ip_addr "127.0.0.1"
#define message_len 256
#define socket_port 21567

int main(void)
{
    struct sockaddr_in server_sockaddr, client_sockaddr;
    int sock_desc;
    int cslen = sizeof(client_sockaddr);
    char buf[message_len];

    if ((sock_desc = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        perror("Error socket()\n");
        exit(1);
    }

    memset((char*)&server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY); //???
    
    if (bind(sock_desc, &server_sockaddr, sizeof(server_sockaddr)) == -1)
    {
        perror("Error bind()\n");
        exit(1);
    }

    while (1)
    {
        if (recvfrom(sock_desc, buf, message_len, 0, &client_sockaddr, &cslen) == -1)
        {
            perror("Error recvfrom()\n");
            exit(1);
        }
        printf("Received message from: %s:%d\n '%s'", inet_ntoa(client_sockaddr.sin_addr), ntohs(client_sockaddr.sin_port), buf);
    }

    close(sock_desc);

    return 0;
}