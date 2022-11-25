#How to run dockerfile locally?

```
 sudo docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" rest-api-flask sh -c "flask run"
```
