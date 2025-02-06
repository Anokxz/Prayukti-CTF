import pyshark
import base64

def extract_and_reassemble_data(pcap_file):
    extracted_packets = []

    capture = pyshark.FileCapture(pcap_file, display_filter="icmp")

    for packet in capture:
        try:
            if not hasattr(packet, "ICMP") or packet.ICMP.type != "8":
                continue

            if hasattr(packet.ICMP, "data"):
                hex_string = packet.ICMP.data.replace(":", "") 
                extracted_packets.append((int(packet.number), bytes.fromhex(hex_string)))

        except Exception as e:
            print(f"Error processing packet: {e}")
            continue

    capture.close()

   
    extracted_packets.sort(key=lambda x: x[0])

    try:
        message_bytes = b"".join([data for _, data in extracted_packets])
        print(message_bytes)
        decoded_message = message_bytes.decode("ascii", errors="ignore") 
        print("Extracted Hex Message:", decoded_message)

        # Decode Base64 to get the final message
        final_message = base64.b64decode(decoded_message).decode("utf-8")
        print("Final Extracted Message:", final_message)

    except Exception as e:
        print(f"Decoding Error: {e}")

# Call the function with your PCAP file
extract_and_reassemble_data("file.pcapng")
