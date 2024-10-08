
# Mini Web Framework

This is a simple Python-based web framework using **Werkzeug** for request/response handling, routing, middleware support, and **Jinja2** for template rendering. It includes custom routing, static file serving, middleware implementation, and error handling.

## Project Structure

```
mini_framework/
│
├── app/
│   ├── __init__.py            # Initialize the app package
│   ├── views.py               # Application views (handlers)
│   ├── urls.py                # Routes (URL mappings)
│
├── framework/
│   ├── __init__.py            # Initialize the framework package
│   ├── app.py                 # Main MiniFramework class
│   ├── router.py              # Router for URL mappings
│   ├── static.py              # Static file serving
│   ├── template.py            # Template rendering with Jinja2
│   ├── middleware.py          # Middleware base class and implementation
│   ├── errors.py              # Error handling
│
├── static/
│   └── css/
│       └── style.css          # Sample static CSS file
│
├── templates/
│   └── home.html              # HTML template for the home page
│   └── profile.html           # HTML template for the profile page
│   └── 404.html               # Custom 404 error page
│   └── 500.html               # Custom 500 error page
│
├── run.py                     # Entry point to run the application
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## Features

- **Routing**: Define URL patterns and map them to view functions.
- **Middleware Support**: Add middleware for request and response processing.
- **Template Rendering (Jinja2)**: Use Jinja2 templates to render dynamic HTML pages.
- **Static File Serving**: Serve static assets like CSS, JS, images.
- **Error Handling**: Custom 404 and 500 error pages.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/imansadati/mini_web_framework.git
   cd mini_web_framework
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**

   ```bash
   python run.py
   ```

2. **Access the application:**

   Open your browser and navigate to:

   - Home page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Profile page: [http://127.0.0.1:8000/user/user_id>](http://127.0.0.1:8000/user/12)

## Middleware

You can add middleware by subclassing the `Middleware` class and overriding the `process_request` and `process_response` methods.


## Template Rendering (Jinja2)

Jinja2 is used to render dynamic HTML templates. Place your templates in the `templates/` directory, and use the `HtmlResponse()` class to render them.


## Static Files and Templates

- **Static Files**: Place your static files (e.g., CSS, JS) in the `static/` directory.
- **Templates**: HTML templates are located in the `templates/` directory.
