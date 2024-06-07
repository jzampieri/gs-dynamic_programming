# GLOBAL SOLUTION BLUE OCEAN - DYNAMIC PROGRAMMING

## Descrição do Projeto

O projeto "Global Solution Blue Ocean - Dynamic Programming" visa otimizar a alocação de recursos e a distribuição de sensores em áreas marinhas para maximizar a biodiversidade e minimizar vulnerabilidades. O projeto utiliza programação dinâmica e o Teorema de Pick para calcular áreas de polígonos em uma grade de pontos inteiros. 

### Funcionalidades Principais

1. **Geração de Áreas Marinhas Aleatórias**: Gera áreas marinhas com dados fictícios de biodiversidade, vulnerabilidades e conectividade, além de pontos internos e na borda usando uma grade de pontos inteiros.

2. **Cálculo do Valor das Áreas Marinhas**: Utiliza uma fórmula ponderada para calcular o valor de uma área marinha baseada em seus índices de biodiversidade, vulnerabilidades e conectividade.

3. **Otimização de Alocação de Recursos**: Implementa um método guloso para otimizar a alocação de recursos nas áreas marinhas.

4. **Distribuição de Sensores**: Encontra a distribuição ótima de sensores em uma área, maximizando a cobertura.

5. **Estimativa de Recursos Necessários**: Calcula a quantidade de recursos (em toneladas) necessários para que cada área atinja um valor considerado saudável.

6. **Cálculo de Área Usando o Teorema de Pick**: Calcula a área de um polígono simples cujos vértices estão em pontos de uma grade de pontos inteiros.

## Responsáveis

- **JULIO CESAR ZAMPIERI** - RM98772
- **LEONARDO SHUNCK RAINHA** - RM99902
- **KAYKY OLIVEIRA SHUNCK** - RM99756

## Instalação

Para executar este projeto, você precisará do Python instalado em seu ambiente. As bibliotecas necessárias são:

- `random`
- `math`

Certifique-se de ter essas bibliotecas instaladas antes de executar o código.

## Como Usar

1. **Geração de Áreas**: Use a função `generate_random_areas(num_areas, grid_size)` para gerar uma lista de áreas marinhas aleatórias.

2. **Cálculo de Valor das Áreas**: Utilize a função `calc_sea(biodiversity, vulnerabilities, connectivity)` para calcular o valor de cada área marinha.

3. **Otimização de Recursos**: A função `optimize_resource_allocation(areas, total_resources)` ajuda a otimizar a alocação de recursos.

4. **Distribuição de Sensores**: Use a função `optimize_sensor_distribution(num_sensors, area_size, areas)` para encontrar a distribuição ótima de sensores.

5. **Estimativa de Recursos Necessários**: A função `estimate_resources_for_health(area, health_threshold)` calcula os recursos necessários para que cada área atinja um valor saudável.

6. **Cálculo de Área com Teorema de Pick**: Utilize a função `calculate_area_sea(internal_points, boundary_points)` para calcular a área de um polígono usando o Teorema de Pick.

7. **Execução Completa**: A função `find_optimal_distribution` coordena a geração de áreas, otimização de recursos e distribuição de sensores.

```python
find_optimal_distribution(num_areas=10, total_resources=5, num_sensors=5, area_size=(10, 10), health_threshold=0.7, grid_size=10)
```

## Referências

- Pick's Theorem - A simple formula for the area of lattice polygons: [Wikipedia](https://en.wikipedia.org/wiki/Pick%27s_Theorem)
- Greedy Algorithm - A method for solving optimization problems: [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
- Euclidean Distance - Calculating the distance between two points: [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_distance)
