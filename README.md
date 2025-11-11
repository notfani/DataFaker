# DataFaker

This simple data writer on Python to make big test data set. P.S. GitHub told me to name this repo as a "friendly-panckake".

## Features

- Generates hierarchical JSON data with parent-child relationships.
- Supports multiple root nodes (`prime` nodes).
- Randomized branching to create complex data structures.
- Configurable number of records.

## Usage

1. Clone the repository.
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter the desired number of records when prompted.
4. The generated data will be saved in `data.json`.

## Example Output

```json
[
    {
        "id": 1,
        "parent_id": null,
        "ancestor_id": null,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "parent_id": 1,
        "ancestor_id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    },
    {
        "id": 3,
        "parent_id": null,
        "ancestor_id": null,
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }
]
```
