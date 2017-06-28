# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------


def comma_remover(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE, 'r') as r, \
            open(OUTPUT_FILE, 'w') as w:
        cnt = 0
        for num, line in enumerate(r):
            cnt += 1
            if num >= 0:
                newline = line[:-2] + "\n" if "\n" in line else line[:-1]
            else:
                newline = line
            w.write(newline)

        print("total lines of " + INPUT_FILE + str(" :      ") + str(cnt))


list_of_input_files = [
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_balloon.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_gt_fly.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_kendo.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_newspaper.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_poznan_hall2.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_poznan_street.csv',
                       # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_shark.csv',
                       '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/1_raw_data_32x32/z_training_data_32_undo_dancer.csv'
                        ]
list_of_output_files = [
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_balloon.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_gt_fly.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_kendo.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_newspaper.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_poznan_hall2.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_poznan_street.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_shark.csv',
                        '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_undo_dancer.csv'
                        ]

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x], list_of_output_files[x])
