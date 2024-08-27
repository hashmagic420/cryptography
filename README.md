# Seed Phrase Encryption and Decryption

This project is a Streamlit app that allows users to securely encrypt and decrypt seed phrases using encryption keys. The app provides functionalities to generate encryption keys, encrypt seed phrases with these keys, and decrypt seed phrases using the provided keys.

## Features

- **Generate Encryption Key**: Create a new encryption key to use for encrypting and decrypting seed phrases.
- **Encrypt Seed Phrase**: Encrypt a seed phrase using a provided encryption key.
- **Decrypt Seed Phrase**: Decrypt an encrypted seed phrase using the provided encryption key.

## Installation

To run this Streamlit app locally, you need to have Python installed. Follow these steps to set up the project:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/hashmagic420/streamlit-seed-phrase-encryptor.git
Navigate to the Project Directory:

2. bash
Copy code
cd streamlit-seed-phrase-encryptor
Create a Virtual Environment (Optional but recommended):

3. bash
Copy code
python -m venv venv
Activate the Virtual Environment:

4. On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

5. bash
Copy code
source venv/bin/activate
Install Required Packages:

6. bash
Copy code
pip install -r requirements.txt
Running the App
To start the Streamlit app, use the following command:

7. bash
Copy code
streamlit run app.py
The app will open in your default web browser at http://localhost:8501.

Deployment
This app can be deployed to Streamlit Community Cloud. To deploy:

8. Go to Streamlit Community Cloud.
Log in with your GitHub account.
9. Create a New App:
Select this repository from the list.
Choose the branch and specify app.py as the file to run.
Deploy the app and access it via the URL provided by Streamlit Community Cloud.
Usage
10. Generate Key: Click on the "Generate Key" option to create a new encryption key.
Encrypt Seed Phrase: Enter a seed phrase and an encryption key, then click "Encrypt" to get the encrypted seed phrase.
Decrypt Seed Phrase: Enter the encrypted seed phrase and the encryption key to retrieve the original seed phrase.
Contributing
Feel free to open issues or submit pull requests to contribute to the project. For major changes, please open an issue first to discuss what you would like to change.

11. License
This project is licensed under the MIT License - see the LICENSE file for details.

12. Contact
If you have any questions or feedback, you can reach out to hashmagic420@gmail.com.




