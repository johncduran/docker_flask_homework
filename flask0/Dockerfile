FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

# FROM is fetching the version of python necessary to run the file
# WORKDIR used the app.py file as a working directory
# COPY copied the directory into its own virtual machine
# RUN installed all the necessary packages contained in the requirements.txt file
# Expose is telling docker what port ot run the app on 
# CMD is performing the command 'python app.py' in order to run the command and deploy it locally