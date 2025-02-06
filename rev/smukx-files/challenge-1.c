// Challenge 1 [Simple Reverse Engineering]
// By @5mukx [https://x.com/5mukx]


// Remove the inline comments 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define FLAG "Here_I$_$he_F1@G"
#define FLAG_LEN strlen(FLAG)


//xor func !
void encrypt(char *str, char *key, int len) {
    for (int i = 0; i < len; i++) {
        str[i] ^= key[i % strlen(key)];
    }
}

int main() {
    int num;
    char input[100];
    char encrypted_flag[FLAG_LEN + 1];
    char key[] = "ECE_CTF_EVENT";


    strcpy(encrypted_flag, FLAG);
    encrypt(encrypted_flag, key, FLAG_LEN);

    printf("Enter a number: ");
    fflush(stdout);

    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Failed to read line\n");
        return 1;
    }

    if (sscanf(input, "%d", &num) != 1) {
        printf("Invalid input. Please enter a number.\n");
        return 1;
    }

    if (num == 696969) {
        printf("Flag Found!\n");
                
        encrypt(encrypted_flag, key, FLAG_LEN); 
        printf("Flag {%s}\n", encrypted_flag);
    } else {
        printf("Creds Mismatch. Hehe...\n");
        printf("Try again Kiddo ;)\n");
    }

    return 0;
}