#Base image
FROM python:3.10-slim

#set working directory
WORKDIR /app

#copy requirements first
COPY requirements.txt .
#RUN cat requirements.txt
#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy project code
COPY . .

#Expose FASTAPI port
EXPOSE 8000

#Run FastAPI using uvicorn
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]