# Tech Industry Financial Analysis
Interactive Financial Analytics Dashboard for Tech Firms | ACC102 Track4 Assignment

## Project Introduction
This project develops an interactive financial analytics dashboard to compare core financial indicators, including Profit Margin, ROE, ROA, Revenue, and Debt-to-Asset Ratio, across major technology companies such as Apple, Microsoft, Google, Amazon, and Meta, as well as industry benchmarks. With multi-page navigation, dynamic visualizations, and flexible data filtering, this tool is built specifically for the ACC102 Track4 assignment.

The project aims to evaluate and compare the financial strength, profitability, and operational efficiency of selected technology firms through quantitative analysis of key financial metrics. It also establishes industry benchmarks to help contextualize and interpret company performance in a comparable framework, making complex financial data understandable and usable for students, investors, and researchers.

## Project Objective
The main goal of this project is to apply fundamental financial accounting and data analytics concepts learned in ACC102 to conduct a systematic, data-driven financial analysis of leading technology enterprises. The specific objectives are:
1. To extract and process high-quality financial data from the WRDS Compustat database to ensure analytical reliability and validity.
2. To compute and interpret key financial ratios, including profitability, leverage, and growth indicators, for Apple, Microsoft, Google, Amazon, and Meta.
3. To construct industry average benchmarks over the 2015–2023 period to support meaningful cross-company comparison.
4. To visualize historical trends, performance differences, and metric relationships using clear and intuitive charts for easier interpretation.
5. To build an interactive Streamlit dashboard that supports customized data exploration, demonstrating practical data visualization and analytical skills.

## Project Background
This analysis is based on financial data retrieved from WRDS Compustat, a widely recognized database for institutional financial research. Covering a nine-year period from 2015 to 2023, the dataset supports observation of long-term performance trends, market volatility, post-pandemic recovery, and strategic adjustments within the technology sector.

During these years, the tech industry experienced rapid expansion, policy changes, and economic shifts. This project responds to the demand for data-supported insights into how large tech companies perform across key financial dimensions compared to their peers and the overall industry. By establishing benchmarks, the project helps identify which firms truly outperform the market and which merely follow industry trends.

## Data Pipeline & Methodology
1. **Data Extraction**: Fundamental financial data including revenue, net income, total assets, total liabilities, and equity are collected from WRDS Compustat using SQL queries, filtered for target firms and the 2015–2023 period.
2. **Data Cleaning**: Missing values, outliers, and inconsistent records are treated to improve data quality; invalid observations such as negative revenue are removed to maintain accounting consistency.
3. **Ratio Calculation**: Key financial ratios are computed to evaluate different dimensions of performance:
   - Profitability: Net Profit Margin, Return on Equity (ROE), Return on Assets (ROA)
   - Leverage: Debt-to-Asset Ratio
   - Scale & Growth: Total Revenue
4. **Benchmarking**: Annual industry averages are calculated to provide a reference baseline for evaluating individual company performance.
5. **Visualization & Analysis**: Multiple interactive charts are generated, including line charts, bar charts, scatter plots, and box plots, to illustrate trends, comparisons, and risk distributions.

## Key Features
- Multi-dimensional Financial Analysis: Covers profitability, operational efficiency, leverage, and scale for a holistic evaluation.
- Industry Benchmark Comparison: Enables direct comparison between companies and the tech industry average.
- Time-series Trend Analysis: Tracks changes across nine years to identify long-term patterns and fluctuations.
- Interactive Dashboard: Supports user-driven filtering by company, year range, and financial metric.
- Intuitive Visualization: Uses dynamic charts to present complex financial information in an understandable and interpretable way.
- Scenario, Ranking, and Risk Analysis: Provides deeper insight into performance and stability.

## Intended Use
This project serves as an academic tool for the ACC102 Track4 assignment, demonstrating the practical application of financial analysis, data processing, and visualization using Python. It helps students understand how financial ratios reflect business performance and how data tools can support accounting analysis.

It can also be adapted for basic investment analysis, educational demonstrations, or preliminary industry research, providing a clear and structured way to explore financial performance without advanced technical knowledge.

## Technical Notes
- Data Source: WRDS Compustat
- Core Tools: Python (pandas, NumPy), Plotly, Streamlit
- Period: 2015–2023 (annual data)
- Firms: AAPL, MSFT, GOOGL, AMZN, META
- Interface: Interactive multi-page web dashboard

## Personal Reflection
Completing this technology financial analysis project has brought me substantial technical and analytical growth, deepening my understanding of financial analysis and the operating characteristics of the tech industry.

### Technical Learnings
1. **Data Management Skills**: I improved my ability to extract structured financial data from professional databases using SQL and strengthened my data cleaning and preprocessing skills. This experience made me realize how crucial data quality is for ensuring credible analytical results.
2. **Python for Finance**: I enhanced my proficiency in using pandas, NumPy, and Plotly to calculate financial ratios and create visualizations. I also learned to build interactive dashboards with Streamlit, transforming static data into explorable insights.
3. **Debugging and Code Structure**: Solving syntax errors, indentation issues, and logical bugs taught me to be more careful with code structure and readability. Systematic debugging greatly improved my work efficiency.

### Analytical Insights
1. **Interpreting Financial Metrics**: I learned to evaluate ratios within the unique context of the tech industry, such as high R&D input and asset-light business models. Industry benchmarks helped me understand that performance evaluation is relative rather than absolute.
2. **Trend Over Short-term Fluctuation**: Analyzing nine years of data showed that long-term trends reflect strategic strength and resilience better than single-year changes.
3. **Financial Strategy Trade-offs**: Comparing leverage and profitability across firms revealed different financial strategies—such as Apple’s conservative capital structure versus Amazon’s higher growth-oriented model.

### Future Improvements
1. Include more companies or expand to quarterly data for higher granularity.
2. Incorporate qualitative factors such as policy changes, mergers, and new product launches.
3. Add automatic interpretation functions to make the dashboard more user-friendly for non-technical audiences.
4. Include portfolio analysis and risk prediction tools.

## Project Summary
This project delivers a complete, interactive financial analysis system for five leading technology companies over 2015–2023, fully meeting the requirements of the ACC102 Track4 assignment. By processing data from WRDS Compustat, computing key financial ratios, and establishing industry benchmarks, the project provides a clear and comparable view of corporate performance.

The visualizations effectively highlight important differences: Apple’s stable high profit margin, Amazon’s high revenue with relatively low margin, Microsoft’s consistent ROE, and Meta’s fluctuating performance in recent years. The Streamlit dashboard enhances usability by supporting customized exploration by firm, year, and metric.

Overall, this project integrates financial accounting, data processing, and interactive visualization to deliver a professional, practical, and academically aligned analysis tool for technology industry evaluation. It successfully bridges knowledge learned in class with real-world data application, making it a meaningful learning artifact for the course.
