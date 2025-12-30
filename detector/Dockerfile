FROM python:3.10-slim
WORKDIR /detector
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY detector.py .
CMD ["python", "detector.py"]

