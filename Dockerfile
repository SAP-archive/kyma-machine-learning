# STEP 1: Install Python base image
FROM python:3.8-slim-buster

# Step 2: Add requirements.txt file 
COPY requirements.txt /requirements.txt

# Step 3:  Install required pyhton dependencies from requirements file
RUN pip install -r requirements.txt

# Step 3: Copy source code in the current directory to the container
ADD . /app

# Step 4: Set working directory to previously added app directory
WORKDIR /app

# Step 5: Expose the port Flask is running on
EXPOSE 8001

# Step 6: Run the application
CMD [ "python3", "./app.py"]


