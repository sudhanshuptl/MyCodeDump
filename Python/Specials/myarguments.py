import argparse, sys


def handle_commandline():
    """
    sets up the valid command line arguments .
    :return:tuple: with first value is action and second values as dict of parameters
    """
    parser = _add_commandline_arguments()
    opts, args = parser.parse_known_args(sys.argv[1:])
    opts = vars(opts)
    action = opts.pop('action')
    return action, opts

def _add_commandline_arguments():
    """
    sets up the cmd line arguments
    returns:parser object
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-action', action='store', choices=['apply', 'destroy', 'plan'], type=str,
                        help='Action : apply or destroy cluster', required=True)

    parser.add_argument('-team', action='store', help='team name ', type=str, required=True)


    parser.add_argument('-desired_capacity', action='store',
                        help='Desired capacity', type=int)

    return parser
if __name__ == '__main__':
    print(handle_commandline())
# python3 myarguments.py -action apply -team  daredevil
