from kafka.admin import KafkaAdminClient

# Configuration
bootstrap_servers = 'localhost:9092'  # Adjust if necessary

# Create Kafka Admin Client
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

print(admin_client.list_topics())

admin_client.close()