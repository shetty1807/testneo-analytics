# LLM Cost Analytics Dashboard

This project is a Streamlit dashboard for monitoring LLM usage, token consumption, and estimated cost.

## Features

- Cost over time
- Daily token usage
- Cost by model
- Cost by provider
- Cost by interaction type
- Hourly trend
- Raw usage table with filters
- Docker support
- GitHub Actions CI/CD

## Run Locally

pip install -r llm_cost_dashboard/requirements.txt
cd llm_cost_dashboard
streamlit run app.py

## Run with Docker

docker compose up --build

## Tech Stack

Python  
Streamlit  
Pandas  
Plotly  
Docker  
GitHub Actions  

Author: Naveen Shetty