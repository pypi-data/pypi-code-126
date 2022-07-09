import os

import asyncio

from cevlib.match import Match, MatchCache

from cevlib.competitions import Competition

async def main():
    #match = await Match.byUrl("https://www.cev.eu/match-centres/2022-european-cups/cev-volleyball-challenge-cup-2022-men/chcm-60-narbonne-volley-v-sporting-cp-lisboa/")

    #cache = await match.cache()
    #print("currentScore", cache.result)
    comp = await Competition.fromUrl("http://www.cev.eu/national-team/european-league/european-golden-league/men/")
    print(comp)

if os.name == "nt": # windows only
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
