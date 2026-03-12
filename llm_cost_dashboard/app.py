import streamlit as st
import pandas as pd
import plotly.express as px
from observability_data import get_llm_usage_summary, get_llm_usage_raw

st.set_page_config(page_title="LLM Cost Dashboard", layout="wide")

st.title("LLM Cost Analytics Dashboard")
st.caption("Monitor LLM usage, token consumption, and estimated cost across providers, models, and interaction types.")

st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2025-03-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2025-03-10"))

summary = get_llm_usage_summary(str(start_date), str(end_date))
raw_data = get_llm_usage_raw(str(start_date), str(end_date))
raw_df = pd.DataFrame(raw_data)

if not raw_df.empty:
    provider_filter = st.sidebar.multiselect(
        "Provider",
        options=raw_df["llm_provider"].unique(),
        default=list(raw_df["llm_provider"].unique())
    )

    model_filter = st.sidebar.multiselect(
        "Model",
        options=raw_df["model_name"].unique(),
        default=list(raw_df["model_name"].unique())
    )

    interaction_filter = st.sidebar.multiselect(
        "Interaction Type",
        options=raw_df["interaction_type"].unique(),
        default=list(raw_df["interaction_type"].unique())
    )

    raw_df = raw_df[
        (raw_df["llm_provider"].isin(provider_filter)) &
        (raw_df["model_name"].isin(model_filter)) &
        (raw_df["interaction_type"].isin(interaction_filter))
    ]

col1, col2, col3 = st.columns(3)
col1.metric("Total Tokens", f'{summary["total_tokens"]:,}')
col2.metric("Estimated Cost (USD)", f'${summary["estimated_cost_usd"]:.3f}')
col3.metric("Request Count", f'{summary["request_count"]:,}')

st.markdown("---")

daily_df = pd.DataFrame(summary["daily_trend"])
fig_daily = px.line(daily_df, x="date", y="cost_usd", title="Cost Over Time")
st.plotly_chart(fig_daily, use_container_width=True)

fig_tokens = px.line(daily_df, x="date", y="tokens", title="Daily Token Usage")
st.plotly_chart(fig_tokens, use_container_width=True)

model_df = pd.DataFrame(summary["by_model"])
fig_model = px.bar(model_df, x="model_name", y="cost_usd", color="provider", title="Cost by Model")
st.plotly_chart(fig_model, use_container_width=True)

interaction_df = pd.DataFrame(summary["by_interaction_type"])
fig_interaction = px.pie(interaction_df, names="interaction_type", values="cost_usd", title="Cost by Interaction Type")
st.plotly_chart(fig_interaction, use_container_width=True)

provider_df = pd.DataFrame(summary["by_provider"])
fig_provider = px.bar(provider_df, x="provider", y="cost_usd", title="Cost by Provider")
st.plotly_chart(fig_provider, use_container_width=True)

hourly_df = pd.DataFrame(summary["hourly_trend"])
fig_hourly = px.line(hourly_df, x="hour", y="cost_usd", title="Hourly Cost Trend")
st.plotly_chart(fig_hourly, use_container_width=True)

user_df = pd.DataFrame(summary["by_user"])
st.subheader("Cost by User")
st.dataframe(user_df, use_container_width=True)

st.markdown("---")
st.subheader("Raw Usage Records")
if not raw_df.empty:
    raw_df_display = raw_df.rename(columns={
        "user_id": "User ID",
        "project_id": "Project ID",
        "llm_provider": "Provider",
        "model_name": "Model",
        "interaction_type": "Interaction Type",
        "prompt_tokens": "Prompt Tokens",
        "completion_tokens": "Completion Tokens",
        "total_tokens": "Total Tokens",
        "estimated_cost_usd": "Estimated Cost (USD)",
        "request_id": "Request ID",
        "created_at": "Created At"
    })
    st.dataframe(raw_df_display, use_container_width=True)
else:
    st.info("No records found for selected dates.")