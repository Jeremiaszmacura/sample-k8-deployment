FROM python:3.11

WORKDIR /sample-app

COPY sample-app/requirements.txt .
# Ignore Pega certificate problem
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "sample-app/sample-app.py", "run", "--host=0.0.0.0"]
