#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//---[Secret Flag]---//
#define OBFUSCATED_FLAG {0x27, 0x0E, 0x17, 0x04, 0x3B, 0x18, 0x17, 0x3B, 0x11, 0x0F, 0x2F, 0x00}
#define FLAG_KEY 0x55

//---[Obfuscated Password Check Function]---//
int check_pass(char* passwd) {
    unsigned char obfuscated_pass[] = {0x24, 0x13, 0x24, 0x1F, 0x35, 0x2A, 0x3B, 0x10, 0x27, 0x3A, 0x3A, 0x00};
    for (int i = 0; i < strlen((char*)obfuscated_pass); i++) {
        obfuscated_pass[i] ^= 0x5A; // XOR with 0x5A to deobfuscate
    }
    return strcmp(passwd, (char*)obfuscated_pass) == 0;
}

void reveal_flag(char* buffer) {
    unsigned char flag[] = OBFUSCATED_FLAG;
    for (int i = 0; i < strlen((char*)flag); i++) {
        buffer[i] = flag[i] ^ FLAG_KEY; // XOR with FLAG_KEY to reveal flag
    }
    buffer[strlen((char*)flag)] = '\0'; // Null-terminate the flag string
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        exit(0);
    }

    char* username = argv[1];
    char* password = getpass("Password: ");

    if (check_pass(password)) {
        char flag[50];
        reveal_flag(flag);
        printf("Welcome %s! Here is your flag: %s\n", username, flag);
    } else {
        printf("Invalid password! Access denied.\n");
    }

    return 0;
}
