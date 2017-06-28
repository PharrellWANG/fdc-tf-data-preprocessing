# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
from csv_mode_counter import csv_mode_preprocessing

# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/33_angular_modes_only_from_testing_32x32_texture_only.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_only_from_training_32x32_texture_only.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_train_0-32.csv'

# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/training_32x32_depth_only.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32_depth_only.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32_depth_only_MODE36_and_OTHERS.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/training_32x32_depth_only_two_classes_MODE36_and_OTHERS.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/four_classes_from_texture_angular_test.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/four_classes_from_texture_angular_train.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/two_classes_from_texture_angular_train.csv'
ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/z_training_data_32.csv'
x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG_DATA)