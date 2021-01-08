FROM ubuntu
EXPOSE 8888

# use run comand to perform instalations on container
RUN apt-get update -y;
RUN apt-get install -y build-essential python3.9 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

# specify working directory
RUN mkdir src
WORKDIR /src

# using this command we copy on the data we have localy into the src
COPY . .
# install python libraries
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
# TODO: ADD MORE PIP INSTALL HERE

# when all are set and done move to notebooks directory
WORKDIR /src/notebooks

# This code comes from the Jupyter Docker Stacks project, 
# an open-source repository that builds ready-to-use
# data science notebooks to start development and visualization projects.
# These are great for development but loading new data into them can be a little tricky. 
# This process helps avoid crashes and should be included.

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--allow-root"]

# , "python3 /lib/mySqlManager.py"