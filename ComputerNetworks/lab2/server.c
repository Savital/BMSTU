#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define message_len 256
#define socket_port 333331

void handle_error(char* error) 
{
    fprintf(stderr, "%s\n", error);
    exit(-1);
}

int main() 
{    
    int sock_desc;
    int accept_desc;
    struct sockaddr_in server_sockaddr, client_sockaddr;

    char* buf = calloc(sizeof(char), message_len);
    if (buf == NULL) 
    {
        handle_error("allocate memory error");
    }

    int cslen = sizeof(client_sockaddr);
    if ((sock_desc = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1) 
    {
        handle_error("socket error!");
    }

    memset((char *) &server_sockaddr, 0, cslen);
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(socket_port);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(sock_desc, &server_sockaddr, cslen) == -1) 
    {
        close(sock_desc);
        handle_error("bind error!");
    }

    listen(sock_desc, 3);

    accept_desc = accept(sock_desc, (struct sockaddr *)&client_sockaddr, (socklen_t*)&cslen);
    if (accept_desc < 0) 
    {
        close(sock_desc);
        handle_error("accept error");
    }

    while (1) 
    {
        ssize_t size = recv(accept_desc, buf, message_len, 0);
        if (size < 0) 
        {
            close(sock_desc);
            close(accept_desc);
            handle_error("recv error");
            break;
        }
        if (size == 0)
            break;

        for (ssize_t i = size - 2; i >= 0; i--) 
        {
            buf[i + 1] = buf[i];
        }
        buf[0] = '$';

        printf("Recieved message from %s: %d\nMessage: %s\n", inet_ntoa(client_sockaddr.sin_addr), ntohs(client_sockaddr.sin_port), buf);
        send(accept_desc, buf, size, 0);

        for (ssize_t i = 0; i < size; ++i) 
        {
            buf[i] = 0;
        }
    }
    
    free(buf);
    close(accept_desc);
    close(sock_desc);

    return 0;
}