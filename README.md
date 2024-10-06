### Steps

1. [Install](https://docs.docker.com/engine/install/) Docker
2. [Install](https://www.python.org/downloads/) Python and Pip. I used 3.11 for this, but it shouldn't matter too much.
3. Instantiate and activate Python virtual environment `virtualenv venv && source venv/bin/activate`
4. Install Python dependencies `pip install -r requirements.txt`
5. Download and start docker resources `docker compose up -d`
6. Run provided code
   - spark_app will connect to the remote Spark Connect server and writes simple data to Kafka
   - kafka_admin will show how to interface with the Kafka broker via Python
