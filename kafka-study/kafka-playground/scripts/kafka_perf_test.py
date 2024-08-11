from confluent_kafka import Producer
import time
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')

def run_performance_test(topic, num_records, record_size, throughput, bootstrap_servers):
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'python-producer-perf-test'
    }

    producer = Producer(conf)

    start_time = time.time()
    messages_sent = 0
    bytes_sent = 0

    for i in range(num_records):
        value = generate_random_string(record_size)
        producer.produce(topic, value.encode('utf-8'), callback=delivery_report)
        
        messages_sent += 1
        bytes_sent += len(value)

        if messages_sent % 1000 == 0:
            producer.flush()

        # Throttle to maintain desired throughput
        expected_time = messages_sent / throughput
        actual_time = time.time() - start_time
        if actual_time < expected_time:
            time.sleep(expected_time - actual_time)

    producer.flush()

    end_time = time.time()
    duration = end_time - start_time

    print(f'Sent {messages_sent} messages in {duration:.2f} seconds')
    print(f'Throughput: {messages_sent/duration:.2f} messages/sec')
    print(f'    {bytes_sent/duration/1024/1024:.2f} MB/sec')

if __name__ == '__main__':
    topic = 'test-topic'
    num_records = 1000000
    record_size = 1000
    throughput = 2000  # messages per second
    bootstrap_servers = 'localhost:29092,localhost:29093,localhost:29094'

    run_performance_test(topic, num_records, record_size, throughput, bootstrap_servers)