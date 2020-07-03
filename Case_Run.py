from SteelSections import summary, outline

shape = [(0, 0), (5, 0), (5, 1), (3.125, 1), (2.125, 3), (0.875, 3), (1.875, 1), (0, 1)]
print(summary(shape))
outline(shape, 'skewed', format='png', size=(8, 6))