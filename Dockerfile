# Inherit from the official Python 3 image.
FROM python:3

# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app

# Copy setup.py and README.md into /usr/src/app.
# Install application dependencies with pip.
# Build the farmOSaggregator package.
# We do these first to reduce image build time during development.
COPY setup.py README.md ./
RUN pip install -e .
RUN python setup.py install

# Copy the app.
COPY . .

# Run the application test.py.
CMD [ "python", "./test.py" ]
