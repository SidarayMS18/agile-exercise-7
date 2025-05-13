# Use an official Python runtime as a parent image
FROM python:latest

# Update the package manager and install security updates
RUN apt-get update && apt-get upgrade -y

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the app (if Flask is running on port 5000)
EXPOSE 5000

# Define the environment variable to indicate Flask is in production mode
ENV FLASK_ENV=production

# Run the application (adjust if your app entry point is different)
CMD ["python", "app.py"]
