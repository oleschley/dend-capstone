# Project Writeup

## Scenario
We are working for consultancy 'Westerlies' that focuses on international trade. Our consultants want to analyze the relationship between terms of trade of a country and trade flows. From our existing data lake in S3 buckets, we have decided to load the relevant sources into data warehouse using Redshift. This will allow our analysts to query the data fast and without the need of running an ETL process and focus on their analysis.

## Data Sources
We load two data sources, prepare, clean as required and upload relevant files to S3.

### UN Comtrade Data

Our first data source contains UN Comtrade data. While it is available via API directly, for the scope of this project, we have used a version available from Harvard Dataverse.

Location: `https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/H8SFD2/C1KPMP&version=3.1`

We then proceed to prepare and clean the data as required. Country and commodity code mappings are available froim UN Comtrade. Please refer to `notebooks/comtrade.ipynb` for details.

### Terms of Trade
Our second dataset contains terms of trade of countries worldwide. We used data available from the International Monetary Fund.

Location: `https://data.imf.org/?sk=388DFA60-1D26-4ADE-B505-A05A558D9A42&sId=1479329334655`

We wrangle the data to bring it into appropriate shape and map country names to ISO codes. Please refer to `notebooks/terms_of_trade.ipynb` for details.

## Data Exploration
