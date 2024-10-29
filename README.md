# Email Salary Calculator

This script connects to a Gmail account, filters emails from a specified sender, and calculates the total salary received based on specific criteria in the email body.

## Prerequisites

- Python 3.x installed on your machine.
- Access to a Gmail account with IMAP enabled.
- Basic knowledge of using the command line.

## Installation

1. **Clone the repository or download the script** to your local machine.

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Install required Python packages**. You can use pip to install the necessary packages. Open your terminal or command prompt and run:

    ```bash
    pip install python-dotenv beautifulsoup4
    ```

3. **Set up a `.env` file** in the project directory to store your email credentials securely. Create a file named `.env` and add the following lines:

    ```
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASS=your_email_password
    BOSS_NAMES=Your_Boss_Name1,Your_Boss_Name2
    ```

    Replace `your_email@gmail.com` and `your_email_password` with your actual Gmail email address and password. Replace `Your_Boss_Name1,Your_Boss_Name2` with the names of your bosses, separated by commas.

    **Important**: If you have two-factor authentication enabled, you will need to generate an [App Password](https://support.google.com/accounts/answer/185201) and use that instead of your regular password.

4. **Enable IMAP in your Gmail account**:
   - Go to your Gmail settings.
   - Under "Forwarding and POP/IMAP", enable IMAP.

## Usage

1. **Open Visual Studio Code**.

2. **Open the terminal in VS Code** (View > Terminal).

3. **Run the script** by executing:

    ```bash
    python your_script_name.py
    ```

   Replace `your_script_name.py` with the name of your script file.

## Script Functionality

- The script connects to your Gmail account via IMAP and logs in using the credentials from the `.env` file.
- It searches for emails from `ibanking.alert@dbs.com` in your inbox.
- For each email that matches the criteria (subject contains "Transaction Alerts" and the body contains your boss's name), it extracts the salary amount.
- It calculates and prints the total salary along with the amount added for each relevant email.

## Important Notes

- Make sure to keep your `.env` file secure and do not share it publicly as it contains sensitive information.
- The script uses BeautifulSoup to parse HTML emails and extract text from them. 

## Troubleshooting

- If you encounter issues logging in, ensure that IMAP is enabled in your Gmail settings.
- If you're unable to install packages, make sure that pip is correctly installed and configured in your environment.

## License

This project is licensed under Ye Yint Aung.
