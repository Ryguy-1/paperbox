# Use NVIDIA CUDA as the base image
FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Install python3, pip, git, and supervisord
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    supervisor \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -sSL https://ollama.ai/install.sh | sh

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY . .

# Copy the supervisord configuration file into the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the port the app runs on
EXPOSE 5000

# Run supervisord to start the defined programs
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
