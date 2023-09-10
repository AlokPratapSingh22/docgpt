## Docker commands

```
docker build -t chat-gpt-app .
docker run --rm -d --env-file .env --name chat-gpt-container -p 80:80 chat-gpt-app
docker image rm -f chat-gpt-app:latest
docker container stop chat-gpt-container
docker container rm chat-gpt-container
docker exec -it chat-gpt-container /bin/bash
```