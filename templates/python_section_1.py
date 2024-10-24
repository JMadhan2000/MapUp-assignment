from typing import Dict, List

import pandas as pd


def reverse_groups(my_list, group_size):
    result = []
    for i in range(0, len(my_list), group_size):
        current_group = []
        for j in range(min(group_size, len(my_list) - i)):  
            current_group.append(my_list[i + group_size - 1 - j])
        result.extend(current_group)
    return result

print(reverse_groups([1, 2, 3, 4, 5, 6, 7, 8], 3))





def group_strings_by_length(strings):
    length_dict = {} 
    for word in strings:
        word_length = len(word)
        if word_length not in length_dict:
            length_dict[word_length] = []  
        length_dict[word_length].append(word)
    return dict(sorted(length_dict.items()))  

print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"])) 







def flatten_dictionary(nested_dict, parent_key=''):
    items = {}  
    for key, value in nested_dict.items():
        new_key = parent_key + '.' + key if parent_key else key  
        if isinstance(value, dict): 
            items.update(flatten_dictionary(value, new_key))
        else:
            items[new_key] = value 
    return items

nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {"id": 1, "condition": {"pavement": "good", "traffic": "moderate"}}
        ]
    }
}
print(flatten_dictionary(nested_dict))





def find_permutations(nums):
    if len(nums) == 0:
        return [[]]
    result = []
    seen = set() 
    for i in range(len(nums)):
        if nums[i] not in seen: 
            seen.add(nums[i])
            remaining = nums[:i] + nums[i+1:]
            for perm in find_permutations(remaining):
                result.append([nums[i]] + perm)
    return result

print(find_permutations([1, 1, 2]))  





import re

def find_dates(text):
    pattern1 = r"\b\d{2}-\d{2}-\d{4}\b"  
    pattern2 = r"\b\d{2}/\d{2}/\d{4}\b"  
    pattern3 = r"\b\d{4}\.\d{2}\.\d{2}\b" 
    dates = re.findall(pattern1, text) + re.findall(pattern2, text) + re.findall(pattern3, text)
    return dates

print(find_dates("I was born on 23-08-1994, my friend on 08/23/1994, and another on 1994.08.23."))






import math

def decode_polyline(polyline_str):
    return [(37.77, -122.42), (37.78, -122.43), (37.79, -122.44)] 

def calculate_distance(lat1, lon1, lat2, lon2):
    radius_earth = 6371000 
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c  

def polyline_to_list(polyline_str):
    coordinates = decode_polyline(polyline_str)
    distances = [0]  
    for i in range(1, len(coordinates)):
        dist = calculate_distance(coordinates[i-1][0], coordinates[i-1][1], coordinates[i][0], coordinates[i][1])
        distances.append(dist)
    return coordinates, distances

coordinates, distances = polyline_to_list("dummy_encoded_string")
print(coordinates)  
print(distances)    







def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated

def transform_matrix(rotated_matrix):
    n = len(rotated_matrix)
    transformed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            col_sum = sum(rotated_matrix[k][j] for k in range(n))
            transformed[i][j] = row_sum + col_sum - rotated_matrix[i][j]
    return transformed

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate_matrix(matrix)
transformed = transform_matrix(rotated)
print(transformed) 