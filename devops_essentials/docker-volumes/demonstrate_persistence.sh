#!/bin/bash

# Build the Docker image
docker build -t my-data-container .

# Create local directory if it doesn't exist
mkdir -p local_data_directory

# Run the container
docker run -d --name data-container -v $(pwd)/local_data_directory:/data my-data-container

# Write data to the volume
docker exec data-container bash -c "echo 'Hello, Docker Volumes!' > /data/hello.txt"

# Stop the container
docker stop data-container

# Restart the container
docker start data-container

# Read data from the volume
data=$(docker exec data-container cat /data/hello.txt)

# Confirm the data matches
if [ "$data" == "Hello, Docker Volumes!" ]; then
    echo "Data persistence test passed."
else
    echo "Data persistence test failed."
fi
