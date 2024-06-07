### Step 3: `requirements.txt`
To install the dependencies listed in `requirements.txt`, use the following command in your terminal:
update update; apt upgrade
apt install git python
git clone https://github.com/Nepalese-Noob/tscrap
cd tscrap
pip install -r requirements.txt
python3 runner.py



Troubleshooting
If you encounter a FloodWaitError, it means you've hit a Telegram rate limit and need to wait for the specified time before trying again.
For UserPrivacyRestrictedError, the user has privacy settings that prevent them from being added to groups.
perl

Final Structure
Your project directory should look like this:

Copy code
.
├── runner.py
├── requirements.txt
└── README.md
With these files in place, you should be able to set up and run your script successfully.
