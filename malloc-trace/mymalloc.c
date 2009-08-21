#define _GNU_SOURCE
#include <stdio.h>
#include <stdint.h>
#include <dlfcn.h>


void* malloc(size_t size)
{
    static void* (*real_malloc)(size_t) = NULL;
    if (!real_malloc)
        real_malloc = dlsym(RTLD_NEXT, "malloc");

    void *p = real_malloc(size);
    if (p) {
      fprintf(stderr, "Allocated %d at %p\n",size,p);
    } else {
      fprintf(stderr, "Failed to allocate %d\n",size);
    }
    return p;
}

void free(void *p) 
{
  static void (*real_free)(void *) = NULL;
  if (!real_free) 
    real_free = dlsym(RTLD_NEXT,"free");
  fprintf(stderr, "Freed %p\n",p);
  real_free(p);
}  

