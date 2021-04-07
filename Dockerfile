FROM python:3.6.1
# define the present working directory
WORKDIR /cps847-a2-docker
# copy the contents into the working dir
ADD . /cps847-a2-docker
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container

EXPOSE 5000

CMD ["python","app.py"]