#!/bin/bash

# Script to automate the setup of a Deleted File Recovery CTF Challenge

# Set variables
FLAG="CTF{recovered_flag}"
DISK_IMAGE="/challenge/disk.img"
MOUNT_DIR="/mnt/mount_dir"

# Ensure the mount directory exists
mkdir -p ${MOUNT_DIR}

# Step 1: Create a flag file
echo "${FLAG}" > flag.txt

# Step 2: Create a blank disk image
echo "[+] Creating disk image..."
dd if=/dev/zero of=${DISK_IMAGE} bs=1M count=10 > /dev/null 2>&1

# Step 3: Format the disk image with ext4 filesystem
echo "[+] Formatting disk image..."
mkfs.ext4 ${DISK_IMAGE} > /dev/null 2>&1

# Step 4: Mount the disk image
echo "[+] Mounting disk image..."
sudo mount -o loop ${DISK_IMAGE} ${MOUNT_DIR}

# Step 5: Copy the flag file to the disk image
sudo cp flag.txt ${MOUNT_DIR}/

# Step 6: Sync and delete the flag file to simulate deletion
echo "[+] Deleting flag file from disk image..."
sudo sync
sudo rm ${MOUNT_DIR}/flag.txt
sudo sync

# Step 7: Unmount the disk image
echo "[+] Unmounting disk image..."
sudo umount ${MOUNT_DIR}

# Step 8: Clean up temporary files
echo "[+] Cleaning up..."
rm -rf ${MOUNT_DIR} flag.txt

# Final message
echo "[+] Disk image created: ${DISK_IMAGE}"
echo "[+] Challenge setup complete. The disk image is ready to distribute."
