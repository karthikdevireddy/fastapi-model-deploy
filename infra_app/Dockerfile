# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]


#ENTRYPOINT ["uvicorn"]
#CMD ["app:app", "--host", "0.0.0.0"]