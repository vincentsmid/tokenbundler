from moralis import evm_api

import json

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MORALIS_API_KEY")


class ResultItem:
    def __init__(self, item_data):
        for key, value in item_data.items():
            if key == "metadata" and value:
                try:
                    metadata = json.loads(value)
                    self.metadata_name = metadata.get("name", "Unknown Name")
                    self.metadata_description = metadata.get(
                        "description", "No description provided."
                    )
                except json.JSONDecodeError:
                    self.metadata_name = "Metadata parsing error"
                    self.metadata_description = "Metadata parsing error"
            elif key == "media" and value:
                self.media_low = (
                    value.get("media_collection", {})
                    .get("low", {})
                    .get("url", "No low-resolution media link.")
                )
            else:
                setattr(self, key, value)


async def get_wallet_tokens_no_price(address: str, chain: str):
    params_tokens_request = {"chain": chain, "address": address}

    result_tokens = evm_api.token.get_wallet_token_balances(
        api_key=api_key,
        params=params_tokens_request,
    )

    response = []
    for item in result_tokens:
        response_tokens = {
            "token_address": item["token_address"],
            "symbol": item["symbol"],
            "name": item["name"],
            "balance": item["balance"],
            "usd_value": 0,
            "usd_value_percent_change": 0,
            "image": item.get("logo", ""),
        }

        response.append(response_tokens)

    return json.dumps(response)


async def get_wallet_tokens_with_price(address: str, chain: str):
    params_tokens_request = {"chain": chain, "address": address}

    result_tokens = evm_api.wallets.get_wallet_token_balances_price(
        api_key=api_key,
        params=params_tokens_request,
    )

    result_items = [ResultItem(item) for item in result_tokens["result"]]
    response = []

    for item in result_items:
        response_tokens = {
            "token_address": item.token_address,
            "symbol": item.symbol,
            "name": item.name,
            "balance": item.balance_formatted,
            "usd_value": item.usd_value,
            "usd_value_percent_change": item.usd_price_24hr_percent_change,
            "image": item.thumbnail,
        }

        response.append(response_tokens)

    return json.dumps(response)


async def get_wallet_nft(address: str, chain: str):
    params_nft_request = {
        "chain": chain,
        "format": "decimal",
        "media_items": True,
        "address": address,
    }

    result_nft = evm_api.nft.get_wallet_nfts(
        api_key=api_key,
        params=params_nft_request,
    )

    result_items = [ResultItem(item) for item in result_nft["result"]]
    response = []

    for item in result_items:
        response_nft = {
            "amount": item.amount,
            "token_id": item.token_id,
            "token_address": item.token_address,
            "contract_type": item.contract_type,
            "block_number": item.block_number,
            "name": getattr(item, "metadata_name", "Unknown"),
            "description": getattr(
                item, "metadata_description", "No description provided."
            ),
            "image_link": getattr(item, "media_low", "No media link."),
        }

        response.append(response_nft)

    return json.dumps(response)
