from collections import deque

def can_exit(maze):
    R = len(maze)
    C = len(maze[0])
    
    # Coordonatele start și end
    START = (0, 0)
    END = (R - 1, C - 1)
    
    # Verificare inițială
    if maze[0][0] == 1 or maze[R - 1][C - 1] == 1:
        return False
        
    queue = deque([START])
    visited = {START}
    
    # Direcțiile: (dr, dc)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        # Am ajuns la ieșire
        if (r, c) == END
            return True
        
        # Explorează vecinii
        for dr, dc in directions:
            nr, nc = r + dr, c + dc #se calculeaza noile coordonate ale celulei vecine
            
            # Verifică limitele, calea liberă (0) și dacă e vizitat
            if (0 <= nr < R and 0 <= nc < C and  # se verifica daca vecinul este in matrice 
                maze[nr][nc] == 0 and (nr, nc) not in visited): # verifica daca este cale libera si daca nu a fost vizitat
                
                visited.add((nr, nc))  
                queue.append((nr, nc))
                        
    return False
maze1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]
maze2 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]

print(f"Labirint 1: {can_exit(maze1)}")
print(f"Labirint 2: {can_exit(maze2)}")
