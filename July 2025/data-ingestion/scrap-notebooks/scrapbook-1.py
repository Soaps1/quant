import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def get_place_name(data, place_id):
    match = data.loc[data['place_id'] == place_id, 'name']
    if not match.empty:
        return match.iloc[0]
    else:
        return "No match"

def prompt_for_place_id(data):
    while True:
        place_id = input("Enter a place_id (or 'end' to quit): ")
        if place_id.lower() == "end":
            break
        result = get_place_name(data, place_id)
        print(f"Place name: {result}")

def main():
    data = load_data(r"C:\Users\Schalk\OneDrive - Columbia Business School\2025\quant\quinn_live_scores_20250704_163420.csv")
    prompt_for_place_id(data)

if __name__ == "__main__":
    main()