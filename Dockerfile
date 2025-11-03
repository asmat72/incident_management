# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
