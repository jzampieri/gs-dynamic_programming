import random
import math


def calc_sea(biodiversity, vulnerabilities, connectivity):
    """
    Calcula o valor de uma área marinha baseado em biodiversidade, vulnerabilidades e conectividade.

    Args:
    biodiversity (float): Índice de biodiversidade.
    vulnerabilities (float): Índice de vulnerabilidades.
    connectivity (float): Índice de conectividade.

    Returns:
    float: Valor calculado da área.
    """
    weights = [0.5, 0.3, 0.2]
    value = weights[0] * biodiversity + weights[1] * vulnerabilities + weights[2] * connectivity
    return round(value, 2)


def generate_random_areas(num_areas, grid_size):
    """
    Gera dados fictícios aleatórios de áreas marinhas com pontos em uma grade.

    Args:
    num_areas (int): Número de áreas a serem geradas.
    grid_size (int): Tamanho da grade.

    Returns:
    list of dict: Lista de áreas com pontos internos e na borda.
    """
    areas = []
    for _ in range(num_areas):
        I = random.randint(1, grid_size - 2)
        B = random.randint(3, 2 * (grid_size - 1))
        areas.append({
            'internal_points': I,
            'boundary_points': B,
            'biodiversity': round(random.uniform(0, 1), 2),
            'vulnerabilities': round(random.uniform(0, 1), 2),
            'connectivity': round(random.uniform(0, 1), 2)
        })
    return areas


def calculate_distance(point1, point2):
    """
    Calcula a distância euclidiana entre dois pontos.

    Args:
    point1 (tuple): Coordenadas do primeiro ponto (x, y).
    point2 (tuple): Coordenadas do segundo ponto (x, y).

    Returns:
    float: Distância euclidiana entre os pontos.
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def optimize_resource_allocation(areas, total_resources):
    """
    Otimiza a alocação de recursos em áreas marinhas usando método guloso.

    Args:
    areas (list of dict): Lista de áreas marinhas.
    total_resources (int): Número total de recursos disponíveis.

    Returns:
    tuple: Alocação de recursos e valor total das áreas selecionadas.
    """
    for area in areas:
        area['value'] = calc_sea(area['biodiversity'], area['vulnerabilities'], area['connectivity'])

    areas_sorted = sorted(areas, key=lambda x: x['value'], reverse=True)
    allocation = [1 if i < total_resources else 0 for i in range(len(areas_sorted))]
    total_value = round(sum(area['value'] for i, area in enumerate(areas_sorted) if allocation[i] == 1), 2)

    return allocation, total_value


def optimize_sensor_distribution(num_sensors, area_size, areas):
    """
    Encontra a distribuição ótima dos sensores em uma área.

    Args:
    num_sensors (int): Número de sensores disponíveis.
    area_size (tuple): Tamanho da área (largura, altura).
    áreas (list of dict): Lista de áreas marinhas.

    Returns:
    tuple: Posições dos sensores e os sensores nas melhores posições.
    """
    sensors = [(round(random.uniform(0, area_size[0]), 2), round(random.uniform(0, area_size[1]), 2))
               for _ in range(num_sensors)]

    sensor_coverage = [0] * num_sensors
    for i, sensor in enumerate(sensors):
        for area in areas:
            area_position = (random.uniform(0, area_size[0]), random.uniform(0, area_size[1]))
            if calculate_distance(sensor, area_position) < 5:
                sensor_coverage[i] += 1

    best_sensors = sorted(range(num_sensors), key=lambda x: sensor_coverage[x], reverse=True)

    return sensors, best_sensors


def estimate_resources_for_health(area, health_threshold):
    """
    Estima a quantidade de recursos necessários para deixar uma área saudável.

    Args:
    area (dict): Dados da área marinha.
    health_threshold (float): Valor mínimo para uma área ser considerada saudável.

    Returns:
    float: Quantidade estimada de recursos necessários em toneladas.
    """
    if area['value'] >= health_threshold:
        return 0
    else:
        resource_needed = (health_threshold - area[
            'value']) * 10  # Supondo que 1 unidade de recurso aumenta o valor em 0.1
        return round(resource_needed, 2)


def calculate_area_sea(internal_points, boundary_points):
    """
    Calcula a área de um polígono usando o Teorema de Pick.

    Args:
    internal_points (int): Número de pontos internos ao polígono.
    boundary_points (int): Número de pontos na borda do polígono.

    Returns:
    float: Área do polígono.
    """
    return internal_points + boundary_points / 2 - 1


def find_optimal_distribution(num_areas, total_resources, num_sensors, area_size, health_threshold, grid_size):
    """
    Coordena a geração de áreas, otimização de alocação de recursos e distribuição de sensores.

    Args:
    num_areas (int): Número de áreas marinhas a serem geradas.
    total_resources (int): Número total de recursos disponíveis.
    num_sensors (int): Número de sensores disponíveis.
    area_size (tuple): Tamanho da área (largura, altura).
    health_threshold (float): Valor mínimo para uma área ser considerada saudável.
    grid_size (int): Tamanho da grade para o cálculo de áreas.
    """
    areas = generate_random_areas(num_areas, grid_size)
    allocation, total_value = optimize_resource_allocation(areas, total_resources)

    print("Alocação ótima de recursos:", allocation)
    print("Valor total das áreas marinhas:", total_value)
    print("\nDetalhes das áreas marinhas:")
    for i, area in enumerate(areas):
        area['area_sea'] = calculate_area_sea(area['internal_points'], area['boundary_points'])
        resources_needed = estimate_resources_for_health(area, health_threshold)
        print(
            f"Área {i + 1}: Biodiversidade = {area['biodiversity']}, Vulnerabilidades = {area['vulnerabilities']}, Conectividade = {area['connectivity']}, Valor = {area['value']}, Área marinha (unidades de área) = {area['area_sea']}, Recursos necessários para saúde (toneladas) = {resources_needed}")

    sensors, best_sensors = optimize_sensor_distribution(num_sensors, area_size, areas)

    print("\nDistribuição ótima dos sensores:")
    for i, position in enumerate(sensors):
        print(f"Sensor {i + 1}: Posição = {position}")

    print("\nSensores com as melhores posições:")
    for sensor in best_sensors:
        print(f"Sensor {sensor + 1}: Posição = {sensors[sensor]}")


find_optimal_distribution(num_areas=10, total_resources=5, num_sensors=5, area_size=(10, 10), health_threshold=0.7,
                          grid_size=10)
