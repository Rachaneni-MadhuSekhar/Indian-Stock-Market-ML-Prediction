📈 Indian Stock Market Analysis & ML Price Prediction

An end-to-end Data Analytics and Machine Learning project that analyzes Indian stock market data, predicts future stock closing prices, stores stock data in MySQL, and visualizes market insights through an interactive Power BI dashboard.

📌 Project Overview

This project integrates Python, Machine Learning, MySQL, and Power BI to build a stock market analytics solution for five selected companies.

The system analyzes historical stock prices, trains separate machine learning models for each company, generates predicted closing prices, and presents key insights through interactive dashboards.

The project demonstrates practical skills in data preprocessing, SQL database management, machine learning, DAX, and business intelligence reporting.

🎯 Project Objectives

- Analyze historical stock market price movements.
- Clean and prepare stock data for machine learning.
- Train and evaluate separate prediction models for five companies.
- Predict stock closing prices using trained models.
- Store and manage stock data and predictions in MySQL.
- Automate data processing and prediction updates using Python.
- Build interactive Power BI dashboards to monitor stock performance and model predictions.

🛠️ Technologies Used

Technology| Purpose
Python| Data processing and prediction workflows
Pandas & NumPy| Data manipulation and numerical operations
Scikit-learn| Machine learning model training and evaluation
Jupyter Notebook| Model development and experimentation
MySQL| Stock data storage and SQL operations
Power BI| Interactive dashboards and visual analytics
DAX| KPIs, price changes, growth calculations and dynamic insights

🏗️ Project Workflow

1. Data Collection: Obtain stock market data for five selected companies.
2. Data Preprocessing: Prepare the data and select relevant features for model training.
3. Model Training: Split the data into training and testing sets and train separate models for each company.
4. Price Prediction: Generate predicted closing prices using the trained models.
5. Database Integration: Store stock market records and prediction results in MySQL.
6. Automation: Execute Python scripts to update the data and prediction workflow according to the configured schedule.
7. Power BI Integration: Connect the stock data to Power BI and create interactive reports.
8. Insight Generation: Analyze historical price movements, price changes, and predicted closing prices.

🤖 Machine Learning Implementation

The machine learning component focuses on predicting stock closing prices for five selected companies.

Key implementation steps include:

- Preparing input features and the target variable.
- Performing a train/test split.
- Training separate models for each company.
- Generating predicted closing prices.
- Evaluating model performance using:
  - R² Score: Measures how well the model explains variation in the target values.
  - MAE (Mean Absolute Error): Measures the average absolute prediction error.
Actual model names and evaluation results should be documented after verifying the training code and test results.

🗄️ MySQL Database Integration

MySQL is used as the database layer for storing and retrieving stock market information.

The database workflow supports:

- Storing stock prices and company information.
- Managing date-wise stock records.
- Storing predicted closing prices.
- Retrieving data for reporting and analysis.
- Integrating database records with Python and Power BI.

📊 Power BI Dashboard

The Power BI report contains two main pages.

1. Stock Overview

Provides a high-level view of stock market performance.

Key features include:

- Stock price KPIs.
- High-price and low-price movement analysis.
- Price change and growth indicators.
- Company and date slicers.
- Interactive visualizations for exploring stock performance.

2. ML Prediction Analysis

Focuses on machine learning prediction insights.

Key features include:

- Predicted closing prices for five companies.
- Actual versus predicted price comparisons where the required data is available.
- Predicted price growth analysis.
- Company-specific insights.
- Interactive filtering and dynamic KPI calculations.

The report uses DAX measures to calculate stock metrics and respond to user selections.

📈 Key Learnings

- Data cleaning and preprocessing with Python.
- Machine learning model training and evaluation.
- SQL database integration and data retrieval.
- Python automation workflows.
- Power BI dashboard development.
- DAX measures and dynamic calculations.
- Translating data into actionable analytical insights.

🚀 How to Run the Project

1. Clone or download this repository.
2. Install the required Python libraries.
3. Configure MySQL and create the required database and tables.
4. Update database connection settings using your own local configuration.
5. Run the Jupyter Notebook to explore model training and evaluation.
6. Execute the Python automation script after configuring its dependencies and database connection.
7. Open the Power BI report in Power BI Desktop.
8. Configure the appropriate data source credentials and refresh the report.

The exact setup steps depend on the uploaded scripts, database schema, and model dependencies.

⚠️ Disclaimer

This project is developed for educational and analytical purposes. Machine learning predictions are estimates based on available data and model assumptions. They are not guaranteed to reflect actual market prices and should not be treated as financial advice.

👨‍💻 Author

Data Analyst | Python | SQL | Machine Learning | Power BI

This project demonstrates the integration of data analytics, machine learning, database management, and business intelligence in a practical stock market use case.
