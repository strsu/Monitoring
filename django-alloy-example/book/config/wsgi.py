"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import pyroscope
from django.core.wsgi import get_wsgi_application

pyroscope.configure(
    application_name = "django-app",         # Grafana에 표시될 이름
    server_address   = "http://alloy:4318", # Alloy 컨테이너의 Pyroscope 수신 주소
    sample_rate      = 100,                  # 샘플링 속도 (기본 100Hz)
    detect_subprocesses = True,              # 하위 프로세스 감지 여부
    oncpu            = True,                 # CPU 사용량 프로파일링 활성화
    # 필요 시 추가 프로파일링 활성화
    # gil_weighted   = True,                 # GIL 대기 시간 포함 여부
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
