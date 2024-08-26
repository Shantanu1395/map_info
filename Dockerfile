# Use the official Python image as a base
FROM python:3.9

# Install ca-certificates package(for making https calls)
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make the output directory if it doesn't exist
RUN mkdir -p output

# Run the main.py script
CMD ["python", "main.py"]