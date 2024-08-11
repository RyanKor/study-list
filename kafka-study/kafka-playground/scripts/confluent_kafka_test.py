from confluent_kafka import Producer, Consumer, KafkaError

# Producer 예시
p = Producer({'bootstrap.servers': 'localhost:29092,localhost:29093,localhost:29094'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

p.produce('my-topic', key='key', value='value', callback=delivery_report)
p.flush()

# Consumer 예시
c = Consumer({
    'bootstrap.servers': 'localhost:29092,localhost:29093,localhost:29094',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my-topic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()