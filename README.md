# WhatsApp Message Bomber

This Python script uses Selenium to automate the process of sending multiple messages to a contact on WhatsApp Web.

## Requirements

- Python 3.x
- Selenium library
- Chrome WebDriver
- Google Chrome browser

## Installation

1. **Install Python dependencies:**

    ```sh
    pip install selenium
    ```

2. **Download and install Chrome WebDriver:**

    - Ensure that the version of Chrome WebDriver matches your installed version of Google Chrome.
    - Download Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Extract the downloaded file and place it in a directory included in your system's PATH.

## Usage

1. **Save the script:**

    Save the provided script as `whatsapp_bomber.py`.

2. **Run the script:**

    Open a terminal or command prompt and navigate to the directory where `whatsapp_bomber.py` is saved. Run the script using:

    ```sh
    python whatsapp_bomber.py
    ```

3. **Scan the QR code:**

    - The script will open WhatsApp Web in a new Chrome window.
    - Use your phone to scan the QR code displayed.
    - After scanning, return to the terminal and press Enter.

4. **Monitor the process:**

    - The script will search for the specified contact and send 1000 messages.
    - You can monitor the process in the terminal.

## Script Details
