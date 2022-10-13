import os

from dotenv import load_dotenv
from pathlib import Path

from brownie import Gem, accounts
from scripts.create_metadata import create_uri_list

load_dotenv()
JWT = os.environ.get('JWT')


def main():  

    dir_path = Path('./img/golden-ball')

    uri_list = create_uri_list(dir_path)

    account = accounts.load('metamask-dev')

    gem = Gem.deploy('GoldenBall', 'GEM', 13, uri_list, {'from': account}, publish_source=True)

    print(gem)

