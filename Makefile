CC = gcc
FLEX = flex
BISON = bison
SRC_DIR = src
BUILD_DIR = build

all: $(BUILD_DIR)/calculator

$(BUILD_DIR)/calculator: $(BUILD_DIR)/lex.yy.c $(BUILD_DIR)/calc.tab.c
	$(CC) -o $@ $^ -lm

$(BUILD_DIR)/lex.yy.c: $(SRC_DIR)/calc.l
	@mkdir -p $(BUILD_DIR)
	$(FLEX) -o $@ $<

$(BUILD_DIR)/calc.tab.c: $(SRC_DIR)/calc.y
	@mkdir -p $(BUILD_DIR)
	$(BISON) -d -o $@ $<

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all clean