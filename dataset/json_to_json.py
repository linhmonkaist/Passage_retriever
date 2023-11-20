import json
import pandas as pd

def convert(inputfile, outputfile):
    json_data = {}
    with open(inputfile, 'r') as json_file:
        json_object = json.load(json_file)
    header = ['ques_id', 'question', 'text_id','title', 'context']
    ques_id = []
    question = []
    title = []
    context = []
    for i in range (len(json_object['data'])):
        for j in range(len(json_object['data'][i]['paragraphs'])):
            # print(len(json_object['data'][i]['paragraphs'][j]['qas']))
            for k in range(len(json_object['data'][i]['paragraphs'][j]['qas'])):
                ques_id.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['id'])
                question.append(json_object['data'][i]['paragraphs'][j]['qas'][k]['question'])
                title.append(json_object['data'][i]['title'])
                context.append(json_object['data'][i]['paragraphs'][j]['context'])
    json_data['ques_id'] = ques_id
    json_data['question'] = question
    json_data['title'] = title
    json_data['context'] = context

    with open(outputfile, 'w', encoding="utf-8") as file:
        file.write(json.dumps(json_data , indent=4))

def get_passge(inputfile, outputfile):
    json_data = {}
    with open(inputfile, 'r') as json_file:
        json_object = json.load(json_file)
    title = []
    context = []
    for i in range (len(json_object['data'])):
        for j in range(len(json_object['data'][i]['paragraphs'])):
            title.append(json_object['data'][i]['title'])
            context.append(json_object['data'][i]['paragraphs'][j]['context'])
    json_data['title'] = title
    json_data['context'] = context

    with open(outputfile, 'w', encoding="utf-8") as file:
        file.write(json.dumps(json_data , indent=4))

# convert('D:\Github\AI\dataset\dev-v1.1.json' , 'eval.json')
# convert('D:\Github\AI\dataset\\train-v1.1.json' , 'train.json')

get_passge('D:\Github\AI\dataset\dev-v1.1.json', 'eval_passages.json')
get_passge('D:\Github\AI\dataset\\train-v1.1.json', 'train_passages.json')


