import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file

json_file_name = "data/kcl2_cc1.json"

with open(json_file_name, "r") as reader:
    level_pack_json_data = json.load(reader)
level_pack_data = level_pack_json_data["Levels"]
new_level_pack = cc_classes.CCLevelPack()
for level in level_pack_data:
    new_level = cc_classes.CCLevel()
    new_level.level_number = level["level_number"]
    new_level.time = level["time"]
    new_level.num_chips = level["num_chips"]
    new_level.upper_layer = level["upper_layer"]

    optional_fields_data = level["optional_fields"]

    #for field in optional_fields_data:
    new_map_title_field = cc_classes.CCMapTitleField(optional_fields_data["CCMapTitleField"])
    new_level.add_field(new_map_title_field)

    encoded_password_field = cc_classes.CCEncodedPasswordField(optional_fields_data["CCEncodedPasswordField"])
    new_level.add_field(encoded_password_field)

    map_hint_field = cc_classes.CCMapHintField(optional_fields_data["CCMapHintField"])
    new_level.add_field(map_hint_field)

    monster_movement_field = cc_classes.CCMonsterMovementField(optional_fields_data["CCMonsterMovementField"])
    #new_level.add_field(monster_movement_field)

    # print(new_level)
    new_level_pack.levels.append(new_level)

# print(new_level_pack)


#Convert JSON data to CCLevelPack

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/kcl2_cc1.dat")
