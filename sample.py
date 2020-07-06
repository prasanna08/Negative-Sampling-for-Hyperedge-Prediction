import negative_sampler as ns
import argparse

def read_in_file(fname):
    hyperedges = set()
    with open(fname, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            try:
                hyperedges.add(frozenset(map(lambda x: int(x), line.split(','))))
            except ValueError:
                print("Nodes in the hyperedges must be integer values.")
                return None
    return hyperedges

def write_to_file(fname, data):
    with open(fname, 'w') as f:
        for hedge in data:
            f.write(', '.join(str(node) for node in hedge))
            f.write('\n')
    return

def main(args):
    hyperedges = read_in_file(args.hyperedges)
    if not hyperedges:
        return
    neg_hyperedges = ns.generate_negative_samples_for_hyperedges(
        hyperedges, args.ns_algo, args.ns_ratio * len(hyperedges))
    write_to_file(args.output, neg_hyperedges)
    print("Negative Hyperedges written to %s file" % args.output)

parser = argparse.ArgumentParser()
parser.add_argument(
    '--hyperedges', type=str, default='example.csv',
    help='Name of the file containing hyperedges.'
    'Take a look at example.csv for more information on format of the file.')
parser.add_argument(
    '--ns-algo', type=str, default='MNS',
    help='Negative Sampling algorithm. Available algorithms are UNS, SNS, MNS, CNS.')
parser.add_argument(
    '--ns-ratio', type=int, default=5,
    help='Ratio of negative hyperedges to positive hyperedges for sampling.')
parser.add_argument(
    '--output', type=str, default='example_negative.csv',
    help='Name of the output file to store negative edges. The format is same as input file.')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
