# Python은 Sequence 객체에 대해 음수 인덱스와 stride(보폭) 개념을 지원한다

# -- 음수 인덱스
t = 1, 2, 3, 4, 5
print(t[-1]) # 5
print(t[-3]) # 3
# Sequence의 맨 마지막 요소부터 첫 요소까지 값이 작아지는 형태(-1, -2, -3, ...)

print(t[-3:]) # (3, 4, 5)
print(t[:-2]) # (1, 2, 3)
print(t[-4:-1]) # (2, 3, 4)
# 슬라이싱에서도 음수 인덱스를 제공한다

# -- stride
print(t[0:4:2]) # (1, 3)
# seq[n:m:k]
# n부터 m-1번 인덱스 사이의 요소를 k만큼씩 인덱싱하며 sequence를 만들어냄을 의미한다(stride의 기본값은 1)

# stride에도 음수를 사용할 수 있다
print(t[4:0:-1]) # (5, 4, 3, 2)
# seq[n:m:k]에서, n번 인덱스부터 m번 인덱스까지 k만큼의씩 좌측 방향으로 참조해나감을 의미한다. 방향이 뒤바뀐다고 생각하면 된다
# stride에 음수를 사용하는 경우, seq[n:m:k]에서 n이 m보다 커야 제대로 된 결과를 얻을 수 있다
# 이를 이용해, 시작/종료 인덱스를 생략하고 stride를 -1로 두어 sequence를 뒤집을 수도 있다
print(t[::-1])
# 자주 사용하진 않지만, 알아 두면 좋음
