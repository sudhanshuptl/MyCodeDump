from pprint import pprint


def create_link_list(inp: list):
    # map representation of nodes and -> the next node
    link_list_map = dict()
    for pair in inp:
        # skip empty rows
        if not pair:
            continue
        # split pair into key and value representing link [key -> val]
        key, val = pair.split(",")
        link_list_map[key] = val

    return link_list_map


# a -> b -> c
# a:a, b:a, c:
def check_if_intersection(link_list_map: dict, start_nodes: list):
    parent_list_map = dict()

    # Handling special case if input has multiple point with same value
    # this case should always be True
    input_set = set(start_nodes)
    if len(input_set)< len(start_nodes):
        return True

    # Create a hash of node and its origin point(it will be same as start point given in start_nodes)
    # if encountered a situation where for single node there is 2 origin point we can consider them as intersection
    for node in start_nodes:
        start_node = node
        while True:
            if node not in parent_list_map:
                parent_list_map[node] = start_node

            # circular list found
            elif parent_list_map[node] == start_node:
                break

            # intersection found as two nodes with different parents found
            elif parent_list_map[node] != start_node:
                return True

            # break if no next node available
            if node not in link_list_map:
                break
            else:
                node = link_list_map[node]
    return False


def main():
    inp = """a,b
b,c
c,a
"""
#     inp = """a,b
# r,s
# b,c
# x,c
# q,r
# y,x
# w,z
# """
#     inp = """a,b
# b,c
# x,b
# p,x
# c,p
# q,p
# """

    link_list_map = create_link_list(inp.split("\n"))
    pprint(link_list_map)
    while True:
        inp = input("input -> ", )
        print(check_if_intersection(link_list_map, inp.split(",")))


if __name__ == '__main__':
    main()