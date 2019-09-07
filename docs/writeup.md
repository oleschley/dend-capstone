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

### Data Model and ETL
Our source data comes to what resembles a star schema quite closely. Hence, it makes most sense to follow that approach.

We will build a fact table from our main sources UN Comtrade and IMF Terms of Trade. We can join both sources on the ISO code 3166 for country names. The mappings will be utilized as dimension tables. The implementation is fairly forward using two files:

`cluster/queries.sql`: queries for the ETL process
`cluster/etl.py`: runs the ETL process

### Next steps
While the current level of granularity of the UN Comtrade data is fine (annual, only top-level code). However, given the reduction in storage and compute cost, we will evaluate if we can get the data on a monthly basis at all product code levels. 

We intend to use Apache Airflow to query the UN Comtrade API with a monthly scheduled job. This will increase our data more than hundredfold. We will have to monitor performance but feel that this would still be okay using Redshift. Using Apache Cassandra may not be the right choice for us given the ad-hoc nature of the business. Another alternative would be to have our analysts do more of the ETL work and use S3 in combination with Apache Spark. Or move towards DynamoDB given that we are using AWS already.

