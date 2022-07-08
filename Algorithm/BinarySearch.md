# ****이분 탐색 (Binary Search)**** 알고리즘

범위를 점점 좁혀가며 탐색을 하는 알고리즘으로, 이진 탐색이라고도 한다. 하나씩 찾는 것이 아닌 left와 right 양쪽에서 탐색을 하기 때문에 일반 탐색에 비해 속도가 빠르다. **시간복잡도는 일반 탐색이 O(n), 이분 탐색이 O(log n)**이다.

# 알고리즘 작동방식

1. 미리 정렬된 배열에서, 정해놓은 인덱스 위치인 left와 right로 mid 값을 정해줌(mid = (left + right) / 2)
2. mid가 가리키는 값과 목표 값(result)을 비교한다.
    1. **mid > result**, right = mid - 1mid가 가리키는 값보다 목표 값이 더 작을 경우, 목표 값이 절반 아래쪽에 포함된 범위 안에 들어있기 때문에 right를 mid - 1로 설정
    2. **mid < result**, left = mid + 1mid가 가리키는 값보다 목표 값이 더 클 경우, 목표 값이 절반 위쪽 범위 안에 포함된 범위 안에 들어있기 때문에 left를 mid + 1로 설정
3. left > right 가 될 때 까지, 혹은 목표 값을 찾을 때 까지 1~3 반복

앞서 설명한 1과 같이, 탐색하는 배열은 반드시 **미리 정렬**이 되어있어야 한다.
 

# 예시

미리 정렬된 배열 A = { 1, 2, 3, 4, 5, 6, 7, 8 } 에서 찾고자 하는 값이 7일때, 이분 탐색 과정은 다음과 같다.

이 때, 초기 left = 1, right = 8이다.

![img1.daumcdn.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ec4957f-9ded-40d5-b3b9-4dd77339091b/img1.daumcdn.jpg)

***1단계***
 : mid = (left + right) / 2 에 의해 mid = 4가 되고, A[4]와 찾는 목표 값 7을 비교하였을 때, A[4] < 7이기 때문에 left를 mid + 1인 5로 설정한다.

![img1.daumcdn.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/252300a4-5882-482e-ad2f-b2a881d57546/img1.daumcdn.jpg)

***2단계***
 : mid = (5 + 8) / 2 = 6이 되고, A[6]과 찾는 목표 값 7을 비교하였을 때, A[6] < 7이기 때문에 left를 7로 설정한다.

![img1.daumcdn.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a00fec34-b91b-4347-85d8-2b9a07152fc3/img1.daumcdn.jpg)

***3단계***
 : mid = (7 + 8) / 2 = 7이 되고, A[7]과 찾는 목표 값 7을 비교하였을 때, A[7]과 값이 일치하기 때문에 이분 탐색을 종료한다.

# 코드

알고리즘의 주요 코드는 다음과 같다.

```python
# 재귀함수를 활용한 이진 탐색 구현
def binary_search (arr, target, start, end):
    
    if start > end:
        return None
    
    # 중간 인덱스는 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스
    # 몫만 구하기 위해 // 연산자 활용
    mid = (start + end) // 2
    
    # 중간 인덱스의 값이 타겟 데이터와 같은 경우 탐색 종료
    if arr[mid] == target:
        return mid
        
    # 중간 인덱스의 값이 타겟 데이터보다 큰 경우
    # 마지막 인덱스를 중간 인덱스의 한 칸 앞으로 이동
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
        
    # 중간 인덱스의 값이 타겟 데이터보다 작은 경우
    # 시작 인덱스를 중간 인덱스의 한 칸 뒤로 이동
    else:
        return binary_search(arr, target, mid+1, end)
```

```python
# 반복문을 활용한 이진 탐색 구현
def binary_search (arr, target, start, end):
    while start <= end:
        # 중간 인덱스는 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스
        # 몫만 구하기 위해 // 연산자 활용
        mid = (start + end) // 2
    
        # 중간 인덱스의 값이 타겟 데이터와 같은 경우 탐색 종료
        if arr[mid] == target:
            return mid
        
        # 중간 인덱스의 값이 타겟 데이터보다 큰 경우
        # 마지막 인덱스를 중간 인덱스의 한 칸 앞으로 이동
        elif arr[mid] > target:
            end = mid - 1
        
        # 중간 인덱스의 값이 타겟 데이터보다 작은 경우
        # 시작 인덱스를 중간 인덱스의 한 칸 뒤로 이동
        else:
            start = mid + 1
            
    return None
```

---

## 연습문제

1. 백준 1920번 수 찾기
2. 백준 1654번 랜선 자르기
3. 백준 2805번 나무 자르기
4. 백준 6236번 용돈 관리