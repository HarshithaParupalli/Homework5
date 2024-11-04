# Use a lightweight base image with Python installed
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory on the host to the container's /app directory
COPY . .

# Install the required Python package for generating QR codes
RUN pip install qrcode[pil]

# Set an environment variable for the URL (default is your GitHub profile link)
ENV QR_DATA_URL="https://github.com/HarshithaParupalli"

# Define the command that runs when the container starts
CMD ["python", "generate_qr.py"]
