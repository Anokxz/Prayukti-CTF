#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

//---[Secret Flag]---//
#define FLAG_LENGTH 21

// Generates a runtime key for additional obfuscation
void generate_runtime_key(char *key, int len) {
    srand(time(NULL));
    for (int i = 0; i < len; i++) {
        key[i] = rand() % 256; // Random byte
    }
}

// Obfuscates or deobfuscates data using a key
void xor_data(unsigned char *data, char *key, int len) {
    for (int i = 0; i < len; i++) {
        data[i] ^= key[i];
    }
}

// Password check with additional dynamic logic
int check_pass(char *passwd) {
    unsigned char obfuscated_pass[] = {0x1F, 0x22, 0x31, 0x4A, 0x3E, 0x12, 0x2C, 0x3F, 0x29, 0x5B, 0x17, 0x00};
    char runtime_key[sizeof(obfuscated_pass)];
    generate_runtime_key(runtime_key, sizeof(obfuscated_pass));
    xor_data(obfuscated_pass, runtime_key, sizeof(obfuscated_pass) - 1);
    return strcmp(passwd, (char *)obfuscated_pass) == 0;
}

// Flag reveal with runtime protection
void reveal_flag(char *buffer) {
    unsigned char obfuscated_flag[] = {0x45, 0x2E, 0x14, 0x3C, 0x2B, 0x3A, 0x1A, 0x3F, 0x19, 0x20, 0x2E, 
                                       0x30, 0x22, 0x25, 0x3B, 0x27, 0x19, 0x3D, 0x2A, 0x5C, 0x00};
    char runtime_key[FLAG_LENGTH];
    generate_runtime_key(runtime_key, FLAG_LENGTH);
    xor_data(obfuscated_flag, runtime_key, FLAG_LENGTH);
    memcpy(buffer, obfuscated_flag, FLAG_LENGTH);
    buffer[FLAG_LENGTH] = '\0';
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        exit(0);
    }

    char *username = argv[1];
    char *password = getpass("Password: ");

    if (check_pass(password)) {
        char flag[FLAG_LENGTH + 1];
        reveal_flag(flag);
        printf("Welcome %s! Here is your flag: %s\n", username, flag);
    } else {
        printf("Invalid password! Access denied.\n");
    }

    return 0;
}
