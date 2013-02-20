def read(stream):
    corpus = []
    cur_calls = []
    for line in (l.strip() for l in stream):
        if not line:
            if cur_calls: corpus.append(cur_calls)
            cur_calls = []
        else:
            class_name, expression = line.split('\t')
            class_name = class_name.split('<')[0]
            method_name = expression.partition('(')[0].split('.')[-1]
            cur_calls.append( (class_name, method_name) )
    return corpus
