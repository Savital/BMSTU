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
    struct sockaddr_in server_sockaddr;
    int sock_desc;
    char buf[message_len];

    if ((sock_desc = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) < 0)
    {
        perror("Error socket()\n");
        exit(1);
    }

    memset((char*)&server_sockaddr, 0, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    /*if (!inet_aton(ip_addr, &server_sockaddr.sin_addr))
    {
        printf("inet_aton() error!\n");
        exit(1);
    }*/

    printf("Please, enter a message: \n");
    fgets(buf, message_len, stdin);
    if (sendto(sock_desc, buf, message_len, 0, &server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        perror("Error sendto()\n");
        exit(1);
    }

    close(sock_desc);
    
    return 0;
}