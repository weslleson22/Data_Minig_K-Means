import numpy as np
import os
import matplotlib.pyplot as plt

def compute_euclidean_distance(ponto, centroide):
    return np.sqrt(np.sum((ponto - centroide)**2))

def assign_label_cluster(distance, data_ponto, centroides):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_ponto, centroides[index_of_minimum]]

def compute_new_centroides(cluster_label, centroides):
    return np.array(cluster_label + centroides)/2

def iterate_k_means(data_pontos, centroides, total_interacao):
    label = []
    cluster_label = []
    total_pontos = len(data_pontos)
    k = len(centroides)
    
    for interacao in range(0, total_interacao):
        for index_ponto in range(0, total_pontos):
            distance = {}
            for index_centroide in range(0, k):
                distance[index_centroide] = compute_euclidean_distance(data_pontos[index_ponto], centroides[index_centroide])
            label = assign_label_cluster(distance, data_pontos[index_ponto], centroides)
            centroides[label[0]] = compute_new_centroides(label[1], centroides[label[0]])

            if interacao == (total_interacao - 1):
                cluster_label.append(label)

    return [cluster_label, centroides]

def print_label_data(result):
    print("Result of k-Means: \n")
    for data in result[0]:
        print("data ponto: {}".format(data[1]))
        print("number: {} \n".format(data[0]))
    print("Posicão dos centroides: \n {}".format(result[1]))
    fig,ax = plt.subplots()

    

    

def create_centroides():
    centroides = []
    centroides.append([135.000, 0.0])
    
    return np.array(centroides)

if __name__ == "__main__":
    filename = os.path.dirname(__file__) + "\data.csv"
    data_pontos = np.genfromtxt(filename, delimiter=",")
    centroides = create_centroides()
    total_interacao = 100
    
    [cluster_label, new_centroides] = iterate_k_means(data_pontos, centroides, total_interacao)
    print_label_data([cluster_label, new_centroides])
    print()
    
    fig,ax = plt.subplots()

    #ax.plot(data_pontos)
    #ax.plot(centroides)
    #plt.plot(data_pontos, color='green')
    #plt.scatter(data_pontos,centroides, color='red')
    #plt.plot(data_pontos,'o')
    #plt.plot(centroides,'x')
    plt.title('Algoritmo K-Means')
    plt.plot(data_pontos,'o')
    plt.ylabel('Total de Custo')
    plt.xlabel('Nº de Clientes')

    
    plt.show()
