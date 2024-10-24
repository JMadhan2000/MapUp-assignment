import pandas as pd

def calculate_distance_matrix(df):
    distance_matrix = df.pivot_table(index='id_start', columns='id_end', values='distance', fill_value=0)

    for i in distance_matrix.index:
        for j in distance_matrix.columns:
            if distance_matrix.at[i, j] == 0:
                distance_matrix.at[i, j] = distance_matrix.at[j, i]

    return distance_matrix







def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:  
                unrolled_data.append({
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': distance_matrix.at[id_start, id_end]
                })
    return pd.DataFrame(unrolled_data)







def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):
    reference_avg_distance = unrolled_df[unrolled_df['id_start'] == reference_id]['distance'].mean()

    threshold_min = reference_avg_distance * 0.9
    threshold_max = reference_avg_distance * 1.1

    average_distances = unrolled_df.groupby('id_start')['distance'].mean()
    within_threshold = average_distances[(average_distances >= threshold_min) & (average_distances <= threshold_max)]

    return within_threshold.index.tolist()







def calculate_toll_rate(unrolled_df):
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, rate in rate_coefficients.items():
        unrolled_df[vehicle_type] = unrolled_df['distance'] * rate

    return unrolled_df







import datetime

def calculate_time_based_toll_rates(unrolled_df):
    unrolled_df['start_day'] = 'Monday' 
    unrolled_df['start_time'] = datetime.time(0, 0)  
    unrolled_df['end_day'] = 'Monday'
    unrolled_df['end_time'] = datetime.time(23, 59, 59)

    weekday_discounts = {
        '00:00:00-10:00:00': 0.8,
        '10:00:00-18:00:00': 1.2,
        '18:00:00-23:59:59': 0.8
    }
    weekend_discount = 0.7

    def apply_time_based_discount(row):
        if row['start_day'] in ['Saturday', 'Sunday']:
            factor = weekend_discount
        else:
            start_time = row['start_time']
            if start_time < datetime.time(10, 0):
                factor = 0.8
            elif start_time < datetime.time(18, 0):
                factor = 1.2
            else:
                factor = 0.8
        for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
            row[vehicle] *= factor
        return row

    unrolled_df = unrolled_df.apply(apply_time_based_discount, axis=1)
    return unrolled_df