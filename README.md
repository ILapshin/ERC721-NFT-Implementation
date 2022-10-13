# Simple ERC-721 Non-fungible Token implementation

An ERC-721 NFT smart contract representing some AI-generated images of fancy gems with additional metadata. 

Images and metadata are uploaded on IPFS via [Pinata](https://www.pinata.cloud/) using create_metadata.py script.

Smart contract is deployed on Polygon Mumbai test chain on address [0xEe09c50a9c5cBC57CBbAd3810BF720Eff48164Ea](https://mumbai.polygonscan.com/address/0xee09c50a9c5cbc57cbbad3810bf720eff48164ea). You can claim one of the remaining tokens using *claim* method. Find which tokens are not claimed yet you can via *unclaimedGems* view method.

Developed using [Openzeppelin ERC721 contract](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/token/ERC721) incluiding Unumerable and URIStorage extensions.

