CC = g++
CFLAGS = -Wall
PROG = assignment

SRCS = imageloader.cpp vec3f.cpp graphics.cpp

LIBS = -lglut -lGL -lGLU

all: $(PROG)

$(PROG):	$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)

clean:
	rm -f $(PROG)
