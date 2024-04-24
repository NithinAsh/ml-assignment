# Use the official Python image as base
FROM python:3.8.0

COPY model_nithin.pkl /app/

# Set the working directory inside the container
WORKDIR "D:\ml assignment 2\venv"

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=third.py

# Run the Flask application
CMD ["python","./third.py"] 
