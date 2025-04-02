# ------------------------
# 1. builder stage
# ------------------------
FROM python:3.11.9-slim-bullseye as builder

WORKDIR /app

RUN apt-get update -q && \
    apt-get -y install --no-install-recommends libopencv-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Poetry & pip upgrade
RUN pip install --upgrade pip
RUN pip install poetry --no-cache-dir

# virtualenvは無効化
RUN poetry config virtualenvs.create false

# コピーして依存関係だけインストール
COPY ./src/pyproject.toml ./src/poetry.lock ./
# install packages through poetry if there is a pyproject.toml
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# ------------------------
# 2. final stage
# ------------------------
FROM python:3.11.9-slim-bullseye as dev

ENV TZ Asia/Tokyo
RUN mkdir -p /opt/work
ENV PYTHONPATH=/opt/work/
WORKDIR /opt/work


# builderからPythonパッケージだけコピー（poetryは不要）
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# poetry や pip などの実行ファイルがインストールされる場所
# COPY --from=builder /usr/local/bin /usr/local/bin

# 任意: ユーザー作成
ARG USER_NAME=myzn
ARG GROUP_NAME=myzn
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} ${GROUP_NAME} && \
    useradd -lm -s /bin/bash -u ${UID} -g ${GID} -G sudo ${USER_NAME} && \
    echo "${USER_NAME}:password" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USER_NAME}

# # If you want to just run one command, use below
# COPY --chown=${UID}:${GID} ./infra/docker/python/docker-entrypoint.sh /docker-entrypoint.sh
# RUN chmod 755 /docker-entrypoint.sh
# ENTRYPOINT [ "/docker-entrypoint.sh" ]
