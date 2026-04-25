# Tech Industry Financial Analysis
Interactive Financial Analytics Dashboard for Tech Firms | ACC102 Track4 Assignment
**Student Name: Xiaoxu Zhou | Student ID: 2471738**

---

## Project Introduction
This project develops an interactive financial analytics dashboard to compare core financial indicators, including Profit Margin, ROE, ROA, Revenue, and Debt-to-Asset Ratio, across major technology companies such as Apple, Microsoft, Google, Amazon, and Meta, as well as industry benchmarks. With multi-page navigation, dynamic visualizations, and flexible data filtering, this tool is built specifically for the ACC102 Track4 assignment. It further integrates real-time and historical stock price data via the `yfinance` library and adds a portfolio analysis module, connecting fundamental financial performance with market reactions to provide a complete view of corporate value.

The project aims to evaluate and compare the financial strength, profitability, and operational efficiency of selected technology firms through quantitative analysis of key financial metrics. It also establishes industry benchmarks to help contextualize and interpret company performance in a comparable framework, making complex financial data understandable and usable for students, investors, and researchers.

---

## Project Objective
The main goal of this project is to apply fundamental financial accounting and data analytics concepts learned in ACC102 to conduct a systematic, data-driven financial analysis of leading technology enterprises. The specific objectives are:
- To extract and process high-quality financial data from the WRDS Compustat database to ensure analytical reliability and validity.
- To compute and interpret key financial ratios, including profitability, leverage, and growth indicators, for Apple, Microsoft, Google, Amazon, and Meta.
- To construct industry average benchmarks over the 2015–2023 period to support meaningful cross-company comparison.
- To visualize historical trends, performance differences, and metric relationships using clear and intuitive charts for easier interpretation.
- To build an interactive Streamlit dashboard that supports customized data exploration, demonstrating practical data visualization and analytical skills.
- To integrate Yahoo Finance stock data and build a portfolio analysis module to link financial fundamentals with market performance.

---

## Project Background
This analysis is based on financial data retrieved from WRDS Compustat, a widely recognized database for institutional financial research. Covering a nine-year period from 2015 to 2023, the dataset supports observation of long-term performance trends, market volatility, post-pandemic recovery, and strategic adjustments within the technology sector.

During these years, the tech industry experienced rapid expansion, policy changes, and economic shifts. This project responds to the demand for data-supported insights into how large tech companies perform across key financial dimensions compared to their peers and the overall industry. By establishing benchmarks, the project helps identify which firms truly outperform the market and which merely follow industry trends.

---

## Data Pipeline & Methodology
1. **Data Extraction**: Fundamental financial data including revenue, net income, total assets, total liabilities, and equity are collected from WRDS Compustat using SQL queries, filtered for target firms and the 2015–2023 period.
2. **Data Cleaning**: Missing values, outliers, and inconsistent records are treated to improve data quality; invalid observations such as negative revenue are removed to maintain accounting consistency.
3. **Ratio Calculation**: Key financial ratios are computed to evaluate different dimensions of performance:
   - Profitability: Net Profit Margin, Return on Equity (ROE), Return on Assets (ROA)
   - Leverage: Debt-to-Asset Ratio
   - Scale & Growth: Total Revenue
4. **Benchmarking**: Annual industry averages are calculated to provide a reference baseline for evaluating individual company performance.
5. **Stock Data Acquisition**: Historical adjusted stock prices are retrieved via the `yfinance` library to support market performance analysis.
6. **Portfolio & Risk Analysis**: Calculate portfolio returns, volatility, and Sharpe ratio; run Monte Carlo simulations for investment risk assessment.
7. **Visualization & Analysis**: Multiple interactive charts (line, bar, scatter, box plots) are generated to illustrate trends, comparisons, and risk distributions.

---

## Key Features
- Multi-dimensional Financial Analysis: Covers profitability, operational efficiency, leverage, and scale for a holistic evaluation.
- Industry Benchmark Comparison: Enables direct comparison between companies and the tech industry average.
- Time-series Trend Analysis: Tracks changes across nine years to identify long-term patterns and fluctuations.
- Interactive Dashboard: Supports user-driven filtering by company, year range, and financial metric.
- Intuitive Visualization: Uses dynamic charts to present complex financial information in an understandable way.
- Scenario, Ranking, and Risk Analysis: Provides deeper insight into performance and stability.
- **Stock & Portfolio Analysis**: Integrates real-time stock data and investment risk tools for extended financial evaluation.

---

## Intended Use
This project serves as an academic tool for the ACC102 Track4 assignment, demonstrating the practical application of financial analysis, data processing, and visualization using Python. It helps students understand how financial ratios reflect business performance and how data tools support accounting analysis.

It can also be adapted for basic investment analysis, educational demonstrations, or preliminary industry research, providing a clear and structured way to explore financial performance without advanced technical knowledge.

---

## Technical Notes
- Data Source: WRDS Compustat + Yahoo Finance (yfinance)
- Core Tools: Python (pandas, NumPy), Plotly, Streamlit, yfinance
- Period: 2015–2023 (annual financial data + daily stock data)
- Firms: AAPL, MSFT, GOOGL, AMZN, META
- Interface: Interactive multi-page web dashboard
- **Network Configuration**: Automatic proxy switching for local and cloud environments

---

## Network & Proxy Configuration (Code Explanation)
This code segment is designed to **automatically adapt network permissions** between local runtime and Streamlit Cloud deployment, solving network access issues when fetching Yahoo Finance data:
1. It first detects whether the app is running on Streamlit Cloud using `st.config.get_option("server.headless")`.
2. **Local environment**: Enables a local proxy (http://127.0.0.1:7897) to ensure stable access to Yahoo Finance and external data APIs.
3. **Cloud environment**: Automatically removes proxy settings to avoid network conflicts and errors on Streamlit Cloud, as the cloud platform does not require or support local proxies.
4. This design ensures the app runs smoothly in both environments without manual code changes.

---

## Personal Reflection
Completing this technology financial analysis project has brought me substantial technical and analytical growth, deepening my understanding of financial analysis and the operating characteristics of the tech industry.

### Technical Learnings
- Data Management Skills: I improved my ability to extract structured financial data from professional databases using SQL and strengthened data cleaning and preprocessing. I also learned to fetch real-time stock data via `yfinance`.
- Python for Finance: I enhanced my proficiency in pandas, NumPy, and Plotly for financial calculations and visualizations, and built interactive dashboards with Streamlit.
- Debugging and Deployment: I mastered environment detection and automatic proxy configuration, ensuring stable deployment across local and cloud platforms.

### Analytical Insights
- Interpreting Financial Metrics: I learned to evaluate ratios within the unique context of the tech industry, with benchmarks showing performance is relative rather than absolute.
- Trend Over Short-term Fluctuation: Nine-year data reveals long-term trends better reflect strategic strength than single-year changes.
- Financial Strategy Trade-offs: Firms use distinct strategies—Apple’s conservative capital structure vs. Amazon’s growth-oriented model.

### Future Improvements
- Include more companies or use quarterly data for higher granularity.
- Incorporate qualitative factors such as policy changes and new product launches.
- Add automatic interpretation functions for non-technical users.
- Expand portfolio analysis and risk prediction tools.

---

## Project Summary
This project delivers a complete, interactive financial analysis system for five leading technology companies over 2015–2023, fully meeting ACC102 Track4 requirements. By processing WRDS Compustat data, calculating key financial ratios, integrating Yahoo Finance stock data, and building industry benchmarks, the project provides a clear, comparable view of corporate performance.

Visualizations highlight key differences: Apple’s stable high profit margin, Amazon’s high revenue with relatively low margin, Microsoft’s consistent ROE, and Meta’s fluctuating performance. The Streamlit dashboard supports customized exploration, while the automatic proxy configuration ensures reliable cross-environment operation.

Overall, this project integrates financial accounting, data processing, interactive visualization, and practical network configuration, bridging classroom knowledge with real-world data application to create a professional, usable analysis tool.
