# 💫 Module by @peanguin_peanguin

import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class GunAnimationMod(loader.Module):
    """Gun Animation Module"""
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "PewPew",
               "after_sleep": "We have finished sleeping!"}


    async def guncmd(self, message):
        """*Pew Pew* Bang! Displays cool shooting animations with bullets."""
        gun_animation = [
            "🔫",
            "🔫🔫",
            "🔫🔫🔫",
            "🔫🔫🔫🔫",
            "🔫🔫🔫🔫🔫",
            "🔫🔫🔫🔫🔫🔫",
            "🔫🔫🔫🔫🔫🔫🔫",
            "🔫🔫🔫🔫🔫🔫",
            "🔫🔫🔫🔫🔫",
            "🔫🔫🔫🔫",
            "🔫🔫🔫",
            "🔫🔫",
            "🔫"
        ]

        bullet_animation = [
            "🔴",
            "🟡",
            "🟢",
            "🔵"
        ]

        await message.edit("Ready to shoot!")

        for _ in range(3):  # Fire three shots
            for gun, bullet in zip(gun_animation, bullet_animation):
                await message.edit(f"{gun}\n{bullet}")
                await asyncio.sleep(0.2)

        await message.edit("🔫 *Pew Pew* Bang! *Pew Pew*")
        await asyncio.sleep(0.5)
        
        # Delete the original message
        await message.delete()

        # Add a delay before the final message
        await asyncio.sleep(1)

        # Send the final message
        await message.respond("Ты был убит самой быстрой пулей на диком западе..☠️")

    def __init__(self):
        self.license = "This module is licensed under the Dixswr License."
        self.author = "dixswr"

