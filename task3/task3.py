import json

def build_structure(data, values, d=[]):
    for test in data:
        for i in values:
            if i.get('id', 'No id') == test['id']:
                value = i.get('value', 'No value')
                break
            else:
                value = None
        if value:
            if 'values' in test:
                new_list = []
                d.append({'id': test['id'], 'title': test['title'], 'value': value, 'values': build_structure(test['values'], values, new_list)})
            else:
                d.append({'id': test['id'], 'title': test['title'], 'value': value})
        else:
            if 'values' in test:
                new_list = []
                d.append({'id': test['id'], 'title': test['title'], 'values': build_structure(test['values'], values, new_list)})
            else:
                d.append({'id': test['id'], 'title': test['title']})
    return d

def main():
    values_file = input()
    tests_file = input()
    report_file = input()
    with open(values_file, "r") as values_json:
        values = json.loads(values_json.read())
    with open(tests_file, "r") as tests_json:
        tests = json.loads(tests_json.read())
    to_report = {'tests': build_structure(tests['tests'], values['values'])}
    with open(report_file, "w") as report_json:
        json.dump(to_report, report_json)

if __name__ == "__main__":
    main()