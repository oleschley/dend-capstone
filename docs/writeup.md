# Project Writeup

## Scenario
We are working for consultancy 'Westerlies' that focuses on international trade. The company has decided to invest into their analytics structure. We have investigated both the data warehouse and data lake apporach. Our business has an ad-hoc and bespoke nature, so we require flexibility and rarely provide static reports. Most of our data sources are external and can be unstructured. We have come to the conclusion that building a data lake fits our needs quite well for most needs. However, trade data is central to most of our analysis and used in many 

## Data Sources
We have decided on two data sources that should be moved to our data lake first.


### Harvard Dataverse - Trade Data

Our first data source contains trade data. It is provided from Harvard Dataverse but based off 

Location: `https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/H8SFD2/C1KPMP&version=3.1`

Citation:

`The Growth Lab at Harvard University, 2019, "International Trade Data (SITC, Rev. 2)",`
`https://doi.org/10.7910/DVN/H8SFD2, Harvard Dataverse, V3, UNF:6:sjmdhBqTZNTp+zX8dznTpw== [fileUNF]`


Size `1.8GB`



Missing mapping for location, partner and product ID.

### Exchange Rates
Our second data source contains exchange rate information of the Euro against 32 other currencies.

Location: `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html`
Size: `1.4MB`


## Data Exploration
