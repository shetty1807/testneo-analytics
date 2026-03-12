FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r llm_cost_dashboard/requirements.txt

ENV PORT=8501

CMD streamlit run llm_cost_dashboard/app.py --server.port=$PORT --server.address=0.0.0.0