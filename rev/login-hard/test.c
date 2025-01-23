#include <stdio.h>

int main() {
    for (int i = 32; i < 127; i++){
        printf("%i -> '%c'\n", i, i);
    }
}