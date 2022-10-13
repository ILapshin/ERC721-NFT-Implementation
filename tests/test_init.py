from scripts.deploy import *
import pytest
from brownie import Gem, network, accounts


uri_list = ['First test URI', 'Second test URI', 'Third test URI']

def test_deploy_fails():
    # Arrange 
    if network.show_active() != 'development':
       pytest.skip('Only for testnet testing') 

    account = accounts[0]   
    
    # Act - assert
    with pytest.raises(Exception) as e_info:
        failed_gem = Gem.deploy('Test', 'TEST', 2, uri_list, {'from': account})


def test_deploy_secceeded():
    # Arrange 
    if network.show_active() != 'development':
       pytest.skip('Only for testnet testing') 

    account = accounts[0]   
    
    # Act - assert
    assert Gem.deploy('Test', 'TEST', 3, uri_list, {'from': account})


def test_claim():
    # Arrange 
    if network.show_active() != 'development':
       pytest.skip('Only for testnet testing')
    
    account = accounts[0]
    gem = Gem.deploy('Test', 'TEST', 3, uri_list, {'from': account})

    # Act
    gem.claim(0, {'from': account})
    
    #Assert
    assert gem.balanceOf(account) == 1


def test_claim_failed():
    # Arrange 
    if network.show_active() != 'development':
       pytest.skip('Only for testnet testing')
    
    account = accounts[0]
    gem = Gem.deploy('Test', 'TEST', 3, uri_list, {'from': account})
    gem.claim(0, {'from': account})

    # Act - assert
    with pytest.raises(Exception) as e_info:
        gem.claim(0, {'from': account})
    

    
    
