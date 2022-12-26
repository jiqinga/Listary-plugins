FROM python:3.8-slim
LABEL maintainer="1758812645@qq.com"

EXPOSE 8000
# 建议构建 Docker 镜像时一直为 1, 防止 python 将 pyc 文件写入硬盘
ENV PYTHONDONTWRITEBYTECODE 1
# 建议构建 Docker 镜像时一直为 1, 防止 python 缓冲 (buffering) stdout 和 stderr, 以便更容易地进行容器日志记录
ENV PYTHONUNBUFFERED 1
COPY ../src /app
WORKDIR /app
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    openssl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && python -m pip install --no-cache-dir --upgrade -r requirements.txt \
    && rm -rf /root/.cache/pip
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]