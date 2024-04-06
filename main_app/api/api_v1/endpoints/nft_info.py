from fastapi import APIRouter, HTTPException, Query, Depends
import logging
from main_app.schemas import IncomingWalletRequestType
from main_app.wallet_info import get_wallet_nft
from main_app.redis_config import redis_dependency
import redis

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/")
async def token_info(
    wallet_info: IncomingWalletRequestType,
    refresh: bool = Query(False, description="Set to true to refresh cache"),
    r: redis.Redis = Depends(redis_dependency),
):
    logger.info(f"wallet_info: {wallet_info}")
    wallet_var = wallet_info.wallet_id
    chain_var = wallet_info.chain

    cache_key = f"{wallet_var}:{chain_var}:nft"

    try:
        if refresh:
            logger.info("Cache refresh requested.")
            result = None
        else:
            print("Cache hit")
            result = r.get(cache_key)

        if not result:
            print("Cache miss")
            result = await get_wallet_nft(wallet_var, chain_var)
            print(result)
            r.set(cache_key, result, ex=3600)

        return result
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


# TODO: add decorator
