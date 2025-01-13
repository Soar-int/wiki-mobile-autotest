# wiki-mobile-autotest
This is a Python-based automation framework for testing the Wikipedia mobile app using Appium.

## Features

- Automates navigation and search functionalities.
- Tests settings options and validates UI elements.
- Uses the Page Object Model (POM) for better structure.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Soar-int/wiki-mobile-autotest.git
   cd <repository-folder>
   ```

2. Start the Appium server:
   ```bash
   appium
   ```

3. Update the device configuration in `conftest.py` if needed.

## Running Tests

Run all tests using pytest:
```bash
pytest test_task.py
```

## Folder Structure

- `conftest.py`: Appium driver setup.
- `locators.py`: Element locators for the app.
- `pages/`: Contains page object files (HomePage, SearchPage, SettingsPage).
- `test_task.py`: Test cases for navigation, search, and settings.

## Test Scenarios

1. Home Page navigation and scrolling.
2. Search functionality validation.
3. Settings options toggle.

## License

This project is open source. Feel free to use and modify.
