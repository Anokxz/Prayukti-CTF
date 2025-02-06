import subprocess

def divide_string(input_string):
    return [input_string[i:i+16] for i in range(0, len(input_string), 16)]
      
def send_message(ip,msg):
    print(msg)
    subprocess.run(['ping', ip, '-p', msg, '-s', str(len(msg)), '-c', '1'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

# main_msg = " flag{D4Ta_TRAv3L$_wHERE_You_L3AS7_ExPeC7}"
main_msg = "IGZsYWd7RDRUYV9UUkF2M0wkX3dIRVJFX1lvdV9MM0FTN19F  eFBlQzd9Cg=="
# IGZsYWd7RDRUYV9UUkF2M0wkX3dIRVJFX1lvdV9MM0FTN19FeFBlQzd9Cg==
# 
for msg in divide_string(main_msg):
    send_message("127.0.0.1", msg.encode('ascii').hex())    

