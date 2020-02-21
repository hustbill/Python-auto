import json

histogram_bucket_index = [
    1000, 2000, 3000, 4000, 5000, 6000, 10000, 20000, 30000, 60000,
    5 * 60 * 1000, 10 * 60 * 1000, 20 * 60 * 1000, 30 * 60 * 1000,
    45 * 60 * 1000, 60 * 60 * 1000, 1000000 * 60 * 1000
]
histogram_bucket_name = {
    0: '1s',
    1: '2s',
    2: '3s',
    3: '4s',
    4: '5s',
    5: '6s',
    6: '10s',
    7: '20s',
    8: '30s',
    9: '1m',
    10: '5m',
    11: '10m',
    12: '20m',
    13: '30m',
    14: '45m',
    15: '1h',
    16: '100000h'
}


def get_bucket_index(value_param):
    for i, v in enumerate(histogram_bucket_index):
        if long(value) <= histogram_bucket_index[i]:
            return i


def get_bucket_v2(value):
    index = get_bucket_index(value)
    return histogram_bucket_name[index]


def print_histogram(histogram):
    for k in sorted(histogram):
        label = "> 1h" if k == "100000h" else '<= ' + k
        print label + ", " + str(histogram[k])


def print_histogram_perc(histogram):
    for k in sorted(histogram):
        print "DC = " + k
        dc_histogram = histogram[k]
        total = sum(dc_histogram.values())
        print "total is " + str(total)
        for v in histogram[k]:
            label = "> 1h" if v == "100000h" else '<= ' + v
            print label + ", " + str(
                (histogram[k][v] * 1.0 / total)) + ", " + str(histogram[k][v])


with open('streams_out.json') as json_file:
    data = json.load(json_file)

    histogram = {}
    for metric_entry in data:
        tags = metric_entry['tags']
        dps = metric_entry['dps']

        dc = tags['dc'] + ""

        if dc not in histogram.keys():
            histogram[dc] = {}
        for key, value in dps.items():
            bucket = get_bucket_v2(value)
            if bucket in histogram[dc].keys():
                histogram[dc][bucket] = histogram[dc][bucket] + 1
            else:
                histogram[dc][bucket] = 1

    print_histogram_perc(histogram)
