import json
import csv

def convert(inputfile, outputfile):
    with open(inputfile, 'r') as json_file:
        json_object = json.load(json_file)
    header = ['id', 'question','title', 'context']
    with open(outputfile, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range (len(json_object['data'])):
            for j in range(len(json_object['data'][i]['paragraphs'])):
                # print(len(json_object['data'][i]['paragraphs'][j]['qas']))
                for k in range(len(json_object['data'][i]['paragraphs'][j]['qas'])):
                    row = []
                    row.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['id'])
                    row.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['question'])
                    row.append(json_object['data'][i]['title'])
                    row.append(json_object['data'][i]['paragraphs'][j]['context'])
                    if (len(row) != 0):
                        writer.writerow(row)

convert('dev-v1.1.json', 'eval.csv')
convert('train-v1.1.json', 'train.csv')




