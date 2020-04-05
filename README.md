# Installation:

```shell script
mkvirtualenv fapi
createdb fapi
pip install -r requirements/base.txt
./manage upgrade
```

# Server start:
```shell script
./manage run
```

Url to check: http://127.0.0.1:5000/account/

The response should look like this:
```json
{"operation_time":0.0007078647613525391,"operation_id":1}
```

