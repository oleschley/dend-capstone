# Project Writeup

## Scenario
We are working for consultancy 'Westerlies' that focuses on international trade. Our consultants want to analyze the relationship between terms of trade of a country and trade flows. From our existing data lake in S3 buckets, we have decided to load the relevant sources into data warehouse using Redshift. This will allow our analysts to query the data fast and without the need of running an ETL process and focus on their analysis.

## Data Sources


### UN Comtrade Data

Our first data source contains UN Comtrade data. While it is available via API directly, for the scope of this project, we have used a version available from Harvard Dataverse.

Location: `https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/H8SFD2/C1KPMP&version=3.1`

We then proceed to prepare and clean the data as required. Please refer to `notebooks/comtrade_prep.ipynb` for details.

Country and commodity code mappings are available froim UN Comtrade. Please refer to `

### Exchange Rates
Our second data source contains exchange rate information of the Euro against 32 other currencies.

Location: `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html`
Size: `1.4MB`


## Data Exploration
