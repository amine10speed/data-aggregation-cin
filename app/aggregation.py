import json
import csv

def aggregate_data(data):
    """
    Aggregate data from multiple sources.
    :param data: Dictionary containing extracted field data from previous services.
    :return: Aggregated data.
    """
    # Example aggregation logic
    aggregated_data = {
        "id_number": data.get("id_number"),
        "name": data.get("name"),
        "family_name": data.get("family_name"),
        "date_of_birth": data.get("date_of_birth"),
        "place_of_birth": data.get("place_of_birth"),
        "expiration_date": data.get("expiration_date"),
        "arabic_name": data.get("arabic_name"),
        "arabic_family_name": data.get("arabic_family_name"),
        "place_of_birth_arabic": data.get("place_of_birth_arabic"),
    }
    return aggregated_data

def export_to_json(aggregated_data, output_path="output.json"):
    """
    Export aggregated data to a JSON file.
    :param aggregated_data: Aggregated data dictionary.
    :param output_path: Path to save the JSON file.
    """
    with open(output_path, "w") as json_file:
        json.dump(aggregated_data, json_file, indent=4)

def export_to_csv(aggregated_data, output_path="output.csv"):
    """
    Export aggregated data to a CSV file.
    :param aggregated_data: Aggregated data dictionary.
    :param output_path: Path to save the CSV file.
    """
    with open(output_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(aggregated_data.keys())
        writer.writerow(aggregated_data.values())
