# Internationalization and Localization (i18n) Tasks for Flask App :smile:

This repository contains a series of tasks aimed at implementing internationalization and localization (i18n) features in a Flask application using Flask-Babel extension.

## Project Structure

The project is structured as follows:

- **Directories**:
  - `0x02-i18n`: Contains the Flask application code and related files for i18n tasks.
    - `templates`: Directory for HTML templates.
    - `translations`: Directory for language translation files.
  
- **Files**:
  - `0-app.py`: Basic Flask app setup with an index route and an initial HTML template.
  - `1-app.py`, `2-app.py`, ..., `7-app.py`: Flask app files for individual i18n tasks, progressively implementing various features.
  - `babel.cfg`: Configuration file for Babel extension.
  - `README.md`: Project documentation file (you're reading it!).
  
## Tasks Overview

Each task corresponds to a numbered app file and involves different aspects of i18n implementation:

1. **Basic Flask App Setup**: Setting up the initial Flask app with a basic route and template.
2. **Basic Babel Setup**: Configuring Flask-Babel extension, setting available languages, default locale, and timezone.
3. **Get Locale from Request**: Determining the best language match from request headers.
4. **Parametrize Templates**: Enabling translation using `_` or `gettext` functions in templates.
5. **Force Locale with URL Parameter**: Implementing forced locale via URL parameters.
6. **Mock Logging In**: Emulating user login behavior and displaying messages based on login status and language.
7. **Use User Locale**: Prioritizing locale selection based on user settings, URL parameters, and request headers.
8. **Infer Appropriate Time Zone**: Defining and validating time zones based on URL parameters and user settings.
9. **Display Current Time**: Showing the current time on the home page based on the inferred time zone.

## Running the Application

To run the Flask application:

1. Install necessary dependencies using `pip install -r requirements.txt`.
2. Execute the Flask app file for the desired task, e.g., `python 1-app.py`.
3. Access the app via the specified URL (e.g., `http://127.0.0.1:5000`) and test the implemented features.

## Usage

Each task builds upon the previous one, progressively enhancing the i18n features of the Flask app. Follow the instructions in each task's file and associated directories to complete the steps.

## Notes

- Ensure proper installation of Flask and Flask-Babel before running the application.
- Utilize Babel commands (`pybabel extract`, `pybabel init`, `pybabel compile`) as instructed in the tasks to manage translations.
