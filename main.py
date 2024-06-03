from typing import List

class Solution():
  def numberOfBeams(self, bank: List[str]):
    """
    :type bank: List[str]
    :rtype: int
    """
    # Verificando tamanho da array e se nela possuem apenas números 0 e 1.
    if any(len(c) < 1 or len(c) > 500 or not all(contador in '01' for contador in c) for c in bank) == True: return None

    # Separando as casas que não possuem dispositivos
    dispositivos = [valor for valor in bank if '1' in valor]
    # Quantidade de dispositivos em cada linha
    quantidade = [quantidade.count('1') for quantidade in dispositivos]
    # Multiplicação dos valores
    beams = [quantidade[x] * quantidade[x+1] for x in range(len(quantidade)-1)]

    return sum(beams)


bank = Solution()

bank.numberOfBeams(["011001","000000","010100","001000"]) # Output 8
bank.numberOfBeams(["000","111","000"]) # Output 0