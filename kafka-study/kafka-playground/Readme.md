# Kafka Setup with Docker compose

## 1. Project Tree
```
.
├── docker-compose.yml
├── img
│   ├── broker_info.png
│   ├── broker.png
│   ├── claude_answer1.png
│   ├── docker-compose.png
│   ├── docker_stat1.png
│   ├── docker_stat2.png
│   ├── topic_create.png
│   └── topic_list.png
├── performance-test
│   ├── 2024-08-03-test.md
│   └── Readme.md
├── Readme.md
├── requirements.txt
├── scripts
│   ├── confluent_kafka_test.py
│   ├── kafka_perf_test.py
│   ├── __pycache__
│   │   └── confluent_kafka.cpython-39.pyc
│   └── py_kafka.py
```


## 2. How to Run

- Run the command below

```bash
> docker-compose up -d
```

- the result will be shown like the image below.

![docker_compse](./img/docker-compose.png)

![ui-image](./img/broker.png)

## 3. Basic Function of Kafka

- see broker info in the UI

![broker_info](./img/broker_info.png)

- topic list

![topic_list](./img/topic_list.png)

- topic create

![topic_create](./img/topic_create.png)

## 4. Kafka Performance Test

- [Performance Test Directory](./performance-test/Readme.md)
