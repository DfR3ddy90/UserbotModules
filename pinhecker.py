#the module by dixswr @peanguin_peanguin

import logging
from datetime import datetime
import random
import asyncio 

from .. import loader

logger = logging.getLogger(name)

@loader.tds
class PingLoverMod(loader.Module):
    """Модуль для измерения разных пингов бота."""
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "PingLover",
               "after_sleep": "We have finished sleeping!"}

    async def pingcmd(self, message):
        """Измеряет разные пинги бота и выводит результат."""
        pings = []
        for _ in range(5):  # Можете изменить количество пингов
            start = datetime.now()
            await message.edit("Измерение пинга... ⏳")
            end = datetime.now()
            ping = (end - start).microseconds / 1000
            pings.append(ping)
            await message.edit(f"🏓 Пинг {len(pings)}: {ping} мс")
            await asyncio.sleep(1)  # Задержка между измерениями

        average_ping = sum(pings) / len(pings)
        min_ping = min(pings)
        max_ping = max(pings)

        result_message = (
            f"💥 Средний пинг: {average_ping:.2f} мс\n"
            f"🌟 Минимальный пинг: {min_ping} мс\n"
            f"☠️ Максимальный пинг: {max_ping} мс\n"
        )

        await message.edit(result_message)

    async def phelpcmd(self, message):
        """Отображает информацию о команде .ping."""
        await message.edit("Команда .ping измеряет разные пинги бота и выводит средний, минимальный и максимальный пинг в миллисекундах.")

    def init(self):
        self.name = "Модуль Проверки Пинга"
        self.description = "Этот модуль позволяет измерить разные пинги бота и вычислить средний, минимальный и максимальный пинг."
        self.version = "1.0"
