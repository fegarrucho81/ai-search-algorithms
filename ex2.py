# Importação de módulos
import random
import math  # Importa funções matemáticas como seno e exponencial.

# Definição da função tabu_search
def tabu_search(problem, steps=100, tabu_size=10):
    current = problem.initial_state()  # Obtém o estado inicial do problema.
    best_solution = current  # Inicialmente, a melhor solução é o estado inicial.
    tabu_list = []  # Lista tabu para armazenar estados já visitados.

    # Loop para iterar até o número máximo de passos
    for step in range(steps):
        neighbors = problem.get_neighbors(current)  # Obtém estados vizinhos.
        if not neighbors:  # Se não houver vizinhos, encerra a busca.
            break

        # Remove vizinhos que estão na lista tabu
        valid_neighbors = [n for n in neighbors if n not in tabu_list]
        if not valid_neighbors:  # Se todos os vizinhos forem tabu, encerra a busca.
            print("Todos os vizinhos estão na lista tabu. Parando a busca.")
            break

        # Escolhe o melhor vizinho com menor custo
        next_state = min(valid_neighbors, key=problem.evaluate)

        # Exibe informações sobre o progresso da busca
        print(f"Iteração: {step}, Estado atual = {current}, Próximo = {next_state}")
        print(f"Valor da função de custo(t): {problem.evaluate(current)}")
        print(f"Valor da função de custo(t+1): {problem.evaluate(next_state)}")

        # Atualiza a melhor solução encontrada até o momento
        if problem.evaluate(next_state) > problem.evaluate(best_solution):
            best_solution = next_state
            it_best_solution = (step + 1)  # Salva a iteração em que foi encontrada.

        # Atualiza a lista tabu
        tabu_list.append(current)  # Adiciona o estado atual à lista tabu.
        if len(tabu_list) > tabu_size:  # Mantém o tamanho da lista tabu limitado.
            tabu_list.pop(0)  # Remove o estado mais antigo da lista.

        # Atualiza o estado atual para o próximo estado
        current = next_state

    # Exibe a melhor solução encontrada
    print("\n")
    print("Iteração da melhor solução encontrada:", it_best_solution)
    print("Melhor solução encontrada:", best_solution)
    print("Valor da função de custo:", problem.evaluate(best_solution))
    return best_solution  # Retorna a melhor solução.

# Classe SimpleProblem: Define um problema simples para teste
class SimpleProblem:
    def __init__(self):
        self.range = range(-20, 20)  # Define o intervalo dos estados possíveis.

    def initial_state(self):
        return random.choice(self.range)  # Escolhe aleatoriamente um estado inicial.

    def get_neighbors(self, state):
        neighbors = [state - 1, state + 1]  # Define os vizinhos como "state - 1" e "state + 1".
        return [n for n in neighbors if n in self.range]  # Retorna vizinhos dentro do intervalo permitido.

    def evaluate(self, state):
        return math.sin(state) * math.exp(0.1 * state)  # Função de custo usando seno e exponencial.

# Execução do código
if __name__ == "__main__":
    problem = SimpleProblem()  # Instancia o problema.
    solution = tabu_search(problem)  # Aplica o algoritmo de busca tabu no problema.