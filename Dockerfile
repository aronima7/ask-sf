FROM python:3.9 as dev

RUN pip install --upgrade pip
WORKDIR /app

COPY backend/setup.* /app/

RUN pip install -e .

COPY backend/asksf /app/asksf

EXPOSE 8000
CMD ["uvicorn", "asksf.server:app", "--host", "0.0.0.0"]

FROM node:18.14.2-alpine3.17 as frontend

WORKDIR /usr/src/app

# Copy / Install dependencies
COPY frontend/*.json ./

RUN npm ci

# Copy source (ts(x)/css/js(x)/html) code
ADD frontend/ /usr/src/app/

# Build
RUN npm run build

FROM dev as prod

COPY --from=frontend /usr/src/app/dist /app/asksf/ui/