from fastapi import APIRouter

from main_app.api.api_v1.endpoints import nft_info, token_info

router = APIRouter()


router.include_router(nft_info.router, tags=["info"], prefix="/nft_info")
router.include_router(token_info.router, tags=["info"], prefix="/token_info")
