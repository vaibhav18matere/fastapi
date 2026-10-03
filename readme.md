## FastAPI 

### Commands
```
python3 -m venv venv 
source venv/bin/activate
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
```

- check http://127.0.0.1:8000/docs for automatic documents generated 
- explore "try it out"

### Why we need API?

```
- Before APIs there was monolithic architecture, all frontend and backend code was in a single repo.
- Then there was a need to share a particular informtion to third party services
- For ex. Travel apps like MakeMyTrip, yatra, Ixigo, GoIbibo etc needs flights/ trains data to serve their customers but IRCTC or AirIndia cannot give access to their DB/Backend to any company. So, there should be some ways to access/share this data.
- This problems can be solved by APIs
- Decouple FE and BE and we write some publically available functions (APIs) in backend to serve the specific data to third party services/ companies.
- HTTP
- JSON
- For same application - as a company, i might need diff. applications ; FE - web app, mobile app, android, apple etc. 
- So, we will make a single BE and API that will serve different frontends (Mobile, Web etc)
```

### FastAPI

- FastAPI - Starlette + Pydantic
- Starlette : Manages how your API receives requests & sends back responses.
- Pydantic  : Used to check the data coming into your API is correct and in the right format.

### FastAPI Philosophy :
```
1. Fast to run
2. Fast to code 
```

- Earlier framewoks were slow in responses and high latency also lot of boilerplate code was required to write APIs.

- Client sends HTTP request to "Web Server".
- We will not send that HTTP request directly to API.
- Web Server sends in to "SGI - Server Gateway Interface"
- SGI Converts HTTP request in pre-defined (python understandable) format and sends it to "API Code" which is written in python.
- Python executes and gives some results and again the result is sends back to SGI where it is converted in diff format and sends back to web server and then to the client.

### SGI : 2 Types
#### 1. WSGI (Used in Flask) : 
```
- Its synchronous in nature and blocking architecture leads to slower request processing and scalability issues. 
- Flasks uses "Werkzeug" library to implement WSGI. 
- Web server used in flask is "Gunicorn".
```

#### 2. ASGI (Used in FastAPI) : 
```
- Starlette library used for ASGI
- Web server used is "uvicorn"
- Uvicorn is high performance , can handle async operations
- Supports "Async-Await" feature
```

#### Why FastAPI is fast to code?
1. Automatic Input Validations
2. Auto-Generated Interactive Documentation
3. Seamless Interaction with Modern eco-system (ML/DL libraries, Oauth, JWT, SQL Alchemy, Docker, Kubernetes etc)

```
Que : How many ways user can interact in any web application?
Ans : 4 (thus, CRUD : 4 HTTP Methods)
1. Create
2. Read
3. Update
4. Delete
```

#### Path Params
```
- To read, delete or edit particular resource
```

#### Query Params
```
- Optional key-value pairs 
- Appended at the end of URL endpoint
- Useed to pass additional data to the server in an HTTP request.
- Typically used for operations like 1. Filtering, 2. Sorting 3. Searching 4. Pagination
- Without altering the existing endpoint path.
```

#### HTTPS Status Codes

```
200 - Success (OK)
201 - Resource Created
204 - Success But no data return
301 - Permanent Redirect
302 - Remporary Redirect
304 - Not Modified (used for caching)
400 - Bad request
401 - Unauthorized
403 - Forbidden (Authenticated but no permission, Not Allowed)
404 - Not Found (Resource doesn't exists)
500 - Internal Server Error (Something broker on server)
502 - Bad Gateway (Gateway like Ngnix failed to reach backend)
503 - Service Unavailable (Server Down or Overload)
```