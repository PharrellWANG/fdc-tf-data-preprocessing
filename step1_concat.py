# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
size_64_files = ['/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_Balloon_Encoder/mixed_data_0.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_GT_Fly_Encoder/mixed_data_0.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_newspaper_Encoder/mixed_data_0.csv'
                 ]

size_32_files = ['/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_Balloon_Encoder/mixed_data_1.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_GT_Fly_Encoder/mixed_data_1.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_newspaper_Encoder/mixed_data_1.csv'
                 ]

size_16_files = ['/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_Balloon_Encoder/mixed_data_2.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_GT_Fly_Encoder/mixed_data_2.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_newspaper_Encoder/mixed_data_2.csv'
                 ]

size_08_files = ['/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_Balloon_Encoder/mixed_data_3.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_GT_Fly_Encoder/mixed_data_3.csv',
                 '/Users/Pharrell_WANG/data/Data-Collected-from-HTM-all-intra/data_exported--HTM_v16.2_newspaper_Encoder/mixed_data_3.csv'
                 ]

INPUT_FILE = size_16_files
OUTPUT_FILE = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/data_after_step1_concat/merged_from_three_sequences_size_16.csv'


with open(OUTPUT_FILE, 'w') as w:
    for input_file in INPUT_FILE:
        with open(input_file, 'r') as r:
            # cnt = 0
            for num, line in enumerate(r):
                # cnt += 1
                w.write(line)
