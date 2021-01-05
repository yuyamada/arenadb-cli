import sys
import argparse
import requests
import json
from alias import alias


def run(args):
    url = 'https://nomae.net/princess_connect/public/_arenadb/receive.php'
    headers = {'x-from': 'https://nomae.net/arenadb/'}
    def_party = [alias.get(c, c) for c in args.def_party]
    data = [
        ('type', 'search'),
        ('userid', 0),
        ('public', 1),
        *[('def[]', c) for c in def_party],
        ('page', 0),
        ('sort', 0),
    ]
    try:
        res = requests.post(url, headers=headers, data=data)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        # TODO: request again
        print(f'error: {e}')
        sys.exit(1)

    rows = json.loads(res.text)
    # TODO: chache the response

    for r in rows:
        r['atk_party'] = [c.split(',')[0] for c in r['atk'].split('/')[1:]]

    print('def_party:', def_party)
    show_cols = ['updated', 'good', 'bad', 'atk_party']
    print('\t'.join(show_cols))
    for r in rows:
        print('\t'.join([str(r[c]) for c in show_cols]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('def_party', nargs='*',
                        help='defence characters separated by space')
    # parser.add_argument('-e', '--exclude', nargs='*', default=[],
    #                    help='exclude characters separated by space')
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
