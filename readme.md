```
python3 -m venv venv 
source venv/bin/activate
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
```

- check http://127.0.0.1:8000/docs for automatic documents generated 
- explore "try it out"