user = [{
    "username": "John",
    "email": "john@haha.com",
    "password": "Hahaha123",
    "fullname": "John rukmana"
},
{
    "username": "jeff",
    "email": "jeff@haha.com",
    "password": "Hahaha123",
    "fullname": "John rukmana"
}]

tweet = [{
    "email": "john@haha.com",
    "tweet": "Ini ceritanya tweet Twitter yah"
},
{
    "email": "jeff@haha.com",
    "tweet": "Ini ceritanya tweet Twitter yah"
}]

POST /login --> get data user berdasarkan email dan password
```
curl --request POST \
  --url http://localhost:8000/api/v1/login \
  --header 'content-type: application/json' \
  --data '{
	"email": "john@haha.com",
	"password": "Hahaha123"
}'
```

POST /Signup --> save data user ke dict user
```
curl --request POST \
  --url http://localhost:8000/api/v1/Signup \
  --header 'content-type: application/json' \
  --data '{
	"username": "John",
	"email": "john@haha.com",
	"password": "Hahaha123",
	"fullname": "John rukmana"
}'
````

POST /Tweet -->save tweet dan email di tweet
```
curl --request POST \
  --url http://localhost:8000/api/v1/Tweet \
  --header 'content-type: application/json' \
  --data '{
	"email": "john@haha.com",
	"tweet": "Ini contoh tweet"
}'
```

DELETE /tweet -->hapus tweet berdasarkan email dan tweet
```
curl --request DELETE \
  --url http://localhost:8000/api/v1/tweet \
  --header 'content-type: application/json' \
  --data '{
	"email": "john@haha.com",
	"tweet": "Ini ceritanya tweet Twitter yah"
}'
```