import json

def export_to_json(data):
    with open("app/output/results.json", "w") as f:
        json.dump(data, f)
