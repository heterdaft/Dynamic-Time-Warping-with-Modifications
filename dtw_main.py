import dtw
import csv
import codecs
from point2d import Point2D

def main():
    points = {"a":[], "b":[], "c":[], "d":[], "e":[]}
    time = [] # init list of time steps
    with open("dynamic_time_warping_test_data.csv", 'r') as csvfile:
        reader = csv.DictReader(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig'))
        for row in reader:
            time += [float(row["Time"])]
            for key, value in points.items():
                value.append(Point2D(float(row[key+"_x"]), float(row[key+"_y"])))

    with open("dynamic_time_warping_test_output.csv", 'w') as csvfile:
        fieldnames = ["/"] + points.keys()
        writer = csv.DictWriter(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig')
                                , fieldnames=fieldnames)
        writer.writeheader()
        for row_name, value in points.items(): # current row of matrix
            row = {"/":row_name}
            row.update( {col_name:dtw.distance(value, value2)
                    for col_name, value2 in points.items()} ) # Current col of matrix
            writer.writerow(row)

    with open("dynamic_time_warping_test_time_output.csv", 'w') as csvfile:
        fieldnames = ["/"] + points.keys()
        writer = csv.DictWriter(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig')
                                , fieldnames=fieldnames)
        writer.writeheader()
        for row_name, value in points.items(): # current row of matrix
            row = {"/":row_name}
            row.update( {col_name:dtw.time_percentage(value, time, value2, time)
                    for col_name, value2 in points.items()} ) # Current col of matrix
            writer.writerow(row)

    with open("dynamic_time_warping_basic_function_output.csv", 'w') as csvfile:
        fieldnames = ["/"] + points.keys()
        writer = csv.DictWriter(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig')
                                , fieldnames=fieldnames)
        writer.writeheader()
        for row_name, value in points.items(): # current row of matrix
            row = {"/":row_name}
            row.update( {col_name:dtw.basic_function(value, value2, time)
                    for col_name, value2 in points.items()} ) # Current col of matrix
            writer.writerow(row)

if __name__ == "__main__":
    main()
