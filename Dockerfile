FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r llm_cost_dashboard/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "llm_cost_dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]