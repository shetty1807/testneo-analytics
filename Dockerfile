FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r llm_cost_dashboard/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "llm_cost_dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]