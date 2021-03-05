# Run a Local Server by Python just in 5 Minutes

## Steps
1. clone my repository
2. Run my code
    on the terminal (or command line)
    ```bash
    $ python server.py 
    ```
3. request the local server (take `Postman` as an example)
    - GET `localhost:8080`
        ![image](https://user-images.githubusercontent.com/4508256/110089265-d9762400-7dd0-11eb-896c-599d867b017f.png)
    - POST `localhost:8080/webhook`
        ![image](https://user-images.githubusercontent.com/4508256/110089350-fb6fa680-7dd0-11eb-9afc-025077ef8279.png)
    - wrong URL example: POST `localhost:8080/no`
        ![image](https://user-images.githubusercontent.com/4508256/110089425-117d6700-7dd1-11eb-9374-feb5d2077af4.png)

## Reference
1. [Python 3 Simple HTTPS server](https://stackoverflow.com/a/19706670/3755348)
2. [Simple Python HTTP(S) Server - Example](https://blog.anvileight.com/posts/simple-python-http-server/#python-3-x)
