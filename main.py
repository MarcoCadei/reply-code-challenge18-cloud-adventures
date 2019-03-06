import sys
import numpy as np


def read(file_name):
    file = open(file_name, "r")
    V, S, C, P = (int(x) for x in file.readline().split())
    services = file.readline().split()
    countries = file.readline().split()

    providers = []
    for i in range(V):
        provider_name, number_regions = file.readline().split()
        number_regions = int(number_regions)

        providers.append((provider_name, number_regions, []))
        for _ in range(number_regions):
            region_name = file.readline().split()
            t = file.readline().split()
            number_packages = int(t[0])
            package_cost = float(t[1])
            package_services = [int(x) for x in t[2:]]
            region_latencies = [int(x) for x in file.readline().split()]

            providers[i][2].append((region_name, [number_packages], package_cost, package_services, region_latencies))

    projects = []
    for i in range(P):
        t = file.readline().split()
        penalty = int(t[0])
        country = t[1]
        units_needed = [int(x) for x in t[2:]]

        projects.append((penalty, country, units_needed))

    return V, S, C, P, services, countries, providers, projects


def write(file_name, solution):
    file = open(file_name, "w")
    string_solution = []
    for project in solution:
        string_solution.append(" ".join((str(x) for x in project)))
    file.write("\n".join(string_solution))


def main():
    file_name = sys.argv[1]
    V, S, C, P, services, countries, providers, projects = read(file_name)

    thresh = 0.000005
    max_resources = [0] * S
    for i in range(S):
        for j in range(V):
            for k in range(providers[j][1]):
                max_resources[i] += providers[j][2][k][3][i] * providers[j][2][k][1][0]

    regions = []
    for i in range(V):
        for j in range(providers[i][1]):
            t1, t2, t3, t4, t5 = providers[i][2][j]
            regions.append((t1, t2, t3, t4, t5, i))

    solution = []
    for _ in range(P):
        solution.append([])
    counter = 1
    for project in sorted(projects, key=lambda z: z[0], reverse=True):
        project_index = projects.index(project)
        country_index = countries.index(project[1])
        print(counter)
        counter += 1
        for region in sorted(regions, key=lambda y: y[4][country_index]):
            region_index = regions.index(region)
            output_region_index = providers[region[5]][2].index(region[:-1])

            if regions[region_index][1][0] <= 0:
                continue

            i = 1
            x = np.array(1)
            while i < regions[region_index][1][0] + 1 and np.any(x > 0):
                x = np.array(projects[project_index][2]) - i * np.array(regions[region_index][3])
                i += 1
                if np.mean((i * np.array(regions[region_index][3])) / np.array(max_resources).astype(float)) > thresh:
                    break
            i -= 1

            t = projects[project_index][2][:]
            projects[project_index][2].clear()
            t2 = (np.array(t) - i * np.array(regions[region_index][3])).tolist()
            projects[project_index][2].extend(t2)
            regions[region_index][1][0] -= i

            # Update solution
            solution[project_index].extend([regions[region_index][5], output_region_index, i])
            # print(project_index)
            finish = all(v <= 0 for v in projects[project_index][2])
            if finish:
                break

    write(sys.argv[1].split(".")[0]+".out", solution)


if __name__ == "__main__":
        main()
