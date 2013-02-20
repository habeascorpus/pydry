import argparse
from collections import Counter, defaultdict

import corpus

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--traindata', help='training data file', required=True)
    args = parser.parse_args()

    with open(args.traindata) as f:
        data = corpus.read(f)

    class_counts = defaultdict(lambda: Counter())
    for doc in data:
        for class_name, method_name in doc:
            class_counts[class_name][method_name] += 1

    print '{} classes'.format(len(class_counts))
    for class_name, counts in class_counts.iteritems():
        print class_name
        print counts.most_common(n=10)
        print

if __name__ == '__main__':
    main()
