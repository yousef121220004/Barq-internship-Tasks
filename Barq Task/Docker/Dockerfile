FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY subnet_analyzer.py ip_data.xlsx .
CMD ["python", "subnet_analyzer.py"]
