"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from probability import probability, expected_points, binomial_probability
result = {'three_point_make_probability': probability(329, 786), 'two_point_expected_points': expected_points(374, 648, 2), 'exactly_two_of_four': binomial_probability(2, 4, .5)}

import json
print(json.dumps(result, indent=2))

