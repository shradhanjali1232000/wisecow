# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables
ENV SRVPORT=4499
ENV RSPFILE=response

# Install necessary packages (cowsay, fortune, netcat)
RUN apt-get update \
    && apt-get install -y cowsay fortune netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set the PATH environment variable to include directories with required commands
ENV PATH="/usr/games:${PATH}"

# Copy the wisecow.sh script to the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the wisecow.sh script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port on which the server will run
EXPOSE 4499

# Set the working directory to /usr/local/bin/
WORKDIR /usr/local/bin/

# Run the wisecow.sh script
CMD ["/usr/local/bin/wisecow.sh"]