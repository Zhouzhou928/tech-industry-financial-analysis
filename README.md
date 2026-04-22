# tech-industry-financial-analysis
This project builds an interactive financial analytics tool to compare key metrics (Profit Margin, ROE, ROA, Revenue, Debt-to-Asset Ratio) across leading tech firms (AAPL, MSFT, etc.) and industry benchmarks. It features multi-page navigation, dynamic visualizations, and customizable data filtering—designed for ACC102 Track4 assignment.

The core objective is to evaluate and compare the financial health, profitability, and operational efficiency of these firms through quantitative analysis of key accounting metrics, while establishing industry benchmarks to contextualize individual company performance.

## Project Objective
The primary goal of this project is to apply foundational financial accounting and data analytics skills (learned in ACC102) to conduct a structured, data-driven analysis of major tech industry players. Specific objectives include:
1. To extract and process reliable financial data from a professional database (WRDS Compustat) to ensure analytical accuracy.
2. To calculate and interpret core financial ratios (profitability, leverage, growth) to assess the financial performance of AAPL, MSFT, GOOGL, AMZN, and META.
3. To establish industry average benchmarks for the 2015-2023 period to enable meaningful cross-company comparison.
4. To visualize financial trends and relationships through intuitive charts, making complex financial data accessible and interpretable.
5. To build an interactive Streamlit dashboard that allows for customizable exploration of the analyzed data, demonstrating practical application of data visualization skills.

## Project Background
The analysis is built on financial data extracted from the WRDS Compustat database, a trusted source for institutional financial research. The 9-year time frame (2015-2023) allows for the observation of long-term trends, including market fluctuations, post-pandemic recovery, and strategic shifts within the tech industry. This project addresses the need for data-driven insights into how major tech firms perform across critical financial dimensions relative to each other and the broader industry average.

## Data Pipeline & Methodology
1. **Data Extraction**: Raw financial data (revenue, net income, total assets, total liabilities, equity, etc.) is pulled from WRDS Compustat using SQL queries, filtered for the target firms and time period (2015-2023).
2. **Data Cleaning**: Missing values, outliers, and inconsistent data formats are addressed to ensure accuracy; invalid entries (e.g., negative revenue) are removed to maintain accounting consistency.
3. **Ratio Calculation**: Core financial ratios are computed to measure key performance areas:
   - Profitability: Net Profit Margin, Return on Equity (ROE), Return on Assets (ROA)
   - Leverage: Debt-to-Asset Ratio, Current Ratio
   - Growth: Revenue Growth Rate
4. **Benchmarking**: Industry average values for each metric are calculated annually to serve as a comparative baseline for the five target companies.
5. **Visualization & Analysis**: Intuitive charts (trend lines, bar charts, scatter plots, radar charts, correlation heatmaps) are generated to visualize trends, comparisons, and relationships between metrics.

## Key Features
- **Comprehensive Metric Coverage**: Analyzes profitability, leverage, and growth metrics to provide a holistic view of financial performance.
- **Industry Benchmarking**: Enables side-by-side comparison of individual firms against the tech industry average (2015-2023).
- **Time-Series Analysis**: Tracks metric changes over 9 years to identify long-term trends and cyclical patterns.
- **Interactive Exploration**: A Streamlit-based dashboard supports customizable filtering (by company, year range, metric type) for flexible data exploration.
- **Clear Visualization**: Visual outputs include profit margin trend lines, ROE comparison bar charts, ROE-profit margin scatter plots (sized by revenue), 2023 financial strength radar charts, and correlation heatmaps of key metrics.

## Intended Use
This project serves as an educational tool for the ACC102 Track4 assignment, demonstrating practical application of financial analysis techniques, data processing, and visualization using Python. It can also be adapted for basic investment research or academic analysis of tech industry financial performance.

## Technical Notes
- Data source: WRDS Compustat (institutional access required for full data extraction)
- Core tools: Python (pandas, NumPy for data processing; Plotly for visualization; Streamlit for interactive dashboards)
- Time scope: 2015-2023 (annual financial data)
- Target firms: AAPL, MSFT, GOOGL, AMZN, META (major tech industry leaders)

## Personal Reflection
Through completing this financial analysis project for ACC102 Track4, I have gained both technical and analytical insights that deepened my understanding of financial data analysis and tech industry dynamics:

### Technical Learnings
1. **Data Handling Proficiency**: I improved my ability to extract structured financial data from institutional databases (WRDS Compustat) using SQL, and enhanced my skills in cleaning and preprocessing raw financial data to address real-world issues like missing values and outliers. This experience highlighted the critical role of data quality in ensuring reliable analytical outcomes.
2. **Python for Financial Analysis**: I strengthened my practical skills in using Python libraries (pandas, NumPy, Plotly) for calculating accounting ratios and creating intuitive visualizations. I also learned to build interactive dashboards with Streamlit, turning static data into actionable, explorable insights.
3. **Debugging & Problem-Solving**: Resolving syntax and indentation errors in code (e.g., misplaced comments, inconsistent indentation) taught me the importance of code readability and attention to detail—small formatting issues can derail the entire analytical pipeline, and systematic debugging is key to efficient project completion.

### Analytical Insights
1. **Contextualizing Financial Metrics**: Beyond calculating ratios, I learned to interpret metrics in the context of the tech industry’s unique characteristics (e.g., high R&D investment, asset-light business models) and time-specific events (e.g., COVID-19 impacts on revenue growth). Industry benchmarking revealed that "good" financial performance is relative, not absolute.
2. **Trend vs. Static Analysis**: Analyzing 9 years of data showed that short-term metric fluctuations (e.g., a single year’s drop in ROE) are less meaningful than long-term trends, which better reflect a company’s strategic execution and resilience.
3. **Trade-offs in Financial Decisions**: Comparing leverage and profitability across firms highlighted trade-offs (e.g., higher debt-to-asset ratios for Amazon vs. Apple’s conservative leverage strategy) and how different business models drive distinct financial choices in the tech sector.

### Future Improvements
1. Expand the dataset to include more tech firms or quarterly data for granular trend analysis.
2. Integrate qualitative factors (e.g., regulatory changes, product launches) to contextualize financial metric shifts.
3.Refine the Streamlit dashboard to include automated narrative analysis of key trends, making insights more accessible to non-technical stakeholders.

## Project Summary
This project successfully delivers a complete financial analysis framework for five leading tech companies from 2015 to 2023, aligned with the requirements of the ACC102 Track4 assignment. By extracting and cleaning data from WRDS Compustat, calculating key financial ratios, and building industry benchmarks, the project provides a clear comparative view of the financial performance of AAPL, MSFT, GOOGL, AMZN, and META. 

The visualization outputs (trend charts, bar charts, scatter plots, radar charts, heatmaps) effectively highlight key differences: for example, Apple’s consistent high profit margin vs. Amazon’s lower margin but higher revenue growth, or Microsoft’s stable ROE compared to Meta’s more volatile performance post-2020. The interactive Streamlit dashboard further enhances the usability of the analysis, allowing for customized exploration of metrics by company, year, or ratio type.

Overall, the project achieves its core objectives: it applies academic financial knowledge to real-world data, builds technical proficiency in Python-based data analytics, and produces actionable insights into the financial health of the tech industry’s key players.
