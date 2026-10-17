"""Probability calculations for shot-event analysis."""
import argparse
import json
import math
from pathlib import Path

def probability(events, total):
    if type(events) is not int or type(total) is not int or total <= 0 or not 0 <= events <= total:
        raise ValueError('Require integer counts 0 <= events <= total, total > 0')
    return events / total

def binomial_probability(successes, trials, p):
    if type(successes) is not int or type(trials) is not int or not 0 <= successes <= trials:
        raise ValueError('Require integer counts 0 <= successes <= trials')
    if not isinstance(p,(int,float)) or not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError('p must be finite and between zero and one')
    return math.comb(trials,successes)*p**successes*(1-p)**(trials-successes)

def expected_points(made, attempts, point_value):
    if point_value not in (2,3):raise ValueError('point_value must be 2 or 3')
    return point_value*probability(made,attempts)

def summarize(record):
    result={'make_probability':probability(record['made'],record['n'])}
    for kind in ('2','3'):
        row=record[kind]
        result[f'{kind}_point_make_probability']=probability(row['made'],row['attempts'])
        result[f'{kind}_point_expected_points']=expected_points(row['made'],row['attempts'],int(kind))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('counts',type=Path,nargs='?',default=Path(__file__).with_name('results')/'aggregate_counts.json')
    args=parser.parse_args();print(json.dumps(summarize(json.loads(args.counts.read_text())),indent=2))
