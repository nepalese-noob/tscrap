The purpose of the tool is to scrape members from one Telegram group and add them to another group quickly and efficiently. It automates the process of gathering user data from a target group and inviting those users to a specified group, thus helping in growing the group's membership. This can be useful for managing and expanding Telegram communities.

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
the files must be....


├── runner.py

├── requirements.txt

└── README.md

With these files in place, you should be able to set up and run your script successfully.
