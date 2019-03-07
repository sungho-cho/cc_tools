import cc_data
import cc_dat_utils
import json

def make_data_file_from_json(json_data):
    data_file = cc_data.CCDataFile()

    # Parse all levels
    for level_data in json_data["levels"]:
        level = cc_data.CCLevel()
        level.level_number = level_data["level_number"]
        level.time = level_data["time"]
        level.num_chips = level_data["num_chips"]
        level.upper_layer = level_data["upper_layer"]
        level.lower_layer = level_data["lower_layer"]

        # Parse all optional fields
        for field_data in level_data["optional_fields"]:
            field = None
            type_val = field_data["type_val"]

            # Parse Map Title
            if (type_val == 3):
                title = field_data["title"]
                field = cc_data.CCMapTitleField(title)

            # Parse Traps
            elif (type_val == 4):
                traps = []
                for trap_data in field_data["traps"]:
                    bx = trap_data["bx"]
                    by = trap_data["by"]
                    tx = trap_data["tx"]
                    ty = trap_data["ty"]
                    trap = cc_data.CCTrapControl(bx,by,tx,ty)
                    traps.append(trap)
                field = cc_data.CCTrapControlsField(traps)

            # Parse Clone Machines
            elif (type_val == 5):
                machines = []
                for machine_data in field_data["machines"]:
                    bx = machine_data["bx"]
                    by = machine_data["by"]
                    tx = machine_data["tx"]
                    ty = machine_data["ty"]
                    machine = cc_data.CCCloningMachineControl(bx,by,tx,ty)
                    machines.append(machine)
                field = cc_data.CCCloningMachineControlsField(machines)

            # Parse Password
            elif (type_val == 6):
                password = field_data["password"]
                field = cc_data.CCEncodedPasswordField(password)

            # Parse Hint
            elif (type_val == 7):
                hint = field_data["hint"]
                field = cc_data.CCMapHintField(hint)

            # Parse Moving Monsters
            elif (type_val == 10):
                monsters = []
                for monster_data in field_data["monsters"]:
                    x = monster_data["x"]
                    y = monster_data["y"]
                    monster = cc_data.CCCoordinate(x,y)
                    monsters.append(monster)
                field = cc_data.CCMonsterMovementField(monsters)

            level.add_field(field)

        data_file.add_level(level)

    return data_file

#Part 3
fileName = "data/sunghoch_cc2"

#Load your custom JSON file
input_json_file = fileName + ".json"
with open(input_json_file, "r") as reader:
    data = json.load(reader)
#Convert JSON data to cc_data
data_file = make_data_file_from_json(data)
#Save converted data to DAT file
output_dat_file = fileName + ".dat"
cc_dat_utils.write_cc_data_to_dat(data_file, output_dat_file)
