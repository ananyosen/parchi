FROM node:22 AS frontend_env
COPY . /src
RUN corepack enable pnpm

WORKDIR /src/frontend

RUN rm pnpm-lock.yaml && pnpm install

RUN pnpm run build

WORKDIR /src
RUN rm -rf frontend


FROM python:slim AS runtime

COPY --from=frontend_env /src /src

WORKDIR /src

RUN pip install -r requirements.txt

RUN python -m app.scripts.models

ENV ASSET_STORE_PATH=/data/assets/
ENV PERSIST_PATH=/data/persist/

CMD fastapi run app/main.py