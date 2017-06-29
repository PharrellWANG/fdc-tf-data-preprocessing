import pandas
import tensorflow as tf

# FILE_TO_BE_CONVERTED = "/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/train_data/training_data_16x16.csv"
FILE_TO_BE_CONVERTED = "/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_data_16x16.csv"

# TFRecord_OUTPUT = "/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/TFRecords/16x16/16x16_train.tfrecord"
TFRecord_OUTPUT = "/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/TFRecords/16x16/16x16_validation.tfrecord"

csv = pandas.read_csv(FILE_TO_BE_CONVERTED).values
with tf.python_io.TFRecordWriter(TFRecord_OUTPUT) as writer:
    for row in csv:
        features, label = row[:-1], row[-1]
        example = tf.train.Example()
        example.features.feature["features"].float_list.value.extend(features)
        example.features.feature["label"].int64_list.value.append(label)
        writer.write(example.SerializeToString())
