# Paint By Example API

## How to

<details><summary>setup</summary>

```bash
docker build -t paint-by-example-api:lightsail . -f ./Dockerfile.aws.lightsail

cp .env.sample .env

docker container run --rm \
    -v `pwd`/app:/app \
    --env-file .env \
    -p 8080:8000 \
    paint-by-example-api:lightsail --reload
```

</details>