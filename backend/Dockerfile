# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE generator.settings

# Set the working directory in the container to /app
WORKDIR /code

# Add the current directory . (Django project) to the container at /app
ADD . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the app to be accessible
EXPOSE 80

# Define the default command to run the Django development server
CMD ["uvicorn", "generator.asgi:application", "--host", "0.0.0.0", "--port", "80", "--workers", "3", "--log-config", "log_config.json","--timeout-keep-alive","300", "--lifespan", "off"]
