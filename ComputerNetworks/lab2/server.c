#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>

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

    

    close(sock_desc);

    return 0;
}