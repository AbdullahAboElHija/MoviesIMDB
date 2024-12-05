FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update

# Copy the requirements file into the container
COPY requirement.txt .

RUN apt-get update
RUN apt-get install gcc default-libmysqlclient-dev -y

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire project into the container
COPY . .

# Expose the port on which your app runs (default is 8000 for Django)
EXPOSE 8000



# Default command to run the Django server
CMD ["sh", "start_django.sh"]