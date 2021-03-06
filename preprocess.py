from preprocess.parse_mat import ParseMAt
from preprocess.parse_los_mat import LOSParseMAt
from config import *
import argparse


# parse all los and nlos data
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatData_6F_ALL_Path,
    save_path=PAESED_FILES_6F_ALL
)
parse_mat_to_np.generate_data_all()
#
#
# parse NLOS data, with old board
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatData_6F_NLOS_Path,
    save_path=PAESED_FILES_6F_NLOS
)
parse_mat_to_np.generate_data_all()
#
# parse new los data
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatDataLOS6F_NEW_Path,
    save_path=LOS_PAESED_FILES_NEW
)
parse_mat_to_np.generate_data_all()

# # parse old los data
# parse_mat_to_np = ParseMAt(
#     overwrite=False,
#     input_path=MatDataLOS6F_OLD_Path,
#     save_path=LOS_PAESED_FILES_OLD
# )
# parse_mat_to_np.generate_data_all()


###############################
# generate index file for little labeled data experiment
# parse all los and nlos data
data_percent = [0.1, 0.1, 0]
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatData_LOSNEW_NLOSOLD,
    save_path=PARSED_FILES_LOSNEW_NLOSOLD,
    manual_split_data=True,
    data_percent=data_percent,
    save_npy=False
)
parse_mat_to_np.generate_data_all()
# parse nlos data
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatData_6F_NLOS_Path,
    save_path=PAESED_FILES_6F_NLOS,
    manual_split_data=True,
    data_percent=data_percent,
    save_npy=False
)
# parse_mat_to_np.generate_data_all()
# parse los data
parse_mat_to_np = ParseMAt(
    overwrite=False,
    input_path=MatDataLOS6F_NEW_Path,
    save_path=LOS_PAESED_FILES_NEW,
    manual_split_data=True,
    data_percent=data_percent,
    save_npy=False
)
# parse_mat_to_np.generate_data_all()


####################
# from preprocess.parse_unlabeled_mat import ParseUnlabeledMAt
# parse_mat_to_np = ParseUnlabeledMAt(
#     overwrite=False,
#     input_path=UNLABELED_MATDATA_PATH,
#     save_path=UNLABELED_PARSED
# )
# parse_mat_to_np.generate_data_all()


# # parse new los data old nlos data
# parse_mat_to_np = ParseMAt(
#     overwrite=False,
#     input_path=MatData_LOSNEW_NLOSOLD,
#     save_path=PARSED_FILES_LOSNEW_NLOSOLD
# )
# parse_mat_to_np.generate_data_all()


# parse_mat_to_np = LOSParseMAt(
#     overwrite=False
# )
# parse_mat_to_np.generate_data_all()
