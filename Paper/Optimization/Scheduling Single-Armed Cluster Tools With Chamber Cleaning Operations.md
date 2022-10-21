### **Scheduling Single-Armed Cluster Tools With Chamber Cleaning Operations**
(챔버 Cleaning 작업을 통한 Single-Arm 클러스터툴 스케줄링)
___

<br><br>
**[ Abstract ]**
- purge operations : chamber cleaning같은 스케줄링 복잡성을 증가시키는 작업
- parallel chamber를 위한 partial loading을 하는 backward($z$) sequence를 제안할 것
- **vector $z$** : 각 process step $i$에서 몇 개의 챔버 $z_i$를 청소하기 위해 비워두었는가?
- 목적 : optimal vector $z$를 찾자.

<br><br><br>

#### **[ 1. INTRODUCTION ]**
- 웨이퍼 공정 이후에 processing chamber에 잔여 가스 혹은 화학물질이 남아있을 수 있다.
- 그러면 퀄리티에 해로우니까 챔버는 특정 갯수($k$)의 웨이퍼를 공정한 이후 clean된다.
- $purge$ : $k$ = 1인 Chamber cleaning
- wafer cleaning process : etching, chemical vapor deposition, physical vapor deposition 등. 공정의 약 50%∼80%가 purge 된다.
- purge operation 소요시간 : 약 30~300초, 그동안 해당 챔버는 공정 불가
- 따라서 클러스터툴은 cleaning(or purge) operation은 스케줄링에 고려되어야 한다.
- 하지만 해당 공정의 최적화는 쉽지않음. 클리닝이 없을때의 backward sequence가 optimal이어도, 클리닝이 추가되면 더이상 optimal이 아니고 cycle time도 크게 증가
- **$z = [z_1, z_2, \cdots, z_n]$** : n개의 프로세싱 모듈에서, 각 모듈이 병렬 챔버로 되어있을때, 각 공정마다 비어있는 챔버의 갯수
- 예) $z_2 = 3$ : 공정2에서 비어있는 챔버는 3개
- 1. 우리는 특정 z가 주어졌을 때(= 어떤 공정단계에서 몇개의 챔버가 비어져있는지 알 때), backward(z)가 글로벌 옵티멀(최소 싸이클 타임)하게 되는 조건을 알아낸다.
- 2. 옵티멀 벡터 z를 성취하기 위한 최적 모델 제안
- 3. 그런 다음, 우리는 싸이클 타임이 증가하지 않는 z값에 대한 범위 제안

- 실험환경 : backward($0$) : full loading된 상황
- 주어진 실험환경에서 partial loading $z$가 툴의 싸이클타임을 상당히 줄이는 것을 보여주겠다.
- 사이클 시간이 퍼지 작업을 위해 병렬 챔버를 예약하는 방법에 따라 크게 달라진다고 결론짓는다.
- 과도한 툴의 유휴시간은 웨이퍼 퀄리티 관점에서 안좋다.

<br><br><br>

#### **[ 2. WORKLOAD ANALYSIS OF SINGLE-ARMED CLUSTER TOOLS WITH PURGE OPERATIONS ]**

- 싸이클타임 분석과 최적화를 위해서, purge operation이 있을 때, 챔버들과 로봇에 대한 workload 분석이 필수
- **workload** : 리소스에서 웨이퍼를 처리하는 데 필요한 시간 또는 웨이퍼를 생성하는 데 걸리는 시간관 동등. 특정 리소스가 한 work cycle을 돌기위해 최소로 요구되는 시간, 그래서 그 최소로 요구되는 시간의 lower bound를 제공한다, 다른 자원의 work cycle에 의한 간섭으로 지연될 수도 있다.
- 클러스터 툴에서의 workload는 1. 제안된 툴 작동 시퀀스의 최적성을 입증 2. branch and bound 절차에서 lower bound를 개발하기 위해 정의되어 사용되었다.
- purge operations도 함께 고려하기 위해서 workload정의를 확장해야하된다.
- **n개**의 process step이 sequentially하게 있음
- 각 process step $i$는 **$m_i$개의 병렬 챔버**를 가진다.
- process steop $i$에서 **Process time : $p_i$**
- process steop $i$에서 **cleaning time : $c_i$**
- loading, unloading : $w$
- moving time : $v$
- **purge operation 고려하지 않을떄 : 로봇의 workload : $(n+1)(2w+2v)$**
- **챔버의 workload : $\frac{1}{m_i} (p_i + 4w + 3v)$**
- 이제 purge operation을 고려해서 workload를 생각해보자.
- purge operation은 웨이퍼가 step $i$의 챔버에서 언로드 되면서 시작된다.
- purge operation이 끝나야지만 wafer loading가능
- 따라서, 한 챔버에서 **wafer process work cycle : $p_i + 2w + c_i$**
- purge operation이 끝나면, 1. 로봇은 **moves**하여 그 챔버에서 웨이퍼 **unload**하고 그 뺀 웨이퍼를 다음 step $i + 1$에 **load**
- 2. 그리고나서 **moves**해서 이전 step $i-1$에서 **unload**
- 3. 다시 step $i$의 챔버로 **moves**하여 **load**
- purge time $c_i$가 2w + 3v보다 작다면, process step i의 해당 챔버의 웨이퍼 생산 시간 : $(p_i + 2w) + (2w + 3v) = p_i + 4w + 3v$
- 그렇지 않다면, $p_i + 2w + c_i$ (Fig2 참고)
- 따라서, purge operation이 고려된 챔버의 workload : $\frac{1}{m_i} \{p_i + 2w + max(2w + 3v, c_i)\}$
- **maximum workload(tool workload) : $\psi \equiv max[max_{i=1, \cdots, n} (1 / m_i) \{p_i + 2w + max(2w + 3c, c_i)\}, (n+1)(2w+2v)]$**
- 의미 정확히 알아내야됨

<br><br><br>

#### **[ 3. EXTENDED BACKWARD SEQUENCE ]**
- 일반적인 single-armed tool의 backward sequence : process step n의 챔버에서 unload하여 loadlock에 놓고 그 이전 스텝도 쭉쭉쭉
- full work cycle(full tool cycle)(또는 LCM cycle) : step 1에서 step n까지 그 process step의 병렬 챔버의 최소공배수 만큼 웨이퍼 흐름을 반복하는것
- 예시) process step = 3이라면, LCM : $m_1 \times m_2 \times m_3$
- $C_{i, j}$ : process step $i$의 $j$번째 병렬챔버
- 일반적인 backward sequence with full loading은 cleaning time에 비례해서 robot delay시간이 길어진다.
- 예시) process step i에서 웨이퍼를 unload한 로봇은 $C_{i+1}$ (process step i+1의 cleaning time)동안 기다려야한다.
- **결과적으로, step $i+1$에서, 얼마나 많은 수의 챔버를 채우고 얼마나 많은 수의 챔버를 비워놓는지가 중요하다.** 
- 따라서, 의사결정은 robot waiting time과 step i+1의 생산량 간의 상관관계를 가진다.
- cleaning 그 자체는 챔버와 로봇간에 행해져야하는 또다른 job이다 !!
- **EXTENDED BACKWARD SEQUENCE = $backward sequence with partial loading$**

<br><br>

**A. Backward($z$) Sequence**
- $z_i$ : process step $i$의 **빈** parallel chamber들 수
- $m_i - z_i$ : 공정 진행중인 parallel chamber들 수
- $backward(z)$ : partial loading이 있는 backward sequence $z = [z_1, \cdots, z_n]$
- 데드락이 일어나지 않기 위해서 모든 $i = 1, 2, \cdots, n$에서 $z_i \le m_i - 1$를 유지해야한다.
- $z_i > m_i - 1$이라면, 단계 i에서 언로드할 웨이퍼가 없기 때문에 backward sequence를 적용할 수 없다.??
- 이제, 각 프로세스 단계의 병렬 챔버가 사용되는 순서를 결정해보자
- 로봇은 각 프로세스 단계의 병렬 챔버에서 요청이 이루어진 순서대로 요청을 load 또는 unload한다. first-comefirst-served (FCFS) 이것은 cyclic한 order를 만든다.
- 이것은 cyclic한 order를 만든다. process times, cleaning times, 그리고 robot task times는 모두 deterministic하기 때문이다.
- 결론적으로, **backward($z$)는 적절한 $z$값을 수용하여 공정단계 간의 작업량 균형을 맞출수 있습니다**. (작업량 : 웨이퍼 process 뿐만 아니라 챔버 cleaning도 고려)
- $u_{i,j}$ : 챔버 $C_{i,j}$의 unloading task ($u_i$ : 챔버 $C_i$의 ~)
- $l_{i,j}$ : 챔버 $C_{i,j}$의 loading task ($l_i$ : 챔버 $C_i$의 ~)
<br><br>
![Image](https://ifh.cc/g/L3mFFD.jpg)
- 위 Fig에서의 robot task sequence : $u_{3,2} \rightarrow l_4 \rightarrow u_{2,3} \rightarrow l_{3,1} \rightarrow u_1 \rightarrow l_{2,1} \rightarrow u_0 \rightarrow l_1$
- $u_0, l_{n+1}$ : 로드락에서(로)의 unloading, loading
- 위 그림에서는 full tool cycle이 6번 반큼 비슷한 task를 수행한다($m_1 \times m_2 \times m_3 = 6$), 비슷하다는 말은, 같은 cycle이지만 다른 챔버를 이용해서([1,1,1], [1,1,2], [1,2,1] ... [1,3,2] : 6개)

<br><br>

<span style='background-color:#fff5b1'> **B. Timed Event Graph Model for a Tool With Backward(z)** </span>
- TEG : 각 place에서 오직 하나의 input과 output transition을 가지는 TPN의 일종
- 그래서 conflict place가 없으니 의사결정할 일이 없음, 툴은 똑같은 work cycle을 반복할 뿐

- $\mathcal{G}$ = ($P, T, I, P, M_0, H$)인 6개의 튜플로 구성
    - P = {$p_1, p_2, \cdots, p_m$}인 유한한 place들의 집합
    - T = {$t_1, t_2, \cdots, t_n$}인 유한한 transition들의 집합, &nbsp;$P \cup T \ne  \varnothing $, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$P \cap T =  \varnothing $
    - $I:(P \times T) \rightarrow \mathbb{N}$, place에서 transition으로 가는 input function
    - $O:(T \times P) \rightarrow \mathbb{N}$, transition에서 place로 가는 output function
    - $M_0 : P \rightarrow \mathbb{N}$, initial marking, 초기의 petri net상태
    - $H : P \rightarrow \mathbb{R}^+ $, 특정 place에서의 deterministic한 token holding time 또는 특정 transition에서의 time delay들

- backward($z$)인 TEG를 모델링 해보자
- $T \equiv \{ t_1, \cdots, t_{2(n+1)} \}$ : robot task의 시작 혹은 완료, 챔버로의 loading, unloading같은
- $P_r \equiv \{ p_1^r, \cdots, p_{2(n+1)}^r \}$ : robot moving을 나타내는 place
- $P_c \equiv \{ p_1^c, \cdots, p_{2(n+1)}^c \}$ : cleaning operation을 나타내는 place
    - $p_i^c : 청소중인 or 비어있는(??) 챔버 수
- $P_p \equiv \{ p_1^p, \cdots, p_{2(n+1)}^p \}$ : wafer processing을 나타내는 place
    - $p_i^p$ : 웨이퍼를 가공중인 챔버 수
- $p_i^p + p_i^c = m_i$
<br><br>
![Image](https://ifh.cc/g/XhWhn1.png)
<br><br>
- **Token Holding Time**
    - : $P_r : v$
    - : $p_i^p$ : 공정 i에서의 processing time
    - : $p_i^c$ : 공정 i에서의 cleaning time
<br><br>

- $\tau_p$ : place $p$에서의 토큰 수

- (3) : $\sum_{p\in P_r} \tau_p = 1$ : 모든 place에서의 토큰수는 1개, sigle-arm 의미
- (4) : $\tau_{p_i^p} + \tau_{p_i^c} = m_i$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\forall i = 1, \cdots, n$ : 각 스텝 i에서의 processing place와 cleaning place의 토큰의 수의 합은 그 스텝 i에서의 모든 챔버의 수($m_i$)와 같다.
- (5) : $\tau_{p_{n-i+1}^p} + \tau_{p_{2i-1}^r} + \tau_{p_{2i}^r} + \tau_{p_{2i + 1}^r}$ = $m_{n - i + 1} - z_{n - i + 1}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\forall i = 1, \cdots, n$ : 우항 먼저보면, 특정 스텝 n-i+1에서 모든 병렬챔버의 수 - 빈 챔버의 수 = ??

<br><br>

<span style='background-color:#fff5b1'> **C . Tool Cycle Time for Backward($z$)** <\span>

- **circuit ratio** : $R_i$로 표기, 각 리소스(로봇, 챔버)들의 입장에서 한 cycle을 도는데의 소요시간, not 비율

> ## $\frac{place들의\;token\;holding\;time들\;+\;transition들의\;firing\;delay들}{해당\; circuit\;전체의\;토큰\;수}$
<br><br>

![Image](https://ifh.cc/g/2SaHw4.png)
- (6) : $R_1 = (n + 1)(2v + 2w)$ : robot work cycle의 circuit ratio

<br>

![Image](https://ifh.cc/g/8QbWA4.png)

- (7) : $R_2 (i) = \frac{1}{m_i} (p_i + c_i + 2w)$ : 챔버 상 에서 cleaning과 processing간의 스위칭
<br><br><br>

![Image](https://ifh.cc/g/DWj2gb.png)

- (8) : $R_3 (i) = \frac{1}{m_i - z_i} (p_i + 3v + 4w)$ : 한 챔버에서의 processing과정, 완료된 웨이퍼 unload, 새 웨이퍼 load



- (9) : $R_4(A) = \frac{1}{1 + \sum_{i \in A^{Z_i}}} \times \{ (n + 1 - 2|A| )( 2v + 2w ) + \sum_{i \in A} (2w + v + c_i)\}$ : robot task와 cleaning operation간의 연결, 어떤 클리닝, 몇 개의 클리닝과 연결되는지에 따라 여러 조합의 경우의 수 나옴
- **A : roboy task와 이을수있는, 인접하지 않은 cleaning(process도 ??) place들의 subset**
- **S : roboy task와 이을 수 있는 모든 후보 cleaning(process도??) place들**
- 어느 process step $i$에서 $z_i$가 증가하면, circuit ratio $R_3(i)$는 증가하고, $S$에 있는 어느$A$든지 다 $R_4(A)$가 감소한다.
- 그말은 즉, $z_i$에 적절히 웨이퍼를 loading하면 processing과 cleaning 챔버 간의 workload를 균형맞출수 있다.
- $Theorem 2$ : $max[R_1,\quad max_{\forall i=1, \cdots, n} R_2 (i), \quad max_{\forall i = 1, \cdots, n} R_3 (i), \quad max_{\forall A \in S} R_4 (A)]$
- : backward($z$)로 동작하는 series-parallel 챔버들의 single-armed cluster tool의 cycle time

<br><br>

-**D. Optimality of Backward($z$)**
- backward($z$)의 cycle time은 loading $z$에 의해 정해진다.
- 그래서 tool configuration, proccess time, robot task time등과 같은 파라미터들이 주어진 문제상황에서 우리는 **optimal loading z**를 먼저 정해야한다.
- **그리고나서 cycle time( $\lambda_{backward(z∗)}$ )을 다른 모든 가능한 시퀀스들의 cycle time과 비교한다.**
- 그랬을 때도 해당 cycle time이 제일 작으면 그것이 **$global \; optimal$**

