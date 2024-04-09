from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import ForwardRef


class IncomingWalletRequestType(BaseModel):
    wallet_id: StrictStr = Field(..., title="Wallet ID")
    chain: StrictStr = Field(..., title="Chain")


class NftInformationType(BaseModel):
    amount: StrictInt = Field(..., title="Amount")
    token_id: StrictInt = Field(..., title="Token ID")
    token_address: StrictStr = Field(..., title="Token Address")
    contract_type: StrictStr = Field(..., title="Contract Type")
    block_number: StrictInt = Field(..., title="Block Number")
    name: StrictStr = Field(..., title="Name")
    description: StrictStr = Field(..., title="Description")
    image_link: StrictStr = Field(..., title="Image Link")

class TokenInformationType(BaseModel):
    token_address: StrictStr = Field(..., title="Token Address")
    symbol: StrictStr = Field(..., title="Symbol")
    name: StrictStr = Field(..., title="Name")
    balance: StrictStr = Field(..., title="Balance")
    usd_value: StrictStr = Field(..., title="USD Value")
    usd_value_percent_change: StrictStr = Field(..., title="USD Value Percent Change")
    image: StrictStr = Field(..., title="Image")