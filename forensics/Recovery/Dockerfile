FROM ubuntu:20.04

# Install required tools
RUN apt-get update && apt-get install -y \
    e2fsprogs \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV FLAG="CTF{recovered_flag}"
ENV DISK_IMAGE="/challenge/disk.img"
ENV MOUNT_DIR="/mnt/mount_dir"

# Create working directories
WORKDIR /challenge

# Copy setup script into the container
COPY setup_deleted_file_recovery.sh /challenge/setup_deleted_file_recovery.sh

# Make the script executable
RUN chmod +x /challenge/setup_deleted_file_recovery.sh

# Run the setup script to create the disk image
RUN /challenge/setup_deleted_file_recovery.sh

# Provide the disk image as output
# CMD ["cp", "/challenge/disk.img", "/output/disk.img"]
# CMD ["timout 15 "]
