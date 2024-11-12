FROM python:3.12.5

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update

# Copy the requirements file into the container
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire project into the container
COPY . .

# Expose the port on which your app runs (default is 8000 for Django)
EXPOSE 8000



# Default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]