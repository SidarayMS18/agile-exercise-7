FROM python:3.9 
WORKDIR /app 
COPY calculator.py /app 
COPY test_calculator.py /app 
RUN pip install pylint 
CMD ["python", "-m", "unittest", "discover"] 
