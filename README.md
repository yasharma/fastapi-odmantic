# FastApi with odmantic

This service manage Todo app

## Run Steps

1. Run `docker compose up --build` to start the service using docker
2. Run `fastapi dev` to start without docker

### Databases

| Database | Version |
| -------- | ------- |
| mongo  | latest  |

### Ports

| Database | Version |
| -------- | ------- |
| Service  | 80      |

### Environment Variables

| Environment Variable | Description                          | Default Value |
| -------------------- | ------------------------------------ | ------------- |
| PORT                 | Port on which the service should run | 80            |
| DATABASE_URL            | Impala connection string            |   -   |


## Monitoring URLs

| Type        | URL            | Expected Response Code | Sample Response |
| ----------- | -------------- | ---------------------- | --------------- |
| Healthcheck | `/healthcheck` | 200                    | "success"       |

## Service Dependencies:

### Upstream

1. Client facing ..

### Downstream

1. Mongo

## Authors

| Name        | Email          |
| ----------- | -------------- |
| Yash Sharma | `yashsharma205@gmail.com` |
