import json
import sys
from fillpdf import fillpdfs

# Get data from command line arguments
if len(sys.argv) > 3:
    json_data = sys.argv[1]
    template_pdf = sys.argv[2]
    output_pdf = sys.argv[3]
    args = json.loads(json_data)
else:
    print("Error: Missing arguments. Usage: python main.py <json_data> <template_pdf> <output_pdf>")
    sys.exit(1)

try:
    # Remove any extra quotes that might be added by the shell
    json_data = json_data.strip().strip("'").strip('"')
    args = json.loads(json_data)
    print(f"Parsed JSON: {args}")
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON data - {e}")
    print(f"Data received: {repr(json_data)}")
    sys.exit(1)

print(f"Template PDF: {template_pdf}")
print(f"Output PDF: {output_pdf}")

try:
    form_fields = list(fillpdfs.get_form_fields(template_pdf).keys())
    
    print(f"Number of form fields: {len(form_fields)}")
    print(f"Number of fields sent: {len(args)}")
    
    data_dict = {}
    for i in range(len(form_fields)):
        if i < len(args):
            data_dict[form_fields[i]] = str(args[i])

    print("Filling PDF...")
    fillpdfs.write_fillable_pdf(template_pdf, output_pdf, data_dict)
    print("PDF filled successfully!")
    
except FileNotFoundError:
    print(f"Error: Template file '{template_pdf}' not found!")
    sys.exit(1)
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)