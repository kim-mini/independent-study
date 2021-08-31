# 밑바닥부터 시작하는 딥러닝

## 퍼셉트론 구현하기

```python

def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7 
  tmp = x1*w1 + x2*w2 
  if tmp <= theta: 
    return 0 
  else: 
    return 1


print(AND(0, 0)) # 0 
print(AND(0, 1)) # 0 
print(AND(1, 0)) # 0 
print(AND(1, 1)) # 1

```

 - 가중치와 편향 도입
