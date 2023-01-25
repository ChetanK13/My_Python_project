# FROM python

# COPY main.py ./main.py

# WORKDIR main.py

# EXPOSE 8000:8000

# RUN pip3 install --no-cache-dir fastapi
# CMD [ "python3", "main.py" ]

FROM python:3.8

# 
WORKDIR /app

# 
COPY ./requirements.txt requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY main.py ./main.py 
COPY app

# 
CMD [ "python3", "main.py" ]
