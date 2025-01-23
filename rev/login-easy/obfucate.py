#FLAG = "flag{d1D_XOr_$EEM$_Fun_t0_Y0U}"
#FlAG
KEY = 69
print(f'{FLAG}, key = {KEY}')

obfuscated_flag = []
for letter in FLAG:
    obfuscated_flag.append(ord(letter) ^ KEY)

hex_obfuscated_flag = [hex(byte) for byte in obfuscated_flag]

print("obfuscated_flag = {")
for i in hex_obfuscated_flag:
    print(f"{i}", end="")
    if (hex_obfuscated_flag[-1] != i):
        print(", ", end="")

print('}')

original_flag = ''.join(chr(byte ^ KEY) for byte in obfuscated_flag)
print("Recovered FLAG:", original_flag)