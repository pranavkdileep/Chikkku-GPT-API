# Use the official Python image as base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file into the container
COPY app.py .

# Expose port 7860
EXPOSE 7860

# Command to run the Flask app
CMD ["python", "app.py"]
