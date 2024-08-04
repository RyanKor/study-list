# Kafka 초기 성능 테스트 측정 방법

## 1. kafka Built-in Test 툴 사용
- 해당 퍼포먼스 측정 툴의 옵션 (Throughput, record-size, partition 갯수 등...)을 바꿔가면서 테스트 가능
- 하지만, 카프카 자체 설정에서 메모리 관련 설정을 바꿔주지 않으면 CPU 부하가 무척 큼.
```bash
kafka-producer-perf-test
kafka-consumer-perf-test
```

## 2. On-Premise vs Cloud Environment
- 인프라가 갖춰진 장소에 따라 퍼포먼스 성능 측정을 해보는 것도 좋은 선택지임.
- 하지만, 많은 회사들이 클라우드 상에 인프라를 구축하는 최근 추세로 보건데, On-premise 성능 측정이 의미를 갖는 것은 무척 한정적이고, 베어본 장비 성능에 따라 영향도가 천차만별임

## 3. 데이터 타입
- 카프카로 처리하고자하는 데이터 타입에 따라 성능에 영향을 줄 수 있음.
- avro, parque, json 등 데이터 포맷이 있고, UDP / TCP 데이터 타입이냐에 따라 성능이 영향받을 수 있음.

## 4. 장애 상황에 대한 복구?
- 장애 상황에 대한 복구 정책도 회사마다 천차 만별이라, 다양한 시나리오에 따른 정책 상황을 감안해주면 좋을 것 같다.
