### **Petri Nets : Properties, Analysis and Applications**
___
<br>

#### **[1. INTRODUCTION]**
- **Petri net** : 그래피컬하고 수학적인 모델링 툴.
- token : 시스템의 동적 및 동시 활동을 시뮬레이션하기위해 이용
- petri net은 강력한 소통의 매게체이다. 실사용자와 이론적(수학적)으로도 쓰일수 있기 때문.
- 나머지는 역사 얘기. 패스

<br><br>
#### **[2.TRANSITION ENABLING AND FIRING]**
- Petri-net theory상에서 중요한 룰 1가지 : TRANSITIONE NABLING AND FIRING
- token(k) : 검은색 점
- place(p) = condition : 동그라미
- transition = event : bar 혹은 box
- **질문 : arc(w) : 가중치..?, 정확한 의미**

| Input Places | Transition | Output Places |
|---|:---:|---:|
| Preconditions | Event | Postconditions |
| Input data | Computation step | Output data |
| Input signals | Signal processor | Output signals |
| Resources needed | Task or job | Resource released |
| Conditions | Clause in logic | Conclusion(s) |
| Buffers | Processor | Buffers |

- source transition : input place가 없는 transition
- sink transition : output place가 없는 transition

<br><br><br>

![img](https://ifh.cc/g/vB4BC4.png)
- Fig.1. transition의 예시(firing)rule : (a) :firing 전의 enable한 transition t 상태
- (b) : t를 firing한 뒤의 마킹상태, 그리고 t는 이제 disabled한 상황

<br><br><br>

#### **[3.INTRODUCTORY MODELING EXAMPLES]**
- finite capacity net : 각 place가 홀딩할수있는 token의 수는 상한선이 고려되어야한다.
- finite capacity net(유한 용량 망)(N, MO)의 경우, 각 장소 'p'는 관련 용량 K(p)를 가지며, 이는 'p'가 언제든지 보유할 수 있는 최대 토큰 수이다.
- 유한 용량 네트의 경우, transition 't'가 활성화되기 위해서는, 't'의 각 출력 place 'p'의 토큰 수가 't'를 fire한 후 용량 K(p)를 초과할 수 없다는 추가 조건이 있다.
- strict transition rule : capacity constraint를 가진 rule
- weak transition rule : capacity constraint를 가지지않은 rule
- **질문 : fugure2 에서 b그림 어떻게 흘러가야하는지**
- **질문 :  pure finite-capacity net?**
- **질문 : input과 output이 같아야한다는 말은 들어오는 아크의 수랑 나가는 아크의 수가 같아야한다는말?아닌거 같은데 그럼 저 말은 페트리넷 전체의 관점에서 input과 output이 같아야한다는 말인가?**
- **질문 : k-weight arc??**
- inhibitor arc : 보통은 input place에 token이 있어야 fire할수 있는데 이 선으로 연결되어있으면 해당 input place에 token이 없어야 fire가능
- extended Petri net : inhibitor arc가진 Petri net

<br><br><br>

#### **[4.BEHAVIORAL PROPERTIES]**
- Boundedness : 모든 place p에서 허용된 토큰의 수 k를 넘지않고, 모든 marking이$M_0$에서 Reachable하면 그 Patri net($N,M_0$)은 안전하고 1-bounded하다고 말할수있다.
- 'live' Petri net : 어떤 firing sequence가 선택되도 deadlock이 일어나지 않는 Petri net
    - **LO-live**(dead) : 어떤 firing sequnce에서도 fire되지 않는 상태
    - **L1-live**(potentiall firable) : 몇몇 firing sequnce만 가능
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\vdots$
    - **L4-live**(live) : 모든 마킹이 가능
- Reversibility : 어느 상태에서도 $M_0$로 돌아갈수있는 patri net은 reversible하다.
- Persistence : Patri net($N,M_0$)은 활성화된 두 개의 transition에 대해 하나의 transition을 실행해도 다른 하나가 비활성화되지 않을 경우 persistent하다고 한다.

<br><br><br>

#### **[5.ANALYSIS METHOD]**
- 분석방법 3가지
     1. coverability (reachability) tree method
     2. matrix-equation approach
     3. reduction or decomposition techniques

<br>

##### **[A. The Coverability Tree]**
- 당장 필요하진않아서 일단 스킵

<br>

##### **[B. Incidence Matrix and State Equation]**
- 실제 현장등의 다이나믹한 모습의 Petri net을 matrix equation으로 표현할수 있는 방법
- 하지만 non-deterministic한 자연현상이나 제약등으로 해결가능성이 제한될 때가 많다.
- 그래서 이 논문에선 Petri net을 pure하다고 가정하거나 더미형태의 transition이나 place를 넣어 pure하게 만들어준다.

<br><br>

- <span style='background-color:#fff5b1'>**[Incidence Matrix]** </span>
    - Petri net N : n개의 transition, m개의 place에서의
    - **incidence Matrix A : [$a_{ij}$]**(n x m의 matrix형태, 정수)
    > $a_{ij} = a_{ij}^+ - a_{ij}^-$ <br>
    > $a_{ij}^+ = w(i,j)$ : transition i에서 output place j로의 arc의 가중치(weight)<br>
    > $a_{ij}^- = w(j,i)$ : input place j에서 transition i로의 arc의 가중치(weight)
    - $A^T$말고 A를 incidence Matrix로 쓴다.<br><br>
    - transition i가 한 번fire될 때,
    - $a_{ij}^-$ : 감소된 token수
    - $a_{ij}^+$ : 추가된 token수
    - $a_{ij}$ : place j에서 변화된 token수
    > $a_{ij}^- \le M(j),$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$j = 1,2 \cdots, m$

    - **[State Equation]**
    - marking $M_k$ : m x 1의 컬럼벡터
    - $M_k$의 j번째 entry : k번째 firing 직후 j에 있는 토큰의 수
    - $u_k$ : firing vector or control vector, n x 1으로 된 컬럼벡터, 전체 원소 중 하나빼고 다 0
    > $M_k = M_{k-1} + A^T u_k$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$k = 1,2 \cdots$
    - incidence Matrix A의 j번째 행은 transition i의 발화의 결과로써 마킹의 변화를 나타낸다. 
    <br><br>
    - **[Necessary Reachability Condition(필수 도달가능성 조건)]** : firing sequence {$u_1, u_2, \cdots, u_d$}을(를) 통해 목적지 마킹 $M_d$는 $M_0$로부터 도달가능하다고 가정한다.
    > $M_d = M_0 + A^T \sum_{k=1}^d u_k$ <br>
    > $A^T x = \triangle M$ 이라고도 쓸수 있음
    - $\triangle M = M_d - M_0,$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $x = \sum_{k=1}^d u_k$
    - x : firing count vector, n x 1의 컬럼벡터, 비음의 정수로 구성
    - x의 i번째 원소는 $M_0$에서 $M_d$로 가기위해 실행되어야하는 트렌지션 i의 횟수 
    

    > $B_f = [I_\mu : -A^T_{11}(A^T_{12})^{-1}]$
    - $I_\mu$ : 단위행렬, $\mu = m - r$
    