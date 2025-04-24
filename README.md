
# WebApp Health Check Dashboard

## Features
- Automates login to WebUI apps using Selenium.
- Checks if app is UP or DOWN.
- Displays status on Flask dashboard with auto-refresh.

## Setup Instructions
1. Install Python packages:
   ```
   pip install -r requirements.txt
   ```

2. Download ChromeDriver matching your Chrome version:
   - https://chromedriver.chromium.org/downloads
   - Place it in your system PATH.

3. Update `apps_config.json` with real application details.

4. Run the Flask app:
   ```
   python app.py
   ```

5. Visit `http://127.0.0.1:5000` to view the dashboard.

## Note
- This uses headless Chrome via Selenium for login checks.
- Auto-refreshes every 60 seconds.
