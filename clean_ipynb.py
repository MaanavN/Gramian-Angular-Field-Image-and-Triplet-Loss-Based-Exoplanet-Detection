# cat shift_margin_test.ipynb | jq 'del(.metadata.widgets)' > shift_margin_test_clean.ipynb


import json
import os

def clean_notebook(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remove .metadata.widgets if it exists
    if 'metadata' in data and 'widgets' in data['metadata']:
        del data['metadata']['widgets']
        print(f"Removed .metadata.widgets from {input_file}")
    else:
        print(f"No .metadata.widgets found in {input_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)
    
    print(f"Cleaned notebook saved to {output_file}")

if __name__ == "__main__":
    file = input("Notebook path: ")
    clean_notebook(file, f'{file}_clean.ipynb')
