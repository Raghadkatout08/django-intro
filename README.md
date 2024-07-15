# django-intro

## Pages

- **Home Page**: Rendered at the root route `/`.
- **About Page**: Rendered at `/about`.
- **Contact Page**: Rendered at `/contact`.

## Setup Instructions

1. Clone this repository.
2. Create a virtual environment: `python -m venv .venv`.
3. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.
5. Apply migrations: `python manage.py migrate`.
6. Run the development server: `python manage.py runserver`.

## Testing

- Ensure all tests pass: `python manage.py test myapp`.