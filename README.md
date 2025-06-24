# Monitoring

![Alt text](image.png)

## 개요

이 프로젝트는 Docker Compose를 사용하여 모니터링 스택을 구성합니다.

## 구성 요소

- **Prometheus**: 메트릭 수집 및 저장
- **Grafana**: 시각화 및 대시보드
- **Loki**: 로그 수집 및 저장
- **Tempo**: 분산 추적 (Jaeger 호환)
- **Alertmanager**: 알림 관리
- **Pushgateway**: 배치 작업 메트릭 수집
- **Node Exporter**: 시스템 메트릭 수집
- **cAdvisor**: 컨테이너 메트릭 수집
- **Blackbox Exporter**: HTTP/HTTPS 엔드포인트 모니터링
- **Nginx**: 리버스 프록시

## 서비스 접근

모든 서비스는 Nginx를 통해 접근할 수 있습니다:

- **Grafana**: http://localhost/
- **Prometheus**: http://localhost/prometheus/
- **Loki**: http://localhost/loki/
- **Tempo**: http://localhost/tempo/
- **Alertmanager**: http://localhost/alertmanager/
- **Pushgateway**: http://localhost/pushgateway/

### Tempo 포트

Tempo는 nginx를 통해 다음 엔드포인트로 접근할 수 있습니다:

- **웹 UI**: http://localhost/tempo/
- **OTLP HTTP 수신기**: http://localhost/tempo/otlp/v1/traces
- **OTLP gRPC 수신기**: http://localhost/tempo/otlp/grpc/

모든 트레이스 전송은 nginx를 통해 안전하게 프록시됩니다.

## Tempo (분산 추적)

Tempo는 OpenTelemetry OTLP를 지원하는 분산 추적 백엔드입니다.

### 지원 프로토콜

- **OpenTelemetry OTLP** (HTTP/gRPC)

### 테스트

Tempo 테스트를 위해 다음 스크립트를 실행할 수 있습니다:

```bash
cd task
python test_tempo.py
```

### Grafana에서 확인

1. Grafana에 접속
2. Explore 메뉴로 이동
3. Tempo 데이터 소스 선택
4. 트레이스 ID로 검색 (예: `1234567890abcdef1234567890abcdef`)

## 시작하기

1. 환경 변수 설정:
```bash
export GRAFANA_ADMIN_USER=admin
export GRAFANA_ADMIN_PASSWORD=admin
export CLOUDFLARE_TUNNEL_TOKEN=your_token_here
export GRAFANA_DOMAIN=your-domain.com  # Grafana 도메인 (기본값: localhost)
```

2. 모니터링 스택 시작:
```bash
cd monitoring
docker-compose up -d
```

3. Agent 시작 (선택사항):
```bash
cd agent
docker-compose up -d
```