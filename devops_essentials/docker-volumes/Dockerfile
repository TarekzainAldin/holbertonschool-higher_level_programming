# Use the base image (update this line if you have a specific base image)
FROM ubuntu:latest

# Add any additional setup instructions here
# For example, install any required packages
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Specify a volume at /data
VOLUME /data

# Set the default command for the container
CMD ["bash"]
