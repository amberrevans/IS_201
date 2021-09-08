#widgets and gizmos

widgets = float(input('Enter the number of widgets: '))

gizmos = float(input('Enter the number of gizmos: '))

widgetWeight = widgets * 75
gizmoWeight = gizmos * 112

totalWeight = widgetWeight + gizmoWeight
print ('The total weight for your order is ',format(totalWeight, ',.2f'))