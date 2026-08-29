import pandas as pd
def load_data():
    source_df = pd.read_csv('week8_day5_section4_source.csv')
    target_df = pd.read_csv('week8_day5_section4_target.csv')

    return source_df, target_df
def validate_date(source_df):
    total_records_cnt = len(source_df)
    valid_records_df = source_df[source_df['Customer_Name'].notna()]
    valid_records_df = valid_records_df.drop_duplicates(subset=['Customer_ID'])
    valid_records_cnt = len(valid_records_df)
    rejected_records_cnt = total_records_cnt - valid_records_cnt

    return total_records_cnt, valid_records_df, valid_records_cnt, rejected_records_cnt
def cleanse_data(valid_records_df):
    cols_to_clean = ['Customer_Name', 'Region']
    valid_records_df[cols_to_clean] = valid_records_df[cols_to_clean].apply(lambda x: x.str.strip().str.upper())
    cleanse_records_df = valid_records_df

    return cleanse_records_df
def transform_data(cleanse_records_df):
    cleanse_records_df['Tax'] = cleanse_records_df['Amount']*.10
    transformed_records_df = cleanse_records_df

    return transformed_records_df
def reconcile_data(transformed_records_df,target_df):
    comparison = pd.merge(
    transformed_records_df,
    target_df,
    on="Customer_ID",
    how="outer",
    suffixes=("_source", "_target"),
    indicator=True)

    comparison["Status"] = comparison["_merge"].map({
    "both": "Matching",
    "left_only": "Missing",
    "right_only": "Extra"
    })
    reconciled_date_df = comparison[["Customer_ID", "Status"]]

    return reconciled_date_df
def generate_summary(total_records_cnt,valid_records_cnt,rejected_records_cnt,reconciled_date_df):
    print('Total Source Records ' + str(total_records_cnt))
    print('Valid Records ' + str(valid_records_cnt))
    print('Rejected Records ' + str(rejected_records_cnt))

    Stats_df = reconciled_date_df.groupby('Status')['Status'].count()
    print(Stats_df.to_string())

    if  rejected_records_cnt == 0:
        print('Overall Result '+'Pass')
    else:
        print('Overall Result '+'Fail')

source_df, target_df = load_data()

total_records_cnt, valid_records_df, valid_records_cnt, rejected_records_cnt = validate_date(source_df)

cleanse_records_df = cleanse_data(valid_records_df)

transformed_records_df = transform_data(cleanse_records_df)

reconciled_date_df = reconcile_data(transformed_records_df,target_df)

generate_summary(total_records_cnt,valid_records_cnt,rejected_records_cnt,reconciled_date_df)

