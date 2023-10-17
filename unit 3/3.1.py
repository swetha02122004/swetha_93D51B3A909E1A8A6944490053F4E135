def linear_search_product(products, targetproduct):
  indices = []
  for index, product in enumerate(products):
    if product == targetproduct:
      indices.append(index)
  return indices


productlist = ["bat", "ball", "football", "ball", "bat", "tennisracket", "basketball","tennisracket"]
target = input("enter the target product:")
result = linear_search_product(productlist, target)
print(result)
