# Base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy application files into the container
COPY . .

WORKDIR /usr/src/app

# Install artiq_rs_sma100b module
RUN pip install .

ENV PYTHONUNBUFFERED=1

# Specify the default command to run the service
#CMD ["python", "artiq_rs_sma100b/aqctl_artiq_rs_sma100b.py", "--simulation"]
CMD ["pytest", "artiq_rs_sma100b/test_artiq_rs_sma100b.py"]
