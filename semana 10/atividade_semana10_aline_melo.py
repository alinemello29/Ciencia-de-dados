# -*- coding: utf-8 -*-
"""Atividade_Semana10-Aline Melo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SIfi8I8LUCqunt1jJMp8NVH4qidzJ8it

# Atividade da Semana 10

Esta é atividade semanal sugerida. Você deverá preenchê-la e enviá-la dentro do prazo (até o fechamento da semana corrente).
"""

# Instalando o pacote 'ipeadatapy'
!pip install ipeadatapy

# Carregando pacotes
import pandas as pd
import ipeadatapy
import matplotlib.pyplot as plt

# Obtendo serie com dados sobre emplacamento de veículos
emplacamentos = ipeadatapy.timeseries('ANFAVE12_LICVEN12')
emplacamentos.reset_index(inplace=True)
emplacamentos = emplacamentos.loc[(
    emplacamentos["DATE"] >= "2015-01-01") & (emplacamentos["DATE"] < "2019-01-01"),
                                  "VALUE (-)"]
emplacamentos.rename("emplacamentos", inplace=True)

# Obtendo serie com dados sobre IPI arrecadado sobre automóveis
ipi = ipeadatapy.timeseries('SRF12_IPI12')
ipi.reset_index(inplace=True)
ipi = ipi.loc[(ipi["DATE"] >= "2015-01-01") & (ipi["DATE"] < "2019-01-01"),
                                  "VALUE (R$)"]
ipi.rename("ipi", inplace=True)

carros = pd.concat([emplacamentos.reset_index(drop=True),
                    ipi.reset_index(drop=True)],
                   axis=1)
carros

"""###Questão 1

Vamos relembrar o seguinte:

> O número de veículos emplacados (ou seja, veículos que foram comprados novos) funciona como um indicador econômico que demonstra o poder aquisitivo da população em geral. Estes dados também são úteis como indicadores de saúde, uma vez que, uma frota mais nova, polui menos o ar e o número de casos de doenças respiratórias em grandes centros é reduzido.

> O Imposto sobre Produtos Industrializados, cuja sigla é IPI, é um imposto federal, ou seja, somente a União pode instituí-lo ou modificá-lo, sobre produtos industrializados no Brasil.

É possível utilizar uma regressão linear para estimar o `IPI` utilizando o `número de veículos emplacados`? Argumente utilizando alguma medida estatística para este fim.

"""

# Questao 1
'''
Questão 1: Utilização da Regressão Linear para Estimar o IPI
Sim, é possível utilizar uma regressão linear para estimar o IPI (Imposto sobre Produtos Industrializados) com base no número de veículos emplacados. A regressão linear é uma técnica estatística que modela a relação entre uma variável dependente e uma ou mais variáveis independentes, permitindo a previsão e a análise de tendências.

Argumentação:
Relação Entre Variáveis:
O número de veículos emplacados pode ser um bom preditor da arrecadação do IPI, uma vez que um aumento nas vendas de veículos novos normalmente leva a um aumento na arrecadação desse imposto. Essa relação econômica sugere que a variável independente (emplacamentos) pode influenciar a variável dependente (IPI).
Medidas Estatísticas:
Coeficiente de Correlação (r): Antes de aplicar a regressão linear, é útil calcular o coeficiente de correlação entre o número de emplacamentos e o IPI. Um coeficiente de correlação próximo de 1 ou -1 indicaria uma relação forte, positiva ou negativa, respectivamente, o que justificaria o uso da regressão linear.
R² (Coeficiente de Determinação): Após ajustar o modelo de regressão, o R² pode ser utilizado para avaliar a qualidade do ajuste. Ele mede a proporção da variância do IPI que é explicada pelo número de emplacamentos. Um R² próximo de 1 sugere que o modelo é eficaz em explicar as variações no IPI.
Teste de Significância: O teste de hipóteses, como o teste t, pode ser usado para determinar se o coeficiente da variável de entrada (emplacamentos) é estatisticamente significativo. Se for significativamente diferente de zero, isso indica que há uma contribuição real dos emplacamentos para a previsão do IPI.
Assumptions da Regressão Linear:
Para que a regressão linear seja válida, algumas suposições devem ser atendidas:
Linearidade: A relação entre as variáveis deve ser linear.
Homoscedasticidade: A variância dos resíduos deve ser constante ao longo dos valores preditores.
Independência dos Erros: Os erros do modelo devem ser independentes.
Normalidade dos Erros: Os resíduos devem seguir uma distribuição normal, o que pode ser verificado através de testes estatísticos ou gráficos (como o gráfico Q-Q).
Conclusão
A regressão linear pode ser uma ferramenta útil para estimar o IPI a partir do número de veículos emplacados, desde que as suposições da técnica sejam atendidas e que a análise estatística mostre uma relação significativa entre as variáveis. A avaliação do coeficiente de correlação e do R² pode fornecer insights sobre a força e a efetividade do modelo de previsão.
'''

"""###Questão 2

Crie uma base de `treinamento` e de `teste` para o ajuste de um modelo linear. Utilize 70% dos dados como conjunto de treinamento.

"""

# Questao 2
# Carregando pacotes
import pandas as pd
import ipeadatapy
from sklearn.model_selection import train_test_split

# Obtendo série com dados sobre emplacamento de veículos
emplacamentos = ipeadatapy.timeseries('ANFAVE12_LICVEN12')
emplacamentos.reset_index(inplace=True)
emplacamentos = emplacamentos.loc[(emplacamentos["DATE"] >= "2015-01-01") &
                                  (emplacamentos["DATE"] < "2019-01-01"), "VALUE (-)"]
emplacamentos.rename("emplacamentos", inplace=True)

# Obtendo série com dados sobre IPI arrecadado sobre automóveis
ipi = ipeadatapy.timeseries('SRF12_IPI12')
ipi.reset_index(inplace=True)
ipi = ipi.loc[(ipi["DATE"] >= "2015-01-01") &
              (ipi["DATE"] < "2019-01-01"), "VALUE (R$)"]
ipi.rename("ipi", inplace=True)

# Concatenando os dados
carros = pd.concat([emplacamentos.reset_index(drop=True), ipi.reset_index(drop=True)], axis=1)

# Criando as variáveis independentes (X) e dependentes (y)
X = carros[['emplacamentos']].values  # Variável independente
y = carros['ipi'].values  # Variável dependente

# Dividindo os dados em conjunto de treinamento e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Exibindo os tamanhos dos conjuntos
print(f"Tamanho do conjunto de treinamento: {len(X_train)}")
print(f"Tamanho do conjunto de teste: {len(X_test)}")

"""###Questão 3

Treine o modelo linear utilizando a base de `treino`.
"""

# Questao 3
# Carregando pacotes
import pandas as pd
import ipeadatapy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Obtendo série com dados sobre emplacamento de veículos
emplacamentos = ipeadatapy.timeseries('ANFAVE12_LICVEN12')
emplacamentos.reset_index(inplace=True)
emplacamentos = emplacamentos.loc[(emplacamentos["DATE"] >= "2015-01-01") &
                                  (emplacamentos["DATE"] < "2019-01-01"), "VALUE (-)"]
emplacamentos.rename("emplacamentos", inplace=True)

# Obtendo série com dados sobre IPI arrecadado sobre automóveis
ipi = ipeadatapy.timeseries('SRF12_IPI12')
ipi.reset_index(inplace=True)
ipi = ipi.loc[(ipi["DATE"] >= "2015-01-01") &
              (ipi["DATE"] < "2019-01-01"), "VALUE (R$)"]
ipi.rename("ipi", inplace=True)

# Concatenando os dados
carros = pd.concat([emplacamentos.reset_index(drop=True), ipi.reset_index(drop=True)], axis=1)

# Criando as variáveis independentes (X) e dependentes (y)
X = carros[['emplacamentos']].values  # Variável independente
y = carros['ipi'].values  # Variável dependente

# Dividindo os dados em conjunto de treinamento e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Exibindo os coeficientes do modelo
print(f"Coeficiente angular (slope): {modelo.coef_[0]}")
print(f"Intercepto (intercept): {modelo.intercept_}")

"""###Questão 4

Avalie a `performance` do modelo estimado através do **coeficiente de determinação** $R^2$.
*    Qual percentual de variabilidade do `IPI` é explicado pelo `número de emplacamentos`?
*    O que esse valor calculado representa?

"""

# Questao 4
# Avaliando a performance do modelo utilizando R²
r_squared = modelo.score(X_test, y_test)

# Exibindo o coeficiente de determinação R²
print(f"Coeficiente de Determinação R²: {r_squared:.4f}")
percentual_variabilidade = r_squared * 100
print(f"Percentual de variabilidade do IPI explicado pelo número de emplacamentos: {percentual_variabilidade:.2f}%")

"""###Questão 5

Faça a previsão para o conjunto de teste.
*    Calcule o $R^2$ para estes resultados
*    Faça o gráfico que exibe os dados observados e a reta estimada pelo modelo linear
"""

# Questao 5
# Importando pacotes necessários
import pandas as pd
import ipeadatapy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Obtendo série com dados sobre emplacamento de veículos
emplacamentos = ipeadatapy.timeseries('ANFAVE12_LICVEN12')
emplacamentos.reset_index(inplace=True)
emplacamentos = emplacamentos.loc[(emplacamentos["DATE"] >= "2015-01-01") &
                                  (emplacamentos["DATE"] < "2019-01-01"), "VALUE (-)"]
emplacamentos.rename("emplacamentos", inplace=True)

# Obtendo série com dados sobre IPI arrecadado sobre automóveis
ipi = ipeadatapy.timeseries('SRF12_IPI12')
ipi.reset_index(inplace=True)
ipi = ipi.loc[(ipi["DATE"] >= "2015-01-01") &
              (ipi["DATE"] < "2019-01-01"), "VALUE (R$)"]
ipi.rename("ipi", inplace=True)

# Concatenando os dados
carros = pd.concat([emplacamentos.reset_index(drop=True), ipi.reset_index(drop=True)], axis=1)

# Criando as variáveis independentes (X) e dependentes (y)
X = carros[['emplacamentos']].values  # Variável independente
y = carros['ipi'].values  # Variável dependente

# Dividindo os dados em conjunto de treinamento e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazendo previsões para o conjunto de teste
y_pred = modelo.predict(X_test)

# Calculando o R² para os resultados
r_squared_test = modelo.score(X_test, y_test)
print(f"Coeficiente de Determinação R² para o conjunto de teste: {r_squared_test:.4f}")

# Gráfico dos dados observados e a reta estimada pelo modelo
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Dados Observados')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Reta Estimada')
plt.title('Previsão do IPI com Base em Emplacamentos')
plt.xlabel('Número de Emplacamentos')
plt.ylabel('IPI Arrecadado (R$)')
plt.legend()
plt.grid()
plt.show()