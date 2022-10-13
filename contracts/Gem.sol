// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract Gem is ERC721Enumerable, ERC721URIStorage {

    uint256 private _totalSupply;

    mapping(address => bool) private _claimed;

    event gemClaimed(uint256 tokenId, address claimer);
    
    constructor(
        string memory _name, 
        string memory _symbol, 
        uint256 totalSupply_,
        string[] memory URIs
    ) 
    ERC721(_name, _symbol) {

        require(totalSupply_ == URIs.length, "Number of URIs doesn't correspond to total supply");

        _totalSupply = totalSupply_;

        // Minting gems
        for (uint256 tokenId_ = 0; tokenId_ < _totalSupply; tokenId_++) {
            _mint(address(this), tokenId_);
            _setTokenURI(tokenId_, URIs[tokenId_]);
        }
    }
    
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    } 

    function claim(uint256 tokenId) public payable returns (bool) {
        uint256 unclaimedNumber = balanceOf(address(this));
        require(unclaimedNumber > 0, "All gems are already claimed");
        require(!_claimed[msg.sender], "You have already claimed");
        require(ownerOf(tokenId) == address(this), "This gem is already claimed");

        _claimed[msg.sender] = true;
        _approve(msg.sender, tokenId);

        safeTransferFrom(address(this), msg.sender, tokenId);   

        emit gemClaimed(tokenId, msg.sender);
    }

    function unclaimedGems() public view returns (uint256[] memory) {  

        uint256[] memory result = new uint256[](balanceOf(address(this)));
        uint256 i = 0;

        for (uint256 _tokenId = 0; _tokenId < _totalSupply; _tokenId++) {
            if (ownerOf(_tokenId) == address(this)) {
                result[i] = _tokenId;
                i++;
            }
        }

        return result;
    }

    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable)
    {
        return super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage)
    {
        return super._burn(tokenId);
    }

    function supportsInterface(bytes4 interfaceId) public view override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}