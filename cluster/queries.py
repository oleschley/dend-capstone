import configparser


# Read config
config = configparser.ConfigParser()
config.read('dwh.conf')

# Drop existing
drop_staging_comtrade = "DROP TABLE IF EXISTS staging_comtrade;"
drop_staging_terms = "DROP TABLE IF EXISTS staging_terms;"
drop_trade = "DROP TABLE IF EXISTS trade;"
drop_countries = "DROP TABLE IF EXISTS countries;"
drop_reporters = "DROP TABLE IF EXISTS reporters;"
drop_partners = "DROP TABLE IF EXISTS partners;"
drop_commodities = "DROP TABLE IF EXISTS commodities;"

# Create new
create_comtrade = (
    """CREATE TABLE IF NOT EXISTS staging_comtrade (
        location_id BIGINT,
        partner_id BIGINT,
        product_id BIGINT,
        year BIGINT,
        export_value BIGINT,
        import_value BIGINT,
        location_code TEXT,
        partner_code TEXT,
        sitc_product_code BIGINT,
        index BIGINT);""")

create_terms = (
    """CREATE TABLE IF NOT EXISTS staging_terms (
        code TEXT,
        country_name TEXT,
        indicator_name TEXT,
        indicator_code TEXT,
        type_name TEXT,
        type_code TEXT,
        year BIGINT,
        value FLOAT,
        index BIGINT);""")

create_trade = (
    """CREATE TABLE IF NOT EXISTS trade (
        location_code TEXT,
        partner_code TEXT,
        product_id BIGINT,
        sitc_product_code BIGINT,
        year BIGINT,
        export_value BIGINT,
        import_value BIGINT,
        indicator_code TEXT,
        type_code TEXT,
        terms_of_trade FLOAT);""")

create_countries = (
    """CREATE TABLE IF NOT EXISTS countries (
        code TEXT,
        country_name TEXT);""")

create_reporters = (
    """CREATE TABLE IF NOT EXISTS reporters (
        id INT,
        country_name TEXT);"""
)

create_partners = (
    """CREATE TABLE IF NOT EXISTS partners (
        id INT,
        country_name TEXT);""")

create_commodities = (
    """CREATE TABLE IF NOT EXISTS commodities (
        id TEXT,
        class VARCHAR(512),
        parent VARCHAR);""")

# Insert data
insert_comtrade = (
    f"COPY staging_comtrade FROM {config.get('S3', 'TRADE_DATA')}"
    f"IAM_ROLE '{config.get('IAM_ROLE', 'ARN')}'"
    f"FORMAT AS PARQUET;"
)

insert_terms = (
    f"COPY staging_terms FROM {config.get('S3', 'TERMS_OF_TRADE')}"
    f"IAM_ROLE '{config.get('IAM_ROLE', 'ARN')}'"
    f"FORMAT AS PARQUET;"
)

insert_fact = (
    """INSERT INTO trade (
        location_code, partner_code, product_id, sitc_product_code, year, export_value, 
        import_value, indicator_code, type_code, terms_of_trade)
    SELECT
        c.location_code,
        c.partner_code,
        c.product_id,
        c.sitc_product_code,
        c.year,
        c.export_value,
        c.import_value,
        t.indicator_code,
        t.type_code,
        t.value
    FROM staging_comtrade AS c
    JOIN staging_terms AS t ON (c.location_code = t.code) AND (c.year = t.year);""")

insert_countries= (
    f"COPY countries FROM {config.get('S3', 'COUNTRIES')}"
    f"CREDENTIALS 'aws_iam_role={config.get('IAM_ROLE', 'ARN')}'"
    f"DELIMITER '\t'"
    f"IGNOREHEADER 1"
    f"REGION 'us-west-2';"
)

insert_reporters = (
    f"COPY reporters FROM {config.get('S3', 'REPORTERS')}"
    f"CREDENTIALS 'aws_iam_role={config.get('IAM_ROLE', 'ARN')}'"
    f"DELIMITER '\t'"
    f"IGNOREHEADER 1"
    f"REGION 'us-west-2';"
)

insert_partners = (
    f"COPY partners FROM {config.get('S3', 'PARTNERS')}"
    f"CREDENTIALS 'aws_iam_role={config.get('IAM_ROLE', 'ARN')}'"
    f"DELIMITER '\t'"
    f"IGNOREHEADER 1"
    f"REGION 'us-west-2';"
)

insert_commodities = (
    f"COPY commodities FROM {config.get('S3', 'COMMODITIES')}"
    f"CREDENTIALS 'aws_iam_role={config.get('IAM_ROLE', 'ARN')}'"
    f"DELIMITER '\t'"
    f"IGNOREHEADER 1"
    f"REGION 'us-west-2';"
)

drop = [drop_staging_comtrade, drop_staging_terms, drop_trade, drop_countries, drop_reporters, drop_partners, drop_commodities]
create = [create_comtrade, create_terms, create_trade, create_countries, create_reporters, create_partners, create_commodities]
insert = [insert_commodities, insert_terms, insert_fact, insert_countries, insert_reporters, insert_partners, insert_commodities]