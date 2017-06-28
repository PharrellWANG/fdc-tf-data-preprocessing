# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
import datetime
import glob

files = [f for f in glob.glob('/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/'
                              '4_3738_to_3536_32x32/3536_all_data_32_*.csv')]
outfile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/' \
          '5_concatenating_all_32x32/32x32_merged.csv'.format(datetime.datetime.now())

with open(outfile, 'w') as w:
    for input_file in files:
        with open(input_file, 'r') as r:
            # cnt = 0
            for num, line in enumerate(r):
                # cnt += 1
                w.write(line)