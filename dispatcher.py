import logging
from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
import settings

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not settings.BOT_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)