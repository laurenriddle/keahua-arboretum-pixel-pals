# Function for returning list of biomes a selected plant can be added to
def get_plant_biomes(plant, arboretum):
    '''Function that returns a list of biomes in an arboretum that
    match the requirements of a given plant.

    ARGUMENTS:
    plant (object)
    arboretum (object)
    '''
    plant_biomes = []

    required_biomes = plant.required_locations
    all_biomes = arboretum.biomes
    for required_biome in required_biomes:
        for potential_biome, value in all_biomes.items():
            # if the biome in the arboretum is in required biomes of given plant
            if potential_biome == required_biome:
                for biome in all_biomes[potential_biome]:
                    # check each biome to make sure it is not full
                    if not biome.is_plants_full():
                        # add biomes to plant_biomes list
                        plant_biomes.append(biome)
            
    return plant_biomes