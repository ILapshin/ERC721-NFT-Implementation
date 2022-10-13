import os
import json
import requests

from random import randint
from pathlib import Path
from dotenv import load_dotenv

from metadata.sample_metadata import metadata_template


load_dotenv()
JWT = os.environ.get('JWT')

PINATA_METADATA = {
    "name": "Gem NFT",
        "keyvalues": {
        "author": "ILapshin"
        }
}


def pin_file_on_pinata(file_name, file_path):

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload={
        'pinataOptions': '{"cidVersion": 1}', 
        'pinataMetadata': '{"name": "Gem NFT", "keyvalues": {"author": "ILapshin"}}'
    }
    files=[('file', (file_name, open(file_path,'rb'), 'application/octet-stream'))]
    headers = {'Authorization': f'Bearer {JWT}'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response


def pin_json_on_pinata(metadata: dict):
    
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    payload = json.dumps(
        {
            "pinataOptions": {"cidVersion": 1},
            "pinataMetadata": PINATA_METADATA,
            "pinataContent": metadata
        }
    )
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {JWT}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def create_uri_list(dir_path: Path):

    result = []

    for path in dir_path.iterdir():
        file_path = str(path)
        file_name = file_path.split('\\')[-1]
        
        r_file = pin_file_on_pinata(file_name, file_path)
        
        img_ipfs_hash = r_file.json()['IpfsHash']
        image_uri = f'https://ipfs.io/ipfs/{img_ipfs_hash}'

        print(f'Image uploaded on {image_uri}')

        metadata = metadata_template

        metadata['image'] = image_uri
        metadata['attributes'] = [
            {'trait_type': 'size', 'value': randint(50, 100)},
            {'trait_type': 'fancyness', 'value': randint(50, 100)}
        ]

        r_metadata = pin_json_on_pinata(metadata)

        metadata_ipfs_hash = r_metadata.json()['IpfsHash']
        metadata_uri = f'https://ipfs.io/ipfs/{metadata_ipfs_hash}'

        print(f'Metadata uploaded on {metadata_uri}')

        result.append(metadata_uri)

    return result

     