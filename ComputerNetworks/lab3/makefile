all: server client hello_world

server: server.c file_transfer.h
	gcc -w -o server server.c

client: client.c file_transfer.h
	gcc -w -o client client.c

hello_world: hello_world.c
	gcc -w -o hello_world hello_world.c