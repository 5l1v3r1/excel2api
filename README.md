# Convert your excel as data source and convert it as API

Excel2api currently only supports Google sheets and Excel via http

Documentation
-----------
Please open [https://excel2api.herokuapp.com/docs](https://excel2api.herokuapp.com/docs)

Manual Installation
------------
* Need python 3.7+
* Backed by python [fast api](https://github.com/tiangolo/fastapi)
* `pip install -r requirements.txt`
* Run with command `uvicorn app:app --reload --port 8000`

Docker Installation
------------
* Need python 3.7+
* Backed by python [fast api](https://github.com/tiangolo/fastapi)
* `docker-compose up -d --build`

Running unit test
------------
```shell script
  python -m unittest discover -v -s ./tests
```


Contribution
------------
We are always happy to have new contributions. 
We have `marked issues good for anyone looking to get started`, and welcome.