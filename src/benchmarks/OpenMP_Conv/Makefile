WARN= -Wall -Werror -Wall
CFLAGS=
DFLAGS=

omprelease:CFLAGS+=-fopenmp -DOMP_COMPILE
omprelease: release

ompdebug:CFLAGS+=-fopenmp -DOMP_COMPILE
ompdebug: debug

release:CFLAGS+=-O3
release: all

debug:CFLAGS+=-g -O0
debug:DFLAGS+=-DDEBUG
debug: all

all: main.o
	gcc main.o -o omp_convolve.out $(WARN) $(CFLAGS)

main.o: main.cpp net_specs.h convolve.h
	gcc -c main.cpp $(DFLAGS) $(WARN) $(CFLAGS)

clean:
	rm *.o *.out
	echo Removed all .o and .out files.
