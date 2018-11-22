#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#include "file_transfer.h"

void file_send(int sock_desc)
{
    char buff[max_file_length];
    char name[max_filename_length];
    char message[max_message_length];
    int file_desc = 0;

    memset((char*) buff, 0, max_file_length);
    memset((char*) name, 0, max_filename_length);
    memset((char*) message, 0, max_message_length);

    printf("Enter filename:\n");
    scanf("%s", name);

    file_desc = open(name, 0);
    ssize_t size = read(file_desc, buff, max_file_length);

    write(sock_desc, buff, size);
    read(sock_desc, message, sizeof(message));
    printf("Message from server: %s\n", message);
    write(sock_desc, name, sizeof(name));

    memset(buff, 0, max_file_length);

    read(sock_desc, message, sizeof(message));

    printf("Message from server: %s\n", message);

    close(file_desc);
}

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

    file_send(sock_desc);

    close(sock_desc);

    return 0;
}