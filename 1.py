import heapq

def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]

def min_cost(cables):
    if not cables:
        cost = 0
    elif len(cables) < 2:
        cost = cables[0]
    else:
        cables_sorted = heap_sort(cables)
        print(cables_sorted)
        cost = cables_sorted[0] + cables_sorted[1]
        new_cables =  cables_sorted[2:]
        new_cables.append(cost)
        cost =+ min_cost(new_cables)
    return cost

if __name__ == "__main__":
    cables = [5,9,6,2,3,7]
   

    print(min_cost(cables))