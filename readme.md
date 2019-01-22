# 分析预测

```
docker build -t rightcloud/analyze:v1.0 .

docker run -d --name analyze -p 5025:5025 --link mongo:mongo  -e MONGO_HOST=mongo \
    -e MONGO_PORT=27017 -e MONGO_DATABASE=rightcloud -e MONGO_USER=rightcloud \
    -e MONGO_PWD=H89lBgAg -e DEBUG=false rightcloud/analyze:v1.0
```