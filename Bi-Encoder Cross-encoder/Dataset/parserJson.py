import json
import csv

def convert(inputfile, outputfile):
    with open(inputfile, 'r') as json_file:
        json_object = json.load(json_file)
    header = ['ques_id', 'question', 'text_id','title', 'context']
    with open(outputfile, 'w', encoding="utf-8", newline='') as file:
        # print(len(json_object['data']))
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range (len(json_object['data'])):
            for j in range(len(json_object['data'][i]['paragraphs'])):
                # print(len(json_object['data'][i]['paragraphs'][j]['qas']))
                for k in range(len(json_object['data'][i]['paragraphs'][j]['qas'])):
                    row = []
                    row.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['id'])
                    row.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['question'])
                    row.append(str(i) + '_' + str(j))
                    row.append(json_object['data'][i]['title'])
                    row.append(json_object['data'][i]['paragraphs'][j]['context'])
                    if (len(row) != 0):
                        writer.writerow(row)

def get_passage_only(inputfile, outputfile):
    with open(inputfile, 'r') as json_file:
        json_object = json.load(json_file)
    header = ['text_id','title', 'context']
    with open(outputfile, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range (len(json_object['data'])):
            for j in range(len(json_object['data'][i]['paragraphs'])):
                # print(len(json_object['data'][i]['paragraphs'][j]['qas']))
                row = []
                row.append(str(i) + '_' + str(j))
                row.append(json_object['data'][i]['title'])
                row.append(json_object['data'][i]['paragraphs'][j]['context'])
                if (len(row) != 0):
                    writer.writerow(row)
    print(len(json_object['data']) * len(json_object['data'][i]['paragraphs']))

# convert('dev-v1.1.json', 'eval_with_id.csv')
# convert('train-v1.1.json', 'train_with_id.csv')
get_passage_only('D:\Github\AI\dataset\dev-v1.1.json', 'eval_passage.csv')
get_passage_only('D:\Github\AI\dataset\train-v1.1.json', 'train_passage.csv')



