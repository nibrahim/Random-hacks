all : mymalloc.so

mymalloc.so: mymalloc.c	Makefile
	gcc -shared -ldl -fPIC mymalloc.c -o mymalloc.so

clean: 
	rm mymalloc.so
