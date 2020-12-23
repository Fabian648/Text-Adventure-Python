import json
import configparser

def create_map_base(size=20):
    config = configparser.ConfigParser()
    maper = "map_" + str(size)
    try:
        config.read('TA_Data\\src\\mapblueprints\\mapblueprint.ini')
        map = json.loads(config.get("MAPBLUEPRINTS", maper))
    except:
        with open('TA_Data\\src\\mapblueprints\\mapblueprint.ini', 'a') as file:
            x = []
            y = []

                # poplulates the y slots 
            for height in range(size):
                y.append([])
            #print(y)
            # poplulates the x colum
            for width in range(size):
                x.append(y)
                
            file.write("\n\nmap_"+ str(size) + " = " + str(x)+ " ")
            
    finally:
        config.read('TA_Data\\src\\mapblueprints\\mapblueprint.ini')
        map = json.loads(config.get("MAPBLUEPRINTS", maper))
        return map
