# Класс, реализующий граф и некоторые операции с ним.
class Graph:
    # Конструктор класса.
    def __init__(self, m, n):
        self.vert_vertex = m  # Количество вершин графа по вертикали.
        self.hor_vertex = n  # Количество вершин графа по горизонтали.
        self.vertexes = self.hor_vertex * self.vert_vertex  # Общее количество вершин графа.
        # Установка списка смежных вершин.
        self.adj_list = list()
        for i in range(self.vertexes):
            self.adj_list.append([])
        # Установка матрицы смежности.
        self.adj_mat = [[-1] * self.vertexes for _ in range(self.vertexes)]
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat)):
                if i == j:
                    self.adj_mat[i][j] = 0

    # Процедура вставки взвешенного ребра в граф.
    def connect(self, node1, node2, weight):
        self.adj_list[node1].append([node2, weight])  # Вставка ребра в список смежных вершин.
        self.adj_mat[node1][node2] = weight  # Вставка ребра в матрицу смежности для алгоритма перебора вершин.

    # Модифицированный алгоритм Дейкстры.
    def modified_dijkstra(self, node):
        nodes_to_visit = list()  # Инициализация списка вершин для посещения.
        nodes_to_visit.append((0, node))  # Добавление стартовой вершины в список как первой вершины для посещения.
        visited = set()  # Множество для хранения посещённых вершин.
        max_dist = {i: -1 for i in range(len(self.adj_list))}  # Заполнение расстояний до вершин.
        max_dist[node] = 0  # Заполнение расстояния до стартовой вершины.
        while len(nodes_to_visit):  # Пока nodes_to_visit не пустой:
            weight, current_node = max(nodes_to_visit)  # Выбор дальней вершины.
            nodes_to_visit.remove((weight, current_node))  # Удаление этой вершины из списка вершин для посещения.
            if current_node in visited:  # Если выбранная вершина уже посещена:
                continue  # Запуск следующего прохода цикла без выполнения оставшегося тела цикла.
            visited.add(current_node)  # Добавление выбранной вершины в список посещённых.
            # next_weight - вес из текущей вершины, next_node - прикреплённая вершина, в которую необходимо попасть.
            for next_node, next_weight in self.adj_list[current_node]:  # Проход по всем соединённым вершинам.
                if weight + next_weight > max_dist[next_node] and next_node not in visited:
                    max_dist[next_node] = weight + next_weight  # Обновление расстояния.
                    nodes_to_visit.append((weight + next_weight, next_node))  # Добавление в список для посещения.
        return max_dist  # Возврат множества из словарей {номер_узла: кратчайший путь до него от заданного узла}.

    # Функция величины самого длинного пути, модифицированным методом "Дейкстры".
    def longest_path_dijkstra(self, node1, node2):  # Для заданного узла node1 и другого заданного узла node2:
        return self.modified_dijkstra(node1)[node2]  # Возврат величины самого длинного пути между node1 и node2.

    # Функция восстановления самого длинного пути между двумя заданными вершинами, модифицированным методом "Дейкстры".
    def path_restoring_modified_dijkstra(self, node1, node2):
        visited = list()
        for i in range(len(self.adj_mat)):
            visited.append((None, None))
        # Начальный элемент - конечная вершина. Добавление в список номера элемента матрицы.
        visited[0] = (node2 // self.hor_vertex + 1, node2 % self.hor_vertex + 1)
        pre = 1  # Индекс предыдущей вершины.
        weight = self.longest_path_dijkstra(node1, node2)  # Вес пути до конечной вершины.
        while node2 != node1:  # Пока не дошли до начальной вершины:
            for i in range(len(self.adj_mat)):  # Проход по всем вершинам.
                if self.adj_mat[i][node2] > 0:  # При наличии связи:
                    temp = weight - self.adj_mat[i][node2]  # Определение веса пути из предыдущей вершины.
                    # Если вес совпал с рассчитанным, то из этой вершины был переход.
                    if temp == self.longest_path_dijkstra(node1, i):
                        weight = temp
                        node2 = i
                        visited[pre] = (i // self.hor_vertex + 1, i % self.hor_vertex + 1)
                        pre += 1
        while (None, None) in visited:
            visited.remove((None, None))
        return visited[::-1]

    # Приложение для нахождения самого длинного пути.
    def app_longest_path(self, matrix_elements):  # Для заданного списка элементов матрицы:
        for node in range(self.vertexes):  # Для каждой вершины:
            if node < self.vertexes - self.hor_vertex:  # Если вершина не на нижней границе поля:
                # Соединение текущей вершины с соседней снизу.
                self.connect(node, node + self.hor_vertex, matrix_elements[node + self.hor_vertex])
                if (node + 1) % self.hor_vertex != 0 or node == 0:  # Если вершина не на правой границе поля:
                    # Соединение текущей вершины с соседней справа.
                    self.connect(node, node + 1, matrix_elements[node + 1])
            elif node < self.vertexes - 1:  # Иначе, если вершина не последняя (но на нижней границе поля):
                # Соединение текущей вершины с соседней справа.
                self.connect(node, node + 1, matrix_elements[node + 1])
        '''
        # Вывод графа в виде списка смежных вершин.
        for row in self.adj_list:  # Для каждой строки в списке смежных вершин:
            print(row)  # Вывод текущей строки списка смежных вершин.
        # Вывод графа в виде матрицы смежности.
        for row in self.adj_mat:  # Для каждой строки в матрцие смежности:
            print(row)  # Вывод текущей строки списка матрицы смежности.
        '''
        # Самый длинный путь, представленный элементами матрицы.
        path = self.path_restoring_modified_dijkstra(0, self.vertexes - 1)
        # Оптимизация полученных данных под условие вывода.
        nodes = []  # Массив индексов пройденных вершин.
        for i in range(len(path)):  # Для каждого элемента path:
            # Восстановление индекса элемента по его координатам в матрице.
            node = (path[i][0] - 1) * self.hor_vertex + path[i][1] - 1
            nodes.append(node)  # Добавление полученного индекса в массив индексов.
        final_array = []  # Массив с направлениями шагов и весами.
        current_weight = matrix_elements[0]  # Сумма значений пройденных элементов как набранное "кол-во проводников".
        for i in range(len(nodes) - 1):
            if nodes[i + 1] - nodes[i] == 1:  # Если был сделан шаг вправо:
                current_weight += self.adj_mat[nodes[i]][nodes[i + 1]]  # Добавление текущего веса к суммарному.
                final_array.append(['R', current_weight])  # Добавление выявленного направления шага и с. веса в массив.
            else:  # Иначе (если был сделан шан вниз):
                current_weight += self.adj_mat[nodes[i]][nodes[i + 1]]  # Добавление текущего веса к суммарному.
                final_array.append(['D', current_weight])  # Добавление выявленного направления шага и с. веса в массив.
        for element in final_array:  # Для каждого элемента в final_array:
            print(element[0], element[1])  # Вывод первого и второго элементов для element.


# Главная функция.
def main():
    matrix_elements = list()  # Список элементов матрицы (весов клеток поля).
    size = list(map(int, input().split()))  # Задание размера матрицы.
    m = size[0]  # Количество строк матрицы.
    n = size[1]  # Количество столбцов матрицы.
    for i in range(m):  # Для каждой строки матрицы:
        matrix_row_elements = list(map(int, input().split()))
        for element in range(n):
            matrix_elements.append(matrix_row_elements[element])
    w_graph = Graph(m, n)  # Создание пустого графа заданного размера.
    w_graph.app_longest_path(matrix_elements)  # Нахождение самого длинного пути от первого элемента к последнему.


# Точка входа в программу.
if __name__ == '__main__':
    main()
