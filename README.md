## Negative Sampling code for Hyperedge Prediction.

This repository implements negative sampling code for hyperedge prediction as defined in following paper:
```
Negative sampling for hyperlink prediction in networks. 
Prasanna Patil, Govind Sharma, and M Narasimha Murty.
Pacific-Asia Conference on Knowledge Discovery and Data Mining
doi: 10.1007/978-3-030-47436-2-46.
```

### Dependencies
* Python 3.7
* numpy
* tqdm

#### Install dependencies
Install neccessary requirements through `requirements.txt`
```
pip install -r requirements.txt
```

### Usage
Run sample.py with following arguments:
```
sample.py [-h] [--hyperedges HYPEREDGES] [--ns-algo NS_ALGO]
                 [--ns-ratio NS_RATIO] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --hyperedges HYPEREDGES
                        Name of the file containing hyperedges.Take a look at
                        example.csv for more information on format of the
                        file.
  --ns-algo NS_ALGO     Negative Sampling algorithm. Available algorithms are
                        UNS, SNS, MNS, CNS.
  --ns-ratio NS_RATIO   Ratio of negative hyperedges to positive hyperedges
                        for sampling.
  --output OUTPUT       Name of the output file to store negative edges. The
                        format is same as input file.
```

If you find this code helpful in your research, please cite our publication:
```
@inproceedings{patil2020negative,
  title={Negative Sampling for Hyperlink Prediction in Networks},
  author={Patil, Prasanna and Sharma, Govind and Murty, M Narasimha},
  booktitle={Pacific-Asia Conference on Knowledge Discovery and Data Mining},
  pages={607--619},
  year={2020},
  doi={10.1007/978-3-030-47436-2_46},
  organization={Springer}
}
```
