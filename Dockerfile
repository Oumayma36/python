# Base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables if needed
# ENV VARIABLE_NAME=value

# Start the application
CMD ["python", "app.py"]