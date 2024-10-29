import numpy as np
import matplotlib.pyplot as plt
import requests as rqst
import pprint

#Использование NumPy
arr = np.array([1, 2, 3, 4, 5])

arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_sqrt = np.sqrt(arr)

print("Сумма элементов:", arr_sum)
print("Среднее значение:", arr_mean)
print("Квадратный корень каждого элемента:", arr_sqrt)

#Использование MatPlotLib
x_list = []
y_list = []
for x in range(1, 20):
    y = 1 / x
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list, label="Муд по жизни", color="red")
plt.xlabel("Расстояние, которое я проехал")
plt.ylabel("Осталось времени до дома")
plt.title("Езда в час пик домой на автобусе")
plt.legend()
plt.grid(True)
plt.show()

#Использование Requests
response = rqst.get("https://api.github.com")

if response.status_code == 200:
    print("Запрос успешен!")
    json_data = response.json()
    pprint.pp(f"Данные JSON:{json_data}")
else:
    print("Ошибка запроса:", response.status_code)

data = {'key1': 'value1', 'key2': 'value2'}
post_response = rqst.post("https://httpbin.org/post", data=data)
pprint.pp(f"Ответ POST-запроса:,{post_response.json()}")
