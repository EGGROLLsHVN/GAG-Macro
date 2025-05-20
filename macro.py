seeds = {
    # Seed Shop:
    "Carrot": False,
    "Strawberry": False,
    "Blueberry": False,
    "OrangeTulip": False,
    "TomatoSeed": False,
    "CornSeed": False,
    "WatermelonSeed": False,
    "PumpkinSeed": False,
    "AppleSeed": False,
    "BambooSeed": False,
    "CoconutSeed": False,
    "CactusSeed": False,
    "DragonFruitSeed": False,
    "MangoSeed": False,
    "GrapeSeed": False,
    "MushroomSeed": False,
    "PepperSeedCacaoSeed": False,
    "BeanstalkSeed": False,

    # Bloodmoon Shop:
    "MysteriousCrate": False,
    "NightEgg": False,
    "NightSeedPack": False,
    "BloodBananaSeed": False,
    "MoonMelonSeed": False,
    "StarCaller": False,
    "BloodKiwi": False,
    "BloodHedgehog": False,
    "BloodOwl": False,

    # Gear:
    "WateringCan": False,
    "Trowel": False,
    "RecallWrench": False,
    "BasicSprinkler": False,
    "AdvancedSprinkler": False,
    "GodlySprinkler": False,
    "LightningRod": False,
    "MasterSprinkler": False,
    "FavoriteTool": False,

    # Eggshop:
    "All": False
}

class Macro():
    def __init__(self, seed_data):
        self.seed_data = seed_data  # Store the seeds dictionary

    def run(self):
        if self.seed_data.get("Carrot", False):
            self.carrotCollect()

        if self.seed_data.get("Strawberry", False):
            self.strawberryCollect()


    def carrotCollect():
        print()
    
    def strawberryCollect():
        print()



