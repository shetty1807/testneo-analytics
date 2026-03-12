FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r llm_cost_dashboard/requirements.txt

EXPOSE 8080

CMD ["sh", "-c", "streamlit run llm_cost_dashboard/app.py --server.port=${PORT:-8080} --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false"]