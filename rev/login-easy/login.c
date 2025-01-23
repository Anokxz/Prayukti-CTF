#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int check_pass(char* passwd){
    unsigned char obfuscated_pass[] = {
        0x23, 0x29, 0x24, 0x22, 0x3e, 0x21, 0x74, 0x01, 0x1a, 0x1d, 
        0x0a, 0x37, 0x1a, 0x61, 0x00, 0x00, 0x08, 0x61, 0x1a, 0x03, 
        0x30, 0x2b, 0x1a, 0x31, 0x75, 0x1a, 0x1c, 0x75, 0x10, 0x38,
    };
    for (int i = 0; i < 30; i++) {
        obfuscated_pass[i] ^= 0x45; 
    }
    
    return strcmp(passwd, (char*)obfuscated_pass) == 0;
}

int verify_username(char* username){
    char secert_user[9] = "@dM1nu53R";
    secert_user[5] = '\0';

    return strcmp(secert_user, username) ? 0 : 1;
}
int main(int argc, char *argv[]) {
    //---[Checking Correct Argument Count]---//
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        exit(1);
    }

    ///---[Verify Secert user]---///
    if (!verify_username(argv[1])) {
        printf("You are not the correct user!!. Be aware I'm watching you\n");
    }
    //---[Get the Password Secertly]---//
    char* password = getpass("Is It really you ??. give me our secert pharse: ");

    if (check_pass(password)) {
        printf("Wow, It is really you.\n");
    } else {
        printf("Don't Try to Fool me by impersontating. -_-\n");
    }
    return 0;
}