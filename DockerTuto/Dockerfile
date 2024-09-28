#Defines a base for your image.
FROM python:latest    

#Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it in the Dockerfile.
WORKDIR /app

#install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy the scripts to the folder
COPY . /app


#start the server
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]