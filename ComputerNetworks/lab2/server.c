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
#define socket_port 21566

int main(void)
{
    struct sockaddr_in server_sockaddr, client_sockaddr;
    int sock_desc;
    int accept_desc;
    char buf[message_len];

    if ((sock_desc = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("Error socket()\n");
        exit(1);
    }

    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(sock_desc, (struct sockaddr*)&server_sockaddr, sizeof(server_sockaddr)) < 0)
    {
        perror("Error bind()\n");
        exit(1);
    }

    listen(sock_desc, 1);

    while (1)
    {
        socklen_t cslen = sizeof(client_sockaddr);
        if (accept_desc = accept(sock_desc, (struct sockaddr*)&client_sockaddr, &cslen) < 0)
        {
            perror("Error accept()\n");
            exit(1);
        }

        printf("Received message from: %s:%d\nMessage: %s", inet_ntoa(client_sockaddr.sin_addr), ntohs(client_sockaddr.sin_port), buf);

        while (1)
        {
            int num_bytes = recv(accept_desc, buf, message_len, 0);
            if (num_bytes <= 0)
                break;
            send(accept_desc, buf, num_bytes, 0);
        }

        close(accept_desc);
        
    }

    close(sock_desc);

    return 0;
}