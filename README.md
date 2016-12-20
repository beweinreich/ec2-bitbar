# EC2 Bit Bar

I was getting tired of logging into AWS to get the EC2 instance IP addresses, and then having to ssh in. Here's a quick way to login if your private keys are in the ~/.ssh folder.

## Installation

1. Go download BitBar: https://github.com/matryer/bitbar/releases/tag/v1.9.2
2. `sudo pip install boto3`
3. Launch BitBar and put the `ec2.10m.py` file in the BitBar plugins directory.
4. You're done.