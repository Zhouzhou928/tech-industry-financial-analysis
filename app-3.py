import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import yfinance as yf

# ======================
# Global Config
# ======================
st.set_page_config(page_title="Tech Firms Financial Analysis", layout="wide")

st.markdown("""
<style>
.stSelectbox, .stSlider {margin-bottom: 20px;}
.metric-card {background: #f0f2f6; padding: 15px; border-radius: 8px; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

# ======================
# Page Navigation
# ======================
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select Page",
    ["Financial Dashboard", "Portfolio Lab"]
)

# ======================
# PAGE 1: Financial Dashboard
# ======================
if page == "Financial Dashboard":

    # ----------------------
    # Load Data
    # ----------------------
    df = pd.read_csv("tech_finance_5firms.csv")
    df = df.round(3)

    # ----------------------
    # Sidebar Filters
    # ----------------------
    st.sidebar.header("📌 Filter Controls (Global)")

    selected_companies = st.sidebar.multiselect(
        "Select Companies",
        options=df["tic"].unique(),
        default=["AAPL", "MSFT", "INDUSTRY"]
    )

    year_range = st.sidebar.slider(
        "Select Year Range",
        int(df["year"].min()),
        int(df["year"].max()),
        (2018, 2023)
    )

    selected_metric = st.sidebar.selectbox(
        "Primary Metric",
        ["profit_margin", "roe", "roa", "revt", "debt_asset"]
    )

    filtered_df = df[
        (df["tic"].isin(selected_companies)) &
        (df["year"] >= year_range[0]) &
        (df["year"] <= year_range[1])
    ]

    # ----------------------
    # Title
    # ----------------------
    st.title("📊 Tech Firms Financial Dashboard")
    st.subheader("Financial Overview")
st.subheader("📊 Investment Insight")

if metrics_summary.empty:
    st.warning("No data available")

else:
    avg = metrics_summary["Average"].mean()

    if pd.isna(avg):
        st.warning("Invalid data")

    elif avg > 0.2:
        st.success("Strong performance")

    elif avg > 0.1:
        st.info("Moderate performance")

    else:
        st.warning("Weak performance")
    # ----------------------
    # Metrics
    # ----------------------
    metrics_summary = filtered_df.groupby("tic")[selected_metric].agg(["mean", "max", "min"]).round(3)
    metrics_summary.columns = ["Average", "Peak", "Trough"]
    st.subheader("📊 Investment Insight")

    if metrics_summary.empty:
        st.warning("No data available")

    else:
        avg = metrics_summary["Average"].mean()

        if pd.isna(avg):
            st.warning("Invalid data")

        elif avg > 0.2:
            st.success("Strong performance")

        elif avg > 0.1:
            st.info("Moderate performance")

        else:
            st.warning("Weak performance")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 📈 Top Performer")
        st.write(metrics_summary["Average"].idxmax())

        st.markdown("### 📉 Bottom Performer")
        st.write(metrics_summary["Average"].idxmin())

    with col2:
        st.dataframe(metrics_summary, use_container_width=True)

    # ----------------------
    # Charts
    # ----------------------
    col3, col4 = st.columns(2)

    with col3:
        fig = px.line(filtered_df, x="year", y=selected_metric, color="tic", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        fig2 = px.scatter(filtered_df, x=selected_metric, y="profit_margin", color="tic", size="revt")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Annual Comparison")
    fig3 = px.bar(filtered_df, x="year", y=selected_metric, color="tic")
    st.plotly_chart(fig3, use_container_width=True)
    # ======================
    # 🧠 Scenario Analysis
    # ======================
    st.markdown("## 🧠 Scenario Analysis")
    
    scenario = st.selectbox(
        "Select Scenario",
        ["Growth Focus", "Profitability Focus", "Risk Focus"]
    )
    
    if scenario == "Growth Focus":
        metric = "revt"
        st.info("Analyzing revenue growth trends")
    
    elif scenario == "Profitability Focus":
        metric = "profit_margin"
        st.info("Analyzing profitability trends")
    
    else:
        metric = "debt_asset"
        st.info("Analyzing financial risk")
    
    fig_scenario = px.line(
        filtered_df,
        x="year",
        y=metric,
        color="tic",
        markers=True,
        title=f"{metric} under {scenario}"
    )
    
    st.plotly_chart(fig_scenario, use_container_width=True)
    
    
    # ======================
    # 🏆 Ranking System
    # ======================
    st.markdown("## 🏆 Company Ranking")
    
    scores = metrics_summary["Average"].rank(ascending=False)
    
    ranking_df = pd.DataFrame({
        "Rank": scores
    }).sort_values("Rank")
    
    st.dataframe(ranking_df)
    
    top_company = ranking_df.index[0]
    st.success(f"Top Company: {top_company}")
    
    
    # ======================
    # ⚠️ Risk Analysis
    # ======================
    st.markdown("## ⚠️ Risk Analysis")
    
    risk_metric = st.selectbox(
        "Select Risk Metric",
        ["debt_asset", "roa"]
    )
    
    fig_risk = px.box(
        filtered_df,
        x="tic",
        y=risk_metric,
        title=f"{risk_metric} Risk Distribution"
    )
    
    st.plotly_chart(fig_risk, use_container_width=True)
# ======================
# PAGE 2: Portfolio Lab
# ======================
elif page == "Portfolio Lab":

    st.title("📊 Portfolio Lab")

    import yfinance as yf
    import numpy as np

    tickers = st.text_input("Enter tickers", "AAPL,MSFT,GOOGL")
    ticker_list = [t.strip() for t in tickers.split(",")]

    raw_data = yf.download(ticker_list, start="2020-01-01")

    if raw_data is None or raw_data.empty:
        st.error("No data downloaded. Please check tickers.")
        st.stop()

    try:
        if isinstance(raw_data.columns, pd.MultiIndex):
            if "Adj Close" in raw_data.columns.levels[0]:
                data = raw_data["Adj Close"]
            else:
                data = raw_data["Close"]
        else:
            if "Adj Close" in raw_data.columns:
                data = raw_data["Adj Close"].to_frame()
            else:
                data = raw_data["Close"].to_frame()
    except Exception as e:
        st.error("Data processing error")
        st.stop()

    returns = data.pct_change().dropna()

    # ======================
    # Portfolio Metrics
    # ======================
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    weights = np.array([1/len(ticker_list)] * len(ticker_list))

    portfolio_return = np.sum(mean_returns * weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    st.subheader("📈 Portfolio Metrics")
    st.write(f"Return: {portfolio_return:.2%}")
    st.write(f"Volatility: {portfolio_volatility:.2%}")
    st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")

    st.line_chart(data)

    # ======================
    # Monte Carlo
    # ======================
    st.subheader("🎲 Monte Carlo Simulation")

    simulations = 100
    days = 252

    last_price = data.iloc[-1]

    sim_data = []

    for _ in range(simulations):
        prices = [last_price.mean()]
        for _ in range(days):
            prices.append(
                prices[-1] * (1 + np.random.normal(
                    returns.mean().mean(),
                    returns.std().mean()
                ))
            )
        sim_data.append(prices)

    sim_df = pd.DataFrame(sim_data).T
    st.line_chart(sim_df)
