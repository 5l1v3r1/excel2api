# Convert your excel as data source and convert it as API

Excel2api currently only supports Google sheets and Excel via http

How to use ?

To use the Google api sheet you must change the configuration in the `conf/env.yml` folder by adding `api_key` you have.
![alt text][/img/google-sheet.png]


You can register by entering the link [Google api console](https://console.developers.google.com/apis/credentials)
![alt text][/img/google-auth.png]


Route list:
* `/v1/api/google`
    * query params `spreadsheet_id` is which spreadsheet you want to open
    * query params `sheet_range` is range you want to get
        Example: 
        - `example!A12:B22` which mean you want to open sheet `example` with range `A12` to `B22`
        - `example!A:B` which mean you want to open sheet `example` with all range `A` to `B`

* `/v1/api/url`
    * query params `spreadsheet_url` is which spreadsheet you want to open via http
    * query params `sheet_range` is range you want to get
        Example: 
        - `Sheet1!A1:C22` which mean you want to open sheet `Sheet1` with range `A12` to `B22`
        - `Sheet1!A:B` which mean you want to open sheet `Sheet1` with all range `A` to `B`

---

### This service may not stable so contributor all welcome

## Running unit test
```shell script
  python -m unittest discover -v -s ./tests
```