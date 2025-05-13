#!/bin/bash

# Customize this with your Docker Hub username and image name
DOCKER_USERNAME="sidaray17"
IMAGE_NAME="vintage-car-auction"

echo "🔐 Logging in to Docker Hub..."
docker login

echo "🐳 Building Docker image..."
docker build -t $DOCKER_USERNAME/$IMAGE_NAME:latest .

echo "📤 Pushing image to Docker Hub..."
docker push $DOCKER_USERNAME/$IMAGE_NAME:latest

echo "✅ Docker image pushed: $DOCKER_USERNAME/$IMAGE_NAME:latest"
