from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, EmailStr


class IncomingWalletRequestType(BaseModel):
    wallet_id: StrictStr = Field(..., title="Wallet ID")
    chain: StrictStr = Field(..., title="Chain")


class TokenInformationType(BaseModel):
    amount: StrictInt = Field(..., title="Amount")
    token_id: StrictInt = Field(..., title="Token ID")
    token_address: StrictStr = Field(..., title="Token Address")
    contract_type: StrictStr = Field(..., title="Contract Type")
    block_number: StrictInt = Field(..., title="Block Number")
