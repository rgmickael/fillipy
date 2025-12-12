# Fillipy

A command-line tool for automatically filling PDF forms with data. Fillipy reads JSON data and populates a template PDF with the provided information, generating a new filled PDF file.

## Description

Fillipy simplifies the process of filling fillable PDF forms programmatically. Instead of manually entering data into PDF forms, you can provide your data in JSON format and let Fillipy automatically populate all form fields in a template PDF. This is particularly useful for batch processing, automation workflows, or integrating PDF form filling into larger applications.

## Features

- **JSON-based data input**: Pass form data as JSON strings
- **Automatic field mapping**: Automatically maps JSON data to PDF form fields in order
- **Error handling**: Validates JSON data and checks for missing PDF files
- **Command-line interface**: Easy to use and integrate into scripts or applications

## Installation

### Requirements

- Python 3.x
- Dependencies listed in `requirement.txt`

### Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

## Usage

Run the script with three arguments:

```bash
python main.py <json_data> <template_pdf> <output_pdf>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `json_data` | JSON array or data structure containing the form field values |
| `template_pdf` | Path to the fillable PDF template file |
| `output_pdf` | Path where the filled PDF will be saved |

### Example

```bash
python main.py '["John Doe", "123 Main Street", "john@example.com"]' "form_template.pdf" "filled_form.pdf"
```

### Example with JSON object

```bash
python main.py '{"field1": "value1", "field2": "value2"}' "template.pdf" "output.pdf"
```

## How It Works

1. The script reads the template PDF and extracts all form field names
2. Parses the provided JSON data
3. Maps the JSON values to the form fields in order
4. Generates a new PDF with all fields filled
5. Saves the completed PDF to the specified output path

## Error Handling

The script provides helpful error messages for common issues:

- **Missing arguments**: Displays usage instructions
- **Invalid JSON**: Reports JSON parsing errors
- **Missing template file**: Alerts if the template PDF cannot be found
- **Other errors**: Catches and reports unexpected exceptions

## Dependencies

- `fillpdf`: Core PDF form filling library
- `pdf2image`: PDF to image conversion
- `pdfrw2`: PDF reading and writing
- `PyMuPDF`: Advanced PDF manipulation
- `pillow`: Image processing
- `pyinstaller`: For creating standalone executables

## License

This project is licensed under the MIT License. For more details, see [MIT License](https://opensource.org/licenses/MIT).

## Author

Developed by rgmickael
