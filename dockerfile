FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y libxml2-dev libxslt-dev

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your scripts
CMD [ "python", "table_finder.py", "scrape_data.py", "generate_tables.py" ]
