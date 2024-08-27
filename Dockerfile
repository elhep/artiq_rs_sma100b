# Base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy application files into the container
COPY . .

# Install sipyco
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/m-labs/sipyco.git
WORKDIR /usr/src/app/sipyco
RUN pip install .

# Install Rohde-Schwarz VISA
RUN apt-get install -y wget
RUN wget https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1dc02___rs_v/rsvisa_5.12.9_amd64.deb -O /tmp/rsvisa_5.12.9_amd64.deb
RUN dpkg -i /tmp/rsvisa_5.12.9_amd64.deb || apt-get install -f -y
RUN rm /tmp/rsvisa_5.12.9_amd64.deb && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Install required modules
RUN pip install --no-cache-dir -r requirements.txt

# Install artiq_rs_sma100b module
RUN pip install .

ENV PYTHONUNBUFFERED=1

# Specify the default command to run the service
CMD ["python", "artiq_rs_sma100b/aqctl_artiq_rs_sma100b.py", "--simulation"]
#CMD ["pytest", "artiq_rs_sma100b/test_artiq_rs_sma100b.py"]
