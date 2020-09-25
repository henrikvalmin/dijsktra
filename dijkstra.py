import pandas as pd
from node import node


class dijsktra:

    def dijsktra_solve(initial_nodes, node):
        """Uses the Dijkstra algorithm to find the least
        cost path from node to every other node in the network."""

        nodes = initial_nodes.copy()
        Nprime = [node]
        nodes.remove(node)

        # Set up
        data = {}
        data["N'"] = [node.name]
        for n in nodes:
            if (n == node):
                pass
            if (node.name in list(n.neighbors.keys())):
                data[n.name] = [(n.neighbors[node.name], node.name)]
            else:
                data[n.name] = 'inf'


        table = pd.DataFrame(data)


        # Loop step - find w with smallest D(w)
        loop_num = len(nodes)
        for i in range(loop_num):

            # Fetch the last row as a dicitonary and find it's smallest value
            new_row = table.iloc[i].to_dict().copy()

            smallest_cost_key = None
            for key in new_row:
                if type(new_row[key]) is tuple and smallest_cost_key is None:
                    smallest_cost_key = key
                elif type(new_row[key]) is tuple and new_row[smallest_cost_key][0] > new_row[key][0]:
                    smallest_cost_key = key
            cost_to_latest_added = new_row[smallest_cost_key][0]

            new_row[smallest_cost_key] = ['Done!']
            new_row["N'"] += smallest_cost_key

            for n in nodes:
                if n.name == smallest_cost_key:
                    Nprime.append(n)

            nodes = [n for n in nodes if n.name != smallest_cost_key]

            # Update distance for each neighbor of w not in Nprime
            latest_added_neighbor_keys = list(Nprime[-1].neighbors.keys())

            for node in nodes:
                # Handle previously unknown values
                if node.name in latest_added_neighbor_keys and new_row[node.name] == 'inf':
                    new_row[node.name] = (cost_to_latest_added + Nprime[-1].neighbors[node.name], Nprime[-1].name)

                # Check if cheaper path found
                elif node.name in latest_added_neighbor_keys and type(new_row[node.name]) is tuple:
                    new_path_cost = cost_to_latest_added + Nprime[-1].neighbors[node.name]
                    if new_row[node.name][0] > new_path_cost:
                        new_row[node.name] = (new_path_cost, Nprime[-1].name)

            # Must wrap every item in a list if it isn't already,
            # to make the conversion work
            for key in list(new_row.keys()):
                if type(new_row[key]) is not list:
                    new_row[key] = [new_row[key]]

            table = pd.concat([table, pd.DataFrame.from_dict(new_row)], ignore_index=True)

        # Loop exited, print results with updated headers (on the form D(v), p(v))
        for key in list(new_row.keys()):
            if key != "N'":
                table.rename({key: "D({}), p({})".format(key, key)}, axis=1, inplace=True)

        return table
