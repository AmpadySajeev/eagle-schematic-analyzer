# CircuitScope — EAGLE Schematic Analyzer

A Django web application that parses Autodesk EAGLE `.sch` schematic files and displays their components and electrical connections in a clear, searchable interface.

## Features

- Upload EAGLE `.sch` files.
- Extract component details, including reference, library, device set, device, and value.
- Extract electrical nets and their connected component pins.
- Display components and nets in separate tables.
- Search and filter table results.
- Validate file extensions and upload size.

## Technologies

- Python
- Django
- XML parsing with `xml.etree.ElementTree`
- HTML, CSS, JavaScript
- Bootstrap 5

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/AmpadySajeev/eagle-schematic-analyzer
cd eagle-schematic-analyzer
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Sample file

The repository includes `sample.sch`, which can be used to test the upload and parsing workflow.

## Project purpose

This project demonstrates file uploads, XML parsing, Django views and templates, input validation, and interactive presentation of structured data.
