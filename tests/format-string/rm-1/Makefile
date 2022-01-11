CHALLENGE=format
USER=maxime

CC=gcc
CFLAGS=-m32 -Wall -no-pie
LDFLAGS=

SRC=$(CHALLENGE).c
OBJ=$(SRC:.c=.o)
BIN=$(CHALLENGE)

.DEFAULT_GOAL := challenge
.PHONY : clean all

$(BIN): $(OBJ)
	@echo "Compiling..."
	$(CC) -o $@ $(SRC) $(LDFLAGS) $(CFLAGS)

challenge: $(BIN)
	@echo "Applying permissions..."
	rm -f $(OBJ)
	chown $(USER):$(USER) $(BIN) .passwd Makefile $(SRC)
	chmod 400 .passwd
	chmod 440 $(SRC) Makefile
	chmod 550 $(BIN)
	chmod u+s $(BIN)

