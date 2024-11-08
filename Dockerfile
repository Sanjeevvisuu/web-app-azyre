# Step 1: Use a base image with Python preinstalled
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application code and .env file into the container
COPY app.py .
COPY .env .

# Step 6: Expose port 5000
EXPOSE 5000

# Step 7: Set the environment variable for Flask to listen on all network interfaces
ENV FLASK_APP=apply.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Step 8: Command to run the application with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
