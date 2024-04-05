from fastapi import APIRouter, Form, HTTPException
import logging
from main_app.schemas import IncomingWalletRequestType
from main_app.wallet_info import get_wallet_nft

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/")
async def token_info(wallet_info: IncomingWalletRequestType):
    logger.info(f"wallet_info: {wallet_info}")
    wallet_var = wallet_info.wallet_id
    chain_var = wallet_info.chain

    try:
        result = await get_wallet_nft(wallet_var, chain_var)
        return result
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))